import os

'''
Configuration Settings
'''

TELNYX_API_KEY = os.environ.get('TELNYX_API_KEY', None)
TELNYX_CALLER_ID = os.environ.get('TELNYX_CALLER_ID', None)
TELNYX_CONNECTION_ID = os.environ.get('TELNYX_CONNECTION_ID', None)
# For Call Control Applications (v2 API)
TELNYX_APPLICATION_ID = os.environ.get('TELNYX_APPLICATION_ID', None)
