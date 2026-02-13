---
name: vm-network-troubleshooting
description: >-
  Diagnose and troubleshoot network connectivity issues in virtual machines
  across cloud providers (AWS, Azure, GCP). Includes connectivity diagnostics,
  DNS troubleshooting, route analysis, firewall inspection, and remediation
  suggestions.
metadata:
  author: telnyx
  product: vm-troubleshooting
  language: python
  category: infrastructure
  cloud_providers:
    - aws
    - azure
    - gcp
    - generic
---

# VM Network Troubleshooting Skill

A comprehensive skill for diagnosing and troubleshooting network connectivity issues in virtual machines across cloud environments.

## Overview

This skill provides systematic approaches to diagnose common VM networking problems including:
- Connectivity failures
- DNS resolution issues
- Routing problems
- Firewall misconfigurations
- Interface configuration errors

## Prerequisites

### Python Dependencies

```bash
pip install boto3 azure-mgmt-compute azure-mgmt-network google-cloud-compute dnspython paramiko
```

### Required Permissions

#### AWS IAM Permissions
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeRouteTables",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeNetworkAcls",
        "logs:GetLogEvents",
        "logs:FilterLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

#### Azure RBAC Permissions
- `Reader` role on the VM resource group
- `Network Contributor` for network diagnostics

#### GCP IAM Permissions
- `compute.instances.get`
- `compute.networks.get`
- `compute.firewalls.list`
- `compute.routes.list`

---

## 1. Connectivity Diagnostics

### 1.1 Basic Connectivity Test (Ping)

Test basic ICMP connectivity to a target host.

```python
import subprocess
import platform

def ping_host(target: str, count: int = 4, timeout: int = 5) -> dict:
    """
    Test ICMP connectivity to a target host.
    
    Args:
        target: IP address or hostname to ping
        count: Number of ping packets to send
        timeout: Timeout in seconds
    
    Returns:
        dict with success status, latency stats, and packet loss
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    timeout_param = '-w' if platform.system().lower() == 'windows' else '-W'
    
    cmd = ['ping', param, str(count), timeout_param, str(timeout), target]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout * count + 5)
        output = result.stdout
        
        # Parse results
        packet_loss = 0
        avg_latency = None
        
        if 'packet loss' in output.lower() or 'lost' in output.lower():
            # Extract packet loss percentage
            import re
            loss_match = re.search(r'(\d+)%\s*(packet\s*)?loss', output, re.IGNORECASE)
            if loss_match:
                packet_loss = int(loss_match.group(1))
        
        # Extract average latency
        latency_match = re.search(r'avg[^=]*=\s*([\d.]+)', output) or \
                       re.search(r'Average\s*=\s*([\d.]+)', output)
        if latency_match:
            avg_latency = float(latency_match.group(1))
        
        return {
            'success': result.returncode == 0 and packet_loss < 100,
            'target': target,
            'packet_loss_percent': packet_loss,
            'avg_latency_ms': avg_latency,
            'raw_output': output
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'target': target,
            'error': 'Ping timeout expired',
            'packet_loss_percent': 100
        }
    except Exception as e:
        return {
            'success': False,
            'target': target,
            'error': str(e)
        }

# Example usage
result = ping_host('8.8.8.8')
print(f"Connectivity to {result['target']}: {'OK' if result['success'] else 'FAILED'}")
if result.get('avg_latency_ms'):
    print(f"Average latency: {result['avg_latency_ms']}ms")
```

### 1.2 TCP Port Connectivity Test

Test TCP connectivity to specific ports.

```python
import socket
from typing import List, Optional

def test_tcp_port(host: str, port: int, timeout: int = 5) -> dict:
    """
    Test TCP connectivity to a specific port.
    
    Args:
        host: Target hostname or IP
        port: TCP port number
        timeout: Connection timeout in seconds
    
    Returns:
        dict with connection status and details
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        result = sock.connect_ex((host, port))
        
        if result == 0:
            return {
                'success': True,
                'host': host,
                'port': port,
                'status': 'open',
                'message': f'Port {port} is open and accepting connections'
            }
        else:
            return {
                'success': False,
                'host': host,
                'port': port,
                'status': 'closed',
                'error_code': result,
                'message': f'Port {port} is closed or filtered'
            }
    except socket.timeout:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'timeout',
            'message': f'Connection to port {port} timed out'
        }
    except socket.gaierror as e:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'dns_error',
            'message': f'DNS resolution failed: {e}'
        }
    except Exception as e:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'error',
            'message': str(e)
        }
    finally:
        sock.close()

def test_common_ports(host: str, ports: Optional[List[int]] = None) -> List[dict]:
    """
    Test connectivity to common service ports.
    
    Args:
        host: Target hostname or IP
        ports: List of ports to test (defaults to common ports)
    
    Returns:
        List of test results for each port
    """
    if ports is None:
        ports = [22, 80, 443, 3389, 5432, 3306, 6379, 27017]
    
    results = []
    for port in ports:
        result = test_tcp_port(host, port)
        results.append(result)
    
    return results

# Example usage
results = test_common_ports('192.168.1.100', [22, 80, 443])
for r in results:
    status = '✓' if r['success'] else '✗'
    print(f"{status} Port {r['port']}: {r['status']}")
```

### 1.3 SSH Connectivity Test

Test SSH connectivity and authentication.

```python
import paramiko
from typing import Optional

def test_ssh_connection(
    host: str,
    username: str,
    password: Optional[str] = None,
    key_filename: Optional[str] = None,
    port: int = 22,
    timeout: int = 10
) -> dict:
    """
    Test SSH connectivity to a VM.
    
    Args:
        host: Target hostname or IP
        username: SSH username
        password: SSH password (optional)
        key_filename: Path to SSH private key (optional)
        port: SSH port (default 22)
        timeout: Connection timeout
    
    Returns:
        dict with connection status and details
    """
    client = paramiko.SSHClient()
    # WARNING: AutoAddPolicy automatically accepts all host keys, which is a security risk.
    # For production use, consider using RejectPolicy or a custom policy with known host verification.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            key_filename=key_filename,
            timeout=timeout,
            allow_agent=False,
            look_for_keys=False if (password or key_filename) else True
        )
        
        # Test command execution
        stdin, stdout, stderr = client.exec_command('echo "SSH_TEST_OK"', timeout=5)
        output = stdout.read().decode().strip()
        
        return {
            'success': True,
            'host': host,
            'port': port,
            'username': username,
            'message': 'SSH connection successful',
            'test_output': output
        }
    except paramiko.AuthenticationException:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'auth_failed',
            'message': 'SSH authentication failed - check credentials'
        }
    except paramiko.SSHException as e:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'ssh_error',
            'message': f'SSH error: {e}'
        }
    except Exception as e:
        return {
            'success': False,
            'host': host,
            'port': port,
            'status': 'connection_error',
            'message': str(e)
        }
    finally:
        client.close()

# Example usage (use environment variables for credentials)
import os
result = test_ssh_connection(
    host='192.168.1.100',
    username=os.environ.get('SSH_USER', 'ubuntu'),
    key_filename=os.environ.get('SSH_KEY_PATH')
)
print(f"SSH Test: {result['message']}")
```

---

## 2. DNS Troubleshooting

### 2.1 DNS Resolution Test

Test DNS resolution using multiple methods.

```python
import socket
import dns.resolver
from typing import List, Optional

def resolve_dns(
    hostname: str,
    record_type: str = 'A',
    nameserver: Optional[str] = None
) -> dict:
    """
    Resolve DNS records for a hostname.
    
    Args:
        hostname: Domain name to resolve
        record_type: DNS record type (A, AAAA, MX, CNAME, TXT, NS)
        nameserver: Specific DNS server to query (optional)
    
    Returns:
        dict with resolution results
    """
    resolver = dns.resolver.Resolver()
    
    if nameserver:
        resolver.nameservers = [nameserver]
    
    try:
        answers = resolver.resolve(hostname, record_type)
        records = [str(rdata) for rdata in answers]
        
        return {
            'success': True,
            'hostname': hostname,
            'record_type': record_type,
            'nameserver': nameserver or 'system default',
            'records': records,
            'ttl': answers.ttl
        }
    except dns.resolver.NXDOMAIN:
        return {
            'success': False,
            'hostname': hostname,
            'record_type': record_type,
            'error': 'NXDOMAIN',
            'message': f'Domain {hostname} does not exist'
        }
    except dns.resolver.NoAnswer:
        return {
            'success': False,
            'hostname': hostname,
            'record_type': record_type,
            'error': 'NoAnswer',
            'message': f'No {record_type} records found for {hostname}'
        }
    except dns.resolver.Timeout:
        return {
            'success': False,
            'hostname': hostname,
            'record_type': record_type,
            'error': 'Timeout',
            'message': 'DNS query timed out'
        }
    except Exception as e:
        return {
            'success': False,
            'hostname': hostname,
            'record_type': record_type,
            'error': str(type(e).__name__),
            'message': str(e)
        }

def check_dns_servers(dns_servers: Optional[List[str]] = None) -> List[dict]:
    """
    Test connectivity to DNS servers.
    
    Args:
        dns_servers: List of DNS server IPs to test
    
    Returns:
        List of test results for each DNS server
    """
    if dns_servers is None:
        dns_servers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
    
    results = []
    test_domain = 'google.com'
    
    for server in dns_servers:
        result = resolve_dns(test_domain, 'A', server)
        result['dns_server'] = server
        results.append(result)
    
    return results

# Example usage
result = resolve_dns('example.com', 'A')
print(f"DNS Resolution: {result}")

# Test multiple DNS servers
dns_results = check_dns_servers()
for r in dns_results:
    status = '✓' if r['success'] else '✗'
    print(f"{status} DNS Server {r['dns_server']}: {r.get('records', r.get('message'))}")
```

### 2.2 Reverse DNS Lookup

Perform reverse DNS lookups.

```python
import socket
import dns.reversename
import dns.resolver

def reverse_dns_lookup(ip_address: str) -> dict:
    """
    Perform reverse DNS lookup for an IP address.
    
    Args:
        ip_address: IP address to look up
    
    Returns:
        dict with reverse DNS results
    """
    try:
        # Method 1: Using socket
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        
        return {
            'success': True,
            'ip_address': ip_address,
            'hostname': hostname,
            'method': 'socket'
        }
    except socket.herror as e:
        # Try dnspython as fallback
        try:
            rev_name = dns.reversename.from_address(ip_address)
            answers = dns.resolver.resolve(rev_name, 'PTR')
            hostname = str(answers[0]).rstrip('.')
            
            return {
                'success': True,
                'ip_address': ip_address,
                'hostname': hostname,
                'method': 'dnspython'
            }
        except Exception as dns_e:
            return {
                'success': False,
                'ip_address': ip_address,
                'error': 'No PTR record',
                'message': f'No reverse DNS entry found for {ip_address}'
            }

# Example usage
result = reverse_dns_lookup('8.8.8.8')
print(f"Reverse DNS: {result}")
```

### 2.3 Check VM DNS Configuration

Check DNS configuration on a VM via SSH.

```python
def check_vm_dns_config(ssh_client) -> dict:
    """
    Check DNS configuration on a Linux VM.
    
    Args:
        ssh_client: Connected paramiko SSH client
    
    Returns:
        dict with DNS configuration details
    """
    config = {}
    
    # Check /etc/resolv.conf
    stdin, stdout, stderr = ssh_client.exec_command('cat /etc/resolv.conf')
    resolv_conf = stdout.read().decode()
    config['resolv_conf'] = resolv_conf
    
    # Extract nameservers
    nameservers = []
    for line in resolv_conf.split('\n'):
        if line.strip().startswith('nameserver'):
            ns = line.split()[1] if len(line.split()) > 1 else None
            if ns:
                nameservers.append(ns)
    config['nameservers'] = nameservers
    
    # Check systemd-resolved status (if applicable)
    stdin, stdout, stderr = ssh_client.exec_command('systemctl is-active systemd-resolved 2>/dev/null')
    resolved_status = stdout.read().decode().strip()
    config['systemd_resolved'] = resolved_status == 'active'
    
    if config['systemd_resolved']:
        stdin, stdout, stderr = ssh_client.exec_command('resolvectl status 2>/dev/null')
        config['resolvectl_output'] = stdout.read().decode()
    
    # Test DNS resolution from VM
    stdin, stdout, stderr = ssh_client.exec_command('nslookup google.com 2>&1')
    config['nslookup_test'] = stdout.read().decode()
    
    return config

# Example usage (requires established SSH connection)
# config = check_vm_dns_config(ssh_client)
# print(f"Nameservers: {config['nameservers']}")
```

---

## 3. Route Analysis

### 3.1 Traceroute

Trace the network path to a destination.

```python
import subprocess
import platform
import re
from typing import List

def traceroute(target: str, max_hops: int = 30, timeout: int = 60) -> dict:
    """
    Trace the network path to a target.
    
    Args:
        target: Destination hostname or IP
        max_hops: Maximum number of hops
        timeout: Overall timeout in seconds
    
    Returns:
        dict with traceroute results
    """
    system = platform.system().lower()
    
    if system == 'windows':
        cmd = ['tracert', '-h', str(max_hops), target]
    else:
        cmd = ['traceroute', '-m', str(max_hops), '-w', '2', target]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        output = result.stdout
        
        # Parse hops
        hops = []
        for line in output.split('\n'):
            # Match hop lines (e.g., "1  192.168.1.1  1.234 ms")
            hop_match = re.match(r'\s*(\d+)\s+(.+)', line)
            if hop_match:
                hop_num = int(hop_match.group(1))
                hop_data = hop_match.group(2)
                
                # Extract IP and latency
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', hop_data)
                latency_match = re.findall(r'([\d.]+)\s*ms', hop_data)
                
                hops.append({
                    'hop': hop_num,
                    'ip': ip_match.group(1) if ip_match else None,
                    'latencies_ms': [float(l) for l in latency_match] if latency_match else [],
                    'raw': hop_data.strip()
                })
        
        return {
            'success': True,
            'target': target,
            'hops': hops,
            'total_hops': len(hops),
            'raw_output': output
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'target': target,
            'error': 'Traceroute timed out'
        }
    except Exception as e:
        return {
            'success': False,
            'target': target,
            'error': str(e)
        }

# Example usage
result = traceroute('8.8.8.8')
if result['success']:
    print(f"Route to {result['target']} ({result['total_hops']} hops):")
    for hop in result['hops']:
        print(f"  {hop['hop']}: {hop['ip'] or '*'} - {hop['latencies_ms']}")
```

### 3.2 Get Routing Table

Retrieve the local routing table.

```python
import subprocess
import platform
import re

def get_routing_table() -> dict:
    """
    Get the local routing table.
    
    Returns:
        dict with routing table entries
    """
    system = platform.system().lower()
    
    if system == 'windows':
        cmd = ['route', 'print']
    elif system == 'darwin':
        cmd = ['netstat', '-rn']
    else:
        cmd = ['ip', 'route', 'show']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout
        
        routes = []
        
        if system == 'linux':
            for line in output.strip().split('\n'):
                parts = line.split()
                if len(parts) >= 3:
                    route = {
                        'destination': parts[0],
                        'raw': line
                    }
                    
                    # Parse common fields
                    if 'via' in parts:
                        idx = parts.index('via')
                        route['gateway'] = parts[idx + 1] if idx + 1 < len(parts) else None
                    
                    if 'dev' in parts:
                        idx = parts.index('dev')
                        route['interface'] = parts[idx + 1] if idx + 1 < len(parts) else None
                    
                    routes.append(route)
        
        return {
            'success': True,
            'routes': routes,
            'raw_output': output
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def check_default_gateway() -> dict:
    """
    Check if a default gateway is configured and reachable.
    
    Returns:
        dict with default gateway status
    """
    routing = get_routing_table()
    
    if not routing['success']:
        return routing
    
    # Find default route
    default_gw = None
    for route in routing['routes']:
        if route['destination'] in ['default', '0.0.0.0', '0.0.0.0/0']:
            default_gw = route.get('gateway')
            break
    
    if not default_gw:
        return {
            'success': False,
            'error': 'No default gateway configured',
            'recommendation': 'Configure a default gateway for internet connectivity'
        }
    
    # Test gateway reachability
    ping_result = ping_host(default_gw, count=3)
    
    return {
        'success': ping_result['success'],
        'default_gateway': default_gw,
        'reachable': ping_result['success'],
        'latency_ms': ping_result.get('avg_latency_ms'),
        'recommendation': None if ping_result['success'] else 'Default gateway is not responding to ping'
    }

# Example usage
gw_status = check_default_gateway()
print(f"Default Gateway: {gw_status.get('default_gateway')}")
print(f"Reachable: {gw_status.get('reachable')}")
```

### 3.3 MTR (My Traceroute)

Run MTR for combined ping and traceroute analysis.

```python
import subprocess
import json

def run_mtr(target: str, count: int = 10) -> dict:
    """
    Run MTR (My Traceroute) for detailed path analysis.
    
    Args:
        target: Destination hostname or IP
        count: Number of pings per hop
    
    Returns:
        dict with MTR results
    """
    try:
        # Try JSON output first (newer mtr versions)
        cmd = ['mtr', '--json', '-c', str(count), target]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            try:
                mtr_data = json.loads(result.stdout)
                return {
                    'success': True,
                    'target': target,
                    'data': mtr_data,
                    'format': 'json'
                }
            except json.JSONDecodeError:
                pass
        
        # Fallback to report mode
        cmd = ['mtr', '--report', '-c', str(count), target]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        return {
            'success': result.returncode == 0,
            'target': target,
            'raw_output': result.stdout,
            'format': 'text'
        }
    except FileNotFoundError:
        return {
            'success': False,
            'error': 'mtr not installed',
            'recommendation': 'Install mtr: apt-get install mtr / yum install mtr'
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'MTR timed out'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

# Example usage
# result = run_mtr('8.8.8.8')
# print(result)
```

---

## 4. Firewall Inspection

### 4.1 Check Local Firewall Rules (Linux)

Inspect iptables/nftables rules on Linux.

```python
import subprocess

def get_iptables_rules() -> dict:
    """
    Get iptables firewall rules.
    
    Returns:
        dict with firewall rules
    """
    rules = {}
    
    try:
        # Get all tables
        for table in ['filter', 'nat', 'mangle']:
            cmd = ['iptables', '-t', table, '-L', '-n', '-v', '--line-numbers']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                rules[table] = result.stdout
        
        return {
            'success': True,
            'firewall_type': 'iptables',
            'rules': rules
        }
    except FileNotFoundError:
        # Try nftables
        try:
            cmd = ['nft', 'list', 'ruleset']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            return {
                'success': result.returncode == 0,
                'firewall_type': 'nftables',
                'rules': {'ruleset': result.stdout}
            }
        except FileNotFoundError:
            return {
                'success': False,
                'error': 'No firewall tool found (iptables/nftables)'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def check_port_allowed(port: int, protocol: str = 'tcp') -> dict:
    """
    Check if a specific port is allowed through the firewall.
    
    Args:
        port: Port number to check
        protocol: Protocol (tcp/udp)
    
    Returns:
        dict with port status
    """
    rules = get_iptables_rules()
    
    if not rules['success']:
        return rules
    
    # Simple check - look for port in rules
    port_str = str(port)
    filter_rules = rules['rules'].get('filter', '')
    
    # Check for explicit ACCEPT rules
    accept_found = f'dpt:{port_str}' in filter_rules and 'ACCEPT' in filter_rules
    drop_found = f'dpt:{port_str}' in filter_rules and ('DROP' in filter_rules or 'REJECT' in filter_rules)
    
    return {
        'success': True,
        'port': port,
        'protocol': protocol,
        'explicitly_allowed': accept_found,
        'explicitly_blocked': drop_found,
        'recommendation': 'Check firewall rules manually for complex configurations'
    }

# Example usage
rules = get_iptables_rules()
if rules['success']:
    print(f"Firewall type: {rules['firewall_type']}")
```

### 4.2 Check Windows Firewall

Inspect Windows Firewall rules.

```python
import subprocess
import platform

def get_windows_firewall_rules(port: int = None) -> dict:
    """
    Get Windows Firewall rules.
    
    Args:
        port: Optional port to filter rules
    
    Returns:
        dict with firewall rules
    """
    if platform.system().lower() != 'windows':
        return {
            'success': False,
            'error': 'Not a Windows system'
        }
    
    try:
        if port:
            cmd = ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 
                   'name=all', f'localport={port}']
        else:
            cmd = ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all']
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        return {
            'success': result.returncode == 0,
            'rules': result.stdout,
            'port_filter': port
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_windows_firewall_status() -> dict:
    """
    Get Windows Firewall status for all profiles.
    
    Returns:
        dict with firewall status
    """
    if platform.system().lower() != 'windows':
        return {'success': False, 'error': 'Not a Windows system'}
    
    try:
        cmd = ['netsh', 'advfirewall', 'show', 'allprofiles', 'state']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        return {
            'success': result.returncode == 0,
            'status': result.stdout
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}
```

---

## 5. Cloud Provider Integration

### 5.1 AWS EC2 Network Diagnostics

Retrieve network information from AWS EC2.

```python
import boto3
from typing import Optional

class AWSNetworkDiagnostics:
    """AWS EC2 network diagnostics helper."""
    
    def __init__(self, region: Optional[str] = None):
        """
        Initialize AWS diagnostics.
        
        Args:
            region: AWS region (uses default if not specified)
        """
        self.ec2 = boto3.client('ec2', region_name=region)
        self.region = region
    
    def get_instance_network_info(self, instance_id: str) -> dict:
        """
        Get network information for an EC2 instance.
        
        Args:
            instance_id: EC2 instance ID
        
        Returns:
            dict with network configuration
        """
        try:
            response = self.ec2.describe_instances(InstanceIds=[instance_id])
            
            if not response['Reservations']:
                return {'success': False, 'error': 'Instance not found'}
            
            instance = response['Reservations'][0]['Instances'][0]
            
            network_info = {
                'success': True,
                'instance_id': instance_id,
                'vpc_id': instance.get('VpcId'),
                'subnet_id': instance.get('SubnetId'),
                'private_ip': instance.get('PrivateIpAddress'),
                'public_ip': instance.get('PublicIpAddress'),
                'private_dns': instance.get('PrivateDnsName'),
                'public_dns': instance.get('PublicDnsName'),
                'security_groups': [
                    {'id': sg['GroupId'], 'name': sg['GroupName']}
                    for sg in instance.get('SecurityGroups', [])
                ],
                'network_interfaces': []
            }
            
            for eni in instance.get('NetworkInterfaces', []):
                network_info['network_interfaces'].append({
                    'id': eni['NetworkInterfaceId'],
                    'subnet_id': eni['SubnetId'],
                    'private_ip': eni['PrivateIpAddress'],
                    'mac_address': eni['MacAddress'],
                    'status': eni['Status']
                })
            
            return network_info
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_security_group_rules(self, security_group_id: str) -> dict:
        """
        Get security group rules.
        
        Args:
            security_group_id: Security group ID
        
        Returns:
            dict with inbound and outbound rules
        """
        try:
            response = self.ec2.describe_security_groups(GroupIds=[security_group_id])
            
            if not response['SecurityGroups']:
                return {'success': False, 'error': 'Security group not found'}
            
            sg = response['SecurityGroups'][0]
            
            return {
                'success': True,
                'security_group_id': security_group_id,
                'name': sg['GroupName'],
                'description': sg['Description'],
                'vpc_id': sg['VpcId'],
                'inbound_rules': sg['IpPermissions'],
                'outbound_rules': sg['IpPermissionsEgress']
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_vpc_route_table(self, vpc_id: str) -> dict:
        """
        Get route tables for a VPC.
        
        Args:
            vpc_id: VPC ID
        
        Returns:
            dict with route table information
        """
        try:
            response = self.ec2.describe_route_tables(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            route_tables = []
            for rt in response['RouteTables']:
                routes = []
                for route in rt['Routes']:
                    routes.append({
                        'destination': route.get('DestinationCidrBlock') or route.get('DestinationIpv6CidrBlock'),
                        'target': route.get('GatewayId') or route.get('NatGatewayId') or route.get('NetworkInterfaceId'),
                        'state': route.get('State')
                    })
                
                route_tables.append({
                    'id': rt['RouteTableId'],
                    'routes': routes,
                    'associations': rt['Associations']
                })
            
            return {
                'success': True,
                'vpc_id': vpc_id,
                'route_tables': route_tables
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_network_acls(self, vpc_id: str) -> dict:
        """
        Get Network ACLs for a VPC.
        
        Args:
            vpc_id: VPC ID
        
        Returns:
            dict with NACL information
        """
        try:
            response = self.ec2.describe_network_acls(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            nacls = []
            for nacl in response['NetworkAcls']:
                nacls.append({
                    'id': nacl['NetworkAclId'],
                    'is_default': nacl['IsDefault'],
                    'entries': nacl['Entries'],
                    'associations': [a['SubnetId'] for a in nacl['Associations']]
                })
            
            return {
                'success': True,
                'vpc_id': vpc_id,
                'network_acls': nacls
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}

# Example usage
# aws_diag = AWSNetworkDiagnostics(region='us-east-1')
# info = aws_diag.get_instance_network_info('i-1234567890abcdef0')
# print(info)
```

### 5.2 Azure VM Network Diagnostics

Retrieve network information from Azure VMs.

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from typing import Optional

class AzureNetworkDiagnostics:
    """Azure VM network diagnostics helper."""
    
    def __init__(self, subscription_id: str):
        """
        Initialize Azure diagnostics.
        
        Args:
            subscription_id: Azure subscription ID
        """
        self.credential = DefaultAzureCredential()
        self.subscription_id = subscription_id
        self.compute_client = ComputeManagementClient(self.credential, subscription_id)
        self.network_client = NetworkManagementClient(self.credential, subscription_id)
    
    def get_vm_network_info(self, resource_group: str, vm_name: str) -> dict:
        """
        Get network information for an Azure VM.
        
        Args:
            resource_group: Resource group name
            vm_name: VM name
        
        Returns:
            dict with network configuration
        """
        try:
            vm = self.compute_client.virtual_machines.get(
                resource_group, vm_name, expand='instanceView'
            )
            
            network_info = {
                'success': True,
                'vm_name': vm_name,
                'resource_group': resource_group,
                'location': vm.location,
                'network_interfaces': []
            }
            
            for nic_ref in vm.network_profile.network_interfaces:
                nic_id = nic_ref.id
                nic_name = nic_id.split('/')[-1]
                nic_rg = nic_id.split('/')[4]
                
                nic = self.network_client.network_interfaces.get(nic_rg, nic_name)
                
                nic_info = {
                    'name': nic.name,
                    'id': nic.id,
                    'mac_address': nic.mac_address,
                    'ip_configurations': []
                }
                
                for ip_config in nic.ip_configurations:
                    ip_info = {
                        'name': ip_config.name,
                        'private_ip': ip_config.private_ip_address,
                        'private_ip_allocation': ip_config.private_ip_allocation_method,
                        'subnet_id': ip_config.subnet.id if ip_config.subnet else None
                    }
                    
                    if ip_config.public_ip_address:
                        pip_id = ip_config.public_ip_address.id
                        pip_name = pip_id.split('/')[-1]
                        pip_rg = pip_id.split('/')[4]
                        pip = self.network_client.public_ip_addresses.get(pip_rg, pip_name)
                        ip_info['public_ip'] = pip.ip_address
                    
                    nic_info['ip_configurations'].append(ip_info)
                
                # Get NSG if attached
                if nic.network_security_group:
                    nsg_id = nic.network_security_group.id
                    nic_info['nsg_id'] = nsg_id
                
                network_info['network_interfaces'].append(nic_info)
            
            return network_info
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_nsg_rules(self, resource_group: str, nsg_name: str) -> dict:
        """
        Get Network Security Group rules.
        
        Args:
            resource_group: Resource group name
            nsg_name: NSG name
        
        Returns:
            dict with NSG rules
        """
        try:
            nsg = self.network_client.network_security_groups.get(resource_group, nsg_name)
            
            rules = {
                'success': True,
                'nsg_name': nsg_name,
                'inbound_rules': [],
                'outbound_rules': []
            }
            
            for rule in nsg.security_rules:
                rule_info = {
                    'name': rule.name,
                    'priority': rule.priority,
                    'access': rule.access,
                    'protocol': rule.protocol,
                    'source': rule.source_address_prefix,
                    'source_port': rule.source_port_range,
                    'destination': rule.destination_address_prefix,
                    'destination_port': rule.destination_port_range
                }
                
                if rule.direction == 'Inbound':
                    rules['inbound_rules'].append(rule_info)
                else:
                    rules['outbound_rules'].append(rule_info)
            
            return rules
        except Exception as e:
            return {'success': False, 'error': str(e)}

# Example usage
# azure_diag = AzureNetworkDiagnostics(subscription_id='your-subscription-id')
# info = azure_diag.get_vm_network_info('my-resource-group', 'my-vm')
# print(info)
```

### 5.3 GCP Compute Engine Network Diagnostics

Retrieve network information from GCP Compute Engine.

```python
from google.cloud import compute_v1
from typing import Optional

class GCPNetworkDiagnostics:
    """GCP Compute Engine network diagnostics helper."""
    
    def __init__(self, project_id: str):
        """
        Initialize GCP diagnostics.
        
        Args:
            project_id: GCP project ID
        """
        self.project_id = project_id
        self.instances_client = compute_v1.InstancesClient()
        self.firewalls_client = compute_v1.FirewallsClient()
        self.routes_client = compute_v1.RoutesClient()
    
    def get_instance_network_info(self, zone: str, instance_name: str) -> dict:
        """
        Get network information for a GCP instance.
        
        Args:
            zone: GCP zone
            instance_name: Instance name
        
        Returns:
            dict with network configuration
        """
        try:
            instance = self.instances_client.get(
                project=self.project_id,
                zone=zone,
                instance=instance_name
            )
            
            network_info = {
                'success': True,
                'instance_name': instance_name,
                'zone': zone,
                'machine_type': instance.machine_type.split('/')[-1],
                'status': instance.status,
                'network_interfaces': []
            }
            
            for nic in instance.network_interfaces:
                nic_info = {
                    'name': nic.name,
                    'network': nic.network.split('/')[-1],
                    'subnetwork': nic.subnetwork.split('/')[-1] if nic.subnetwork else None,
                    'internal_ip': nic.network_ip,
                    'external_ip': None
                }
                
                for access_config in nic.access_configs:
                    if access_config.nat_ip:
                        nic_info['external_ip'] = access_config.nat_ip
                
                network_info['network_interfaces'].append(nic_info)
            
            # Get network tags (used for firewall rules)
            network_info['network_tags'] = list(instance.tags.items) if instance.tags else []
            
            return network_info
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_firewall_rules(self, network: Optional[str] = None) -> dict:
        """
        Get firewall rules for the project.
        
        Args:
            network: Optional network name to filter rules
        
        Returns:
            dict with firewall rules
        """
        try:
            request = compute_v1.ListFirewallsRequest(project=self.project_id)
            firewalls = self.firewalls_client.list(request=request)
            
            rules = []
            for fw in firewalls:
                if network and network not in fw.network:
                    continue
                
                rule = {
                    'name': fw.name,
                    'network': fw.network.split('/')[-1],
                    'direction': fw.direction,
                    'priority': fw.priority,
                    'target_tags': list(fw.target_tags) if fw.target_tags else [],
                    'source_ranges': list(fw.source_ranges) if fw.source_ranges else [],
                    'allowed': [],
                    'denied': []
                }
                
                for allowed in fw.allowed:
                    rule['allowed'].append({
                        'protocol': allowed.ip_protocol,
                        'ports': list(allowed.ports) if allowed.ports else []
                    })
                
                for denied in fw.denied:
                    rule['denied'].append({
                        'protocol': denied.ip_protocol,
                        'ports': list(denied.ports) if denied.ports else []
                    })
                
                rules.append(rule)
            
            return {
                'success': True,
                'firewall_rules': rules
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_routes(self, network: Optional[str] = None) -> dict:
        """
        Get routes for the project.
        
        Args:
            network: Optional network name to filter routes
        
        Returns:
            dict with route information
        """
        try:
            request = compute_v1.ListRoutesRequest(project=self.project_id)
            routes_list = self.routes_client.list(request=request)
            
            routes = []
            for route in routes_list:
                if network and network not in route.network:
                    continue
                
                routes.append({
                    'name': route.name,
                    'network': route.network.split('/')[-1],
                    'dest_range': route.dest_range,
                    'next_hop_gateway': route.next_hop_gateway,
                    'next_hop_ip': route.next_hop_ip,
                    'next_hop_instance': route.next_hop_instance,
                    'priority': route.priority
                })
            
            return {
                'success': True,
                'routes': routes
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}

# Example usage
# gcp_diag = GCPNetworkDiagnostics(project_id='my-project')
# info = gcp_diag.get_instance_network_info('us-central1-a', 'my-instance')
# print(info)
```

---

## 6. Interface Configuration

### 6.1 Get Network Interface Configuration

Retrieve local network interface configuration.

```python
import subprocess
import platform
import socket
import re
from typing import List

def get_network_interfaces() -> dict:
    """
    Get all network interface configurations.
    
    Returns:
        dict with interface details
    """
    system = platform.system().lower()
    interfaces = []
    
    try:
        if system == 'linux':
            # Use ip command
            result = subprocess.run(['ip', '-j', 'addr', 'show'], capture_output=True, text=True)
            
            if result.returncode == 0:
                import json
                try:
                    data = json.loads(result.stdout)
                    for iface in data:
                        iface_info = {
                            'name': iface['ifname'],
                            'state': iface.get('operstate', 'unknown'),
                            'mac_address': iface.get('address'),
                            'mtu': iface.get('mtu'),
                            'ipv4_addresses': [],
                            'ipv6_addresses': []
                        }
                        
                        for addr_info in iface.get('addr_info', []):
                            if addr_info['family'] == 'inet':
                                iface_info['ipv4_addresses'].append({
                                    'address': addr_info['local'],
                                    'prefix_len': addr_info['prefixlen'],
                                    'broadcast': addr_info.get('broadcast')
                                })
                            elif addr_info['family'] == 'inet6':
                                iface_info['ipv6_addresses'].append({
                                    'address': addr_info['local'],
                                    'prefix_len': addr_info['prefixlen']
                                })
                        
                        interfaces.append(iface_info)
                except json.JSONDecodeError:
                    pass
            
            # Fallback to ifconfig
            if not interfaces:
                result = subprocess.run(['ifconfig', '-a'], capture_output=True, text=True)
                # Parse ifconfig output (simplified)
                return {
                    'success': True,
                    'raw_output': result.stdout,
                    'interfaces': []
                }
        
        elif system == 'windows':
            result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
            return {
                'success': True,
                'raw_output': result.stdout,
                'interfaces': []
            }
        
        return {
            'success': True,
            'interfaces': interfaces
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

def validate_ip_configuration(interface_name: str) -> dict:
    """
    Validate IP configuration for a specific interface.
    
    Args:
        interface_name: Network interface name
    
    Returns:
        dict with validation results
    """
    interfaces = get_network_interfaces()
    
    if not interfaces['success']:
        return interfaces
    
    target_iface = None
    for iface in interfaces.get('interfaces', []):
        if iface['name'] == interface_name:
            target_iface = iface
            break
    
    if not target_iface:
        return {
            'success': False,
            'error': f'Interface {interface_name} not found'
        }
    
    issues = []
    recommendations = []
    
    # Check if interface is up
    if target_iface.get('state') != 'UP':
        issues.append(f"Interface {interface_name} is not UP (state: {target_iface.get('state')})")
        recommendations.append(f"Bring interface up: ip link set {interface_name} up")
    
    # Check for IP address
    if not target_iface.get('ipv4_addresses'):
        issues.append(f"No IPv4 address configured on {interface_name}")
        recommendations.append("Configure an IP address or check DHCP")
    
    return {
        'success': len(issues) == 0,
        'interface': interface_name,
        'configuration': target_iface,
        'issues': issues,
        'recommendations': recommendations
    }

# Example usage
interfaces = get_network_interfaces()
if interfaces['success']:
    for iface in interfaces.get('interfaces', []):
        print(f"Interface: {iface['name']}")
        print(f"  State: {iface.get('state')}")
        for ip in iface.get('ipv4_addresses', []):
            print(f"  IPv4: {ip['address']}/{ip['prefix_len']}")
```

---

## 7. Log Collection

### 7.1 Collect Network Logs (Linux)

Collect relevant network logs from a Linux system.

```python
import subprocess
from datetime import datetime, timedelta
from typing import Optional

def collect_network_logs(
    hours: int = 1,
    log_types: Optional[list] = None
) -> dict:
    """
    Collect network-related logs from the system.
    
    Args:
        hours: Number of hours of logs to collect
        log_types: Types of logs to collect
    
    Returns:
        dict with collected logs
    """
    if log_types is None:
        log_types = ['syslog', 'kernel', 'firewall']
    
    logs = {}
    since_time = datetime.now() - timedelta(hours=hours)
    since_str = since_time.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Collect from journalctl if available
        if 'syslog' in log_types:
            cmd = ['journalctl', '--since', since_str, '-u', 'NetworkManager', '--no-pager']
            result = subprocess.run(cmd, capture_output=True, text=True)
            logs['network_manager'] = result.stdout if result.returncode == 0 else None
        
        if 'kernel' in log_types:
            cmd = ['journalctl', '--since', since_str, '-k', '--no-pager', '-g', 'net|eth|ens|enp']
            result = subprocess.run(cmd, capture_output=True, text=True)
            logs['kernel_network'] = result.stdout if result.returncode == 0 else None
        
        if 'firewall' in log_types:
            # Check for iptables logs
            cmd = ['journalctl', '--since', since_str, '--no-pager', '-g', 'iptables|nftables|firewall']
            result = subprocess.run(cmd, capture_output=True, text=True)
            logs['firewall'] = result.stdout if result.returncode == 0 else None
        
        # Also check dmesg for recent network events
        cmd = ['dmesg', '-T', '--level=err,warn']
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            network_dmesg = [line for line in result.stdout.split('\n') 
                           if any(kw in line.lower() for kw in ['eth', 'net', 'link', 'nic'])]
            logs['dmesg_network'] = '\n'.join(network_dmesg)
        
        return {
            'success': True,
            'time_range_hours': hours,
            'logs': logs
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

def collect_aws_vpc_flow_logs(
    log_group_name: str,
    hours: int = 1,
    filter_pattern: Optional[str] = None
) -> dict:
    """
    Collect AWS VPC Flow Logs.
    
    Args:
        log_group_name: CloudWatch log group name
        hours: Number of hours of logs to collect
        filter_pattern: Optional filter pattern
    
    Returns:
        dict with flow log events
    """
    import boto3
    from datetime import datetime, timedelta
    
    try:
        logs_client = boto3.client('logs')
        
        end_time = int(datetime.now().timestamp() * 1000)
        start_time = int((datetime.now() - timedelta(hours=hours)).timestamp() * 1000)
        
        kwargs = {
            'logGroupName': log_group_name,
            'startTime': start_time,
            'endTime': end_time,
            'limit': 1000
        }
        
        if filter_pattern:
            kwargs['filterPattern'] = filter_pattern
        
        response = logs_client.filter_log_events(**kwargs)
        
        events = []
        for event in response.get('events', []):
            events.append({
                'timestamp': event['timestamp'],
                'message': event['message']
            })
        
        return {
            'success': True,
            'log_group': log_group_name,
            'event_count': len(events),
            'events': events
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

# Example usage
# logs = collect_network_logs(hours=2)
# print(f"Collected logs: {list(logs['logs'].keys())}")
```

---

## 8. Remediation Suggestions

### 8.1 Automated Diagnosis and Recommendations

Generate remediation suggestions based on diagnostic findings.

```python
from typing import List, Dict, Any

class NetworkTroubleshooter:
    """Comprehensive VM network troubleshooter with remediation suggestions."""
    
    def __init__(self):
        self.findings = []
        self.recommendations = []
    
    def run_full_diagnosis(
        self,
        target_host: str,
        ports: List[int] = None,
        dns_test_domain: str = 'google.com'
    ) -> dict:
        """
        Run a full network diagnosis.
        
        Args:
            target_host: Target host to diagnose connectivity to
            ports: List of ports to test
            dns_test_domain: Domain to use for DNS tests
        
        Returns:
            dict with diagnosis results and recommendations
        """
        if ports is None:
            ports = [22, 80, 443]
        
        report = {
            'target': target_host,
            'timestamp': datetime.now().isoformat(),
            'tests': {},
            'findings': [],
            'recommendations': []
        }
        
        # 1. Basic connectivity
        ping_result = ping_host(target_host)
        report['tests']['ping'] = ping_result
        
        if not ping_result['success']:
            report['findings'].append({
                'severity': 'high',
                'category': 'connectivity',
                'issue': f'Cannot ping {target_host}',
                'details': ping_result
            })
            report['recommendations'].extend([
                'Check if the target host is powered on and running',
                'Verify network security groups allow ICMP traffic',
                'Check if there is a firewall blocking ICMP',
                'Verify the target IP address is correct',
                'Check routing tables for path to destination'
            ])
        
        # 2. Port connectivity
        for port in ports:
            port_result = test_tcp_port(target_host, port)
            report['tests'][f'port_{port}'] = port_result
            
            if not port_result['success']:
                report['findings'].append({
                    'severity': 'medium',
                    'category': 'port_connectivity',
                    'issue': f'Port {port} is not accessible on {target_host}',
                    'details': port_result
                })
                report['recommendations'].append(
                    f'Check security group/firewall rules for port {port}'
                )
        
        # 3. DNS resolution
        dns_result = resolve_dns(dns_test_domain)
        report['tests']['dns'] = dns_result
        
        if not dns_result['success']:
            report['findings'].append({
                'severity': 'high',
                'category': 'dns',
                'issue': 'DNS resolution failed',
                'details': dns_result
            })
            report['recommendations'].extend([
                'Check /etc/resolv.conf for correct nameserver configuration',
                'Verify DNS server is reachable',
                'Check if systemd-resolved is running correctly',
                'Try using public DNS servers (8.8.8.8, 1.1.1.1)'
            ])
        
        # 4. Default gateway
        gw_result = check_default_gateway()
        report['tests']['default_gateway'] = gw_result
        
        if not gw_result['success']:
            report['findings'].append({
                'severity': 'critical',
                'category': 'routing',
                'issue': 'Default gateway issue',
                'details': gw_result
            })
            report['recommendations'].extend([
                'Configure a default gateway',
                'Check if the gateway IP is correct',
                'Verify the gateway is on the same subnet'
            ])
        
        # 5. Local interface
        iface_result = get_network_interfaces()
        report['tests']['interfaces'] = iface_result
        
        # Generate summary
        report['summary'] = {
            'total_findings': len(report['findings']),
            'critical': len([f for f in report['findings'] if f['severity'] == 'critical']),
            'high': len([f for f in report['findings'] if f['severity'] == 'high']),
            'medium': len([f for f in report['findings'] if f['severity'] == 'medium']),
            'status': 'healthy' if len(report['findings']) == 0 else 'issues_found'
        }
        
        return report
    
    def generate_remediation_script(self, findings: List[Dict[str, Any]]) -> str:
        """
        Generate a remediation script based on findings.
        
        Args:
            findings: List of diagnostic findings
        
        Returns:
            Shell script with remediation commands
        """
        script_lines = [
            '#!/bin/bash',
            '# Auto-generated network remediation script',
            '# Review before executing!',
            '',
            'set -e',
            ''
        ]
        
        for finding in findings:
            category = finding.get('category', '')
            
            if category == 'dns':
                script_lines.extend([
                    '# DNS Remediation',
                    'echo "Checking DNS configuration..."',
                    'cat /etc/resolv.conf',
                    '',
                    '# Uncomment to add Google DNS:',
                    '# echo "nameserver 8.8.8.8" | sudo tee -a /etc/resolv.conf',
                    ''
                ])
            
            elif category == 'connectivity':
                script_lines.extend([
                    '# Connectivity Remediation',
                    'echo "Checking network interface status..."',
                    'ip link show',
                    'ip addr show',
                    '',
                    '# Check routing',
                    'ip route show',
                    ''
                ])
            
            elif category == 'routing':
                script_lines.extend([
                    '# Routing Remediation',
                    'echo "Current routing table:"',
                    'ip route show',
                    '',
                    '# Uncomment to add default route:',
                    '# sudo ip route add default via <GATEWAY_IP>',
                    ''
                ])
        
        return '\n'.join(script_lines)

# Example usage
troubleshooter = NetworkTroubleshooter()
# report = troubleshooter.run_full_diagnosis('192.168.1.100')
# print(f"Status: {report['summary']['status']}")
# print(f"Findings: {report['summary']['total_findings']}")
# for rec in report['recommendations']:
#     print(f"  - {rec}")
```

---

## 9. Complete Troubleshooting Workflow

### 9.1 End-to-End Troubleshooting Example

```python
import json
from datetime import datetime

def troubleshoot_vm_network(
    vm_identifier: str,
    cloud_provider: str = 'generic',
    target_host: str = '8.8.8.8',
    test_ports: list = None,
    **cloud_kwargs
) -> dict:
    """
    Complete VM network troubleshooting workflow.
    
    Args:
        vm_identifier: VM ID or name
        cloud_provider: Cloud provider (aws, azure, gcp, generic)
        target_host: External host to test connectivity
        test_ports: Ports to test
        **cloud_kwargs: Cloud-specific parameters (region, resource_group, etc.)
    
    Returns:
        Comprehensive troubleshooting report
    """
    if test_ports is None:
        test_ports = [22, 80, 443]
    
    report = {
        'vm_identifier': vm_identifier,
        'cloud_provider': cloud_provider,
        'timestamp': datetime.now().isoformat(),
        'cloud_info': None,
        'diagnostics': {},
        'findings': [],
        'recommendations': [],
        'status': 'unknown'
    }
    
    # Step 1: Get cloud-specific information
    if cloud_provider == 'aws':
        aws_diag = AWSNetworkDiagnostics(region=cloud_kwargs.get('region'))
        report['cloud_info'] = aws_diag.get_instance_network_info(vm_identifier)
        
        if report['cloud_info']['success']:
            # Get security group rules
            for sg in report['cloud_info'].get('security_groups', []):
                sg_rules = aws_diag.get_security_group_rules(sg['id'])
                sg['rules'] = sg_rules
    
    elif cloud_provider == 'azure':
        azure_diag = AzureNetworkDiagnostics(
            subscription_id=cloud_kwargs.get('subscription_id')
        )
        report['cloud_info'] = azure_diag.get_vm_network_info(
            cloud_kwargs.get('resource_group'),
            vm_identifier
        )
    
    elif cloud_provider == 'gcp':
        gcp_diag = GCPNetworkDiagnostics(
            project_id=cloud_kwargs.get('project_id')
        )
        report['cloud_info'] = gcp_diag.get_instance_network_info(
            cloud_kwargs.get('zone'),
            vm_identifier
        )
    
    # Step 2: Run local diagnostics
    report['diagnostics']['interfaces'] = get_network_interfaces()
    report['diagnostics']['routing'] = get_routing_table()
    report['diagnostics']['default_gateway'] = check_default_gateway()
    
    # Step 3: Test external connectivity
    report['diagnostics']['ping'] = ping_host(target_host)
    report['diagnostics']['dns'] = resolve_dns('google.com')
    
    # Step 4: Test specific ports
    report['diagnostics']['ports'] = {}
    for port in test_ports:
        report['diagnostics']['ports'][port] = test_tcp_port(target_host, port)
    
    # Step 5: Analyze and generate recommendations
    troubleshooter = NetworkTroubleshooter()
    
    # Check ping
    if not report['diagnostics']['ping']['success']:
        report['findings'].append({
            'severity': 'high',
            'issue': 'External connectivity failed',
            'test': 'ping'
        })
        report['recommendations'].append('Check internet gateway and routing')
    
    # Check DNS
    if not report['diagnostics']['dns']['success']:
        report['findings'].append({
            'severity': 'high',
            'issue': 'DNS resolution failed',
            'test': 'dns'
        })
        report['recommendations'].append('Verify DNS server configuration')
    
    # Check default gateway
    if not report['diagnostics']['default_gateway']['success']:
        report['findings'].append({
            'severity': 'critical',
            'issue': 'No default gateway or gateway unreachable',
            'test': 'default_gateway'
        })
        report['recommendations'].append('Configure or fix default gateway')
    
    # Determine overall status
    critical_count = len([f for f in report['findings'] if f['severity'] == 'critical'])
    high_count = len([f for f in report['findings'] if f['severity'] == 'high'])
    
    if critical_count > 0:
        report['status'] = 'critical'
    elif high_count > 0:
        report['status'] = 'degraded'
    elif len(report['findings']) > 0:
        report['status'] = 'warning'
    else:
        report['status'] = 'healthy'
    
    return report

# Example usage
# report = troubleshoot_vm_network(
#     vm_identifier='i-1234567890abcdef0',
#     cloud_provider='aws',
#     region='us-east-1',
#     target_host='8.8.8.8'
# )
# print(json.dumps(report, indent=2, default=str))
```

---

## Common Issues and Solutions

| Issue | Possible Causes | Recommended Actions |
|-------|-----------------|---------------------|
| Cannot ping external hosts | No internet gateway, routing issue, security group blocking ICMP | Check route tables, verify IGW attachment, check security groups |
| DNS resolution fails | Wrong nameservers, DNS server unreachable, firewall blocking UDP 53 | Check /etc/resolv.conf, test with public DNS, check firewall rules |
| SSH connection refused | SSH service not running, wrong port, firewall blocking | Check sshd status, verify port 22 is open, check security groups |
| High latency | Network congestion, suboptimal routing, resource constraints | Run traceroute, check for packet loss, review instance sizing |
| Intermittent connectivity | Unstable network interface, DHCP issues, MTU problems | Check interface status, verify DHCP lease, test with different MTU |
| Cannot reach other VMs in VPC | Security group rules, NACL rules, routing between subnets | Check SG rules allow internal traffic, verify route tables |

---

## Security Best Practices

1. **Never hardcode credentials** - Use environment variables or IAM roles
2. **Use least-privilege IAM policies** - Only request permissions needed for diagnostics
3. **Sanitize log output** - Remove sensitive IPs and keys before sharing
4. **Avoid modifying system state** - Diagnostic operations should be read-only
5. **Use secure connections** - Always use SSH keys instead of passwords when possible

---

## Dependencies

```
boto3>=1.26.0
azure-identity>=1.12.0
azure-mgmt-compute>=29.0.0
azure-mgmt-network>=25.0.0
google-cloud-compute>=1.14.0
dnspython>=2.3.0
paramiko>=3.0.0
```
