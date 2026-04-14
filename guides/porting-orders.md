# Porting Phone Numbers

Learn how to port phone numbers into Telnyx using the Telnyx Agent.

## Checking Portability

Before creating a porting order, check if numbers are portable:

```typescript
const result = await tool("porting.check_portability", {
  phone_numbers: ["+13125550001", "+13125550002"]
});
```

Returns whether each number is portable and the reason if not.

## Creating a Porting Order

Create a porting order with the numbers you want to port:

```typescript
const order = await tool("porting.create_porting_order", {
  phone_numbers: ["+13125550001", "+13125550002"],
  customer_name: "Acme Corp",
  authorized_person: "John Doe",
  billing_phone_number: "+13125550000",
  old_service_provider: "AT&T"
});
```

## Checking Requirements

After creating an order, check what documents or information are needed:

```typescript
const requirements = await tool("porting.list_porting_requirements", {
  id: order.id
});
```

Requirements vary by number type and country. Common requirements:
- Letter of Authorization (LOA)
- Current invoice
- CSR (Customer Service Record)

## Submitting the Order

Once requirements are met, submit the order:

```typescript
const submitted = await tool("porting.submit_porting_order", {
  id: order.id
});
```

## Monitoring Status

Track the order status:

```typescript
const updated = await tool("porting.get_porting_order", {
  id: order.id
});
console.log(updated.status);
```

Statuses: `draft`, `submitted`, `in-process`, `exception`, `ported`, `cancelled`

## Handling Exceptions

If an order hits an exception, list the issues:

```typescript
const exceptions = await tool("porting.list_porting_exception_types", {});
```

Common exception types:
- `ACCOUNT_NUMBER_MISMATCH` - Billing account number doesn't match
- `POSTAL_CODE_MISMATCH` - Address postal code doesn't match
- `PHONE_NUMBER_MISMATCH` - Number not found on current account

## Activating Numbers (US FastPort)

For US numbers, you can schedule activation:

```typescript
await tool("porting.activate_porting_order", {
  id: order.id
});
```

## Listing Your Orders

```typescript
const orders = await tool("porting.list_porting_orders", {
  page_size: 20
});
```

## Port-Out (Moving Numbers Away)

To move numbers from Telnyx to another provider:

```typescript
// List port-out orders
const portouts = await tool("portout.list_portout_orders", {});

// Get specific port-out details
const detail = await tool("portout.get_portout_order", {
  id: "portout-order-id"
});
```

## Adding Comments

```typescript
await tool("porting.create_porting_comment", {
  id: order.id,
  body: "Customer confirmed LOA document uploaded"
});
```