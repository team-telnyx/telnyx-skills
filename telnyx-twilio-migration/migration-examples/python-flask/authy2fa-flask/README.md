# Two-Factor Authentication with Telnyx Verify
This application example demonstrates how to implement Two-Factor Authentication on a Python Flask application using [Telnyx Verify](https://telnyx.com/products/verify) for SMS verification and [Authy](https://authy.com) for OneTouch push notifications.

[![Flask](https://github.com/TwilioDevEd/authy2fa-flask/workflows/Flask/badge.svg)](https://github.com/TwilioDevEd/authy2fa-flask)

[Learn more about Telnyx Verify in our documentation](https://developers.telnyx.com/docs/api/verify/).

## Quickstart

### Create accounts

1. Create a Telnyx account at [https://telnyx.com/sign-up](https://telnyx.com/sign-up) and generate an API key from the [portal](https://portal.telnyx.com/#/app/api-keys)

2. Create a Verify Profile in the [Telnyx Portal](https://portal.telnyx.com/#/app/verify-profiles) for SMS verification

3. (Optional) Create an Authy application at [https://dashboard.authy.com](https://dashboard.authy.com) if you want OneTouch push notifications

### Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework and the SQLite3 database.

1. To run the app locally, first clone this repository and `cd` into it.

1. Create and activate a new python3 virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

   ```bash
   pip install -r requirements.txt
   ```

1. Copy the `.env.example` file to `.env`, and edit it to include:
   - Your **Telnyx API Key** (from the Telnyx Portal)
   - Your **Telnyx Verify Profile ID** (from the Telnyx Portal)
   - (Optional) Your **Authy API Key** (if using OneTouch)

   ```bash
   cp .env.example .env
   ```

1. Create the Flask app specific environment variables

   ```bash
   export FLASK_APP=twofa
   export FLASK_ENV=development
   ```

1. Initialize the development database

   ```bash
   flask db upgrade
   ```

1. Start the development server.

   ```bash
   flask run
   ```

## Expose your app in the internet
To process OneTouch authentication requests (if using Authy), your development server will need to be publicly accessible. We recommend using ngrok:

```bash
ngrok http -bind-tls=false 5000
```

Once you have started ngrok, set your Authy app's OneTouch callback URL to use your ngrok hostname:

```
http://[your ngrok subdomain].ngrok.io/authy/callback
```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```bash
    python test.py
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Migration Notes

This app has been migrated from Twilio Authy to a hybrid deployment:
- **SMS verification**: Now uses Telnyx Verify API
- **OneTouch push**: Still uses Authy API (no Telnyx equivalent)

The migration used the [Telnyx Twilio Migration Skill](https://github.com/team-telnyx/telnyx-twilio-migration) - see `MIGRATION-PLAN.md` and `MIGRATION-REPORT.md` for details.

## Telnyx-Only Features

Now that you're on Telnyx, consider these capabilities:

- **Flash Calling**: Verification via missed call (no SMS charges)
- **PSD2 Compliance**: Built-in payment authorization support
- **Multiple TTS Engines**: Choose from Google, Deepgram, Azure, or Telnyx

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Originally crafted by Twilio Developer Education, migrated to Telnyx.
