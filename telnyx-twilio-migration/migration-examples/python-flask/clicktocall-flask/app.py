import sys
sys.path.insert(0, '/home/telnyx-user/twilio-test-repos/clicktocall-flask')

import os

from dotenv import load_dotenv
load_dotenv()

from clicktocall.app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)
