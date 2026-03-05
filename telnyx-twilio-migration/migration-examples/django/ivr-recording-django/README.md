<a href="https://www.telnyx.com">
  <img src="https://www.telnyx.com/img/nav-logo-colored.svg" alt="Telnyx" width="250" />
</a>

# IVR Call Recording and Agent Conference (Migrated to Telnyx)

IVRs (interactive voice response) are automated phone systems that can facilitate communication between callers and businesses. In this tutorial you will learn how to screen and send callers to voicemail if an agent is busy.

**This project has been migrated from Twilio to Telnyx using TeXML.**

[Read the full Telnyx Voice API documentation here](https://developers.telnyx.com/docs/v2/voice?protocol=texml)

## Migration Notes

This Django application has been migrated from Twilio TwiML to Telnyx TeXML:

- **TeXML** is Telnyx's TwiML-compatible markup language for voice applications
- XML structure is nearly identical - the same `<Response>`, `<Say>`, `<Gather>`, `<Dial>`, `<Record>` verbs work
- Voice builder classes are replaced with XML element tree generation
- Authentication is via Bearer Token (`TELNYX_API_KEY`) instead of Account SID + Auth Token

## Changes from Original

1. **views.py**: 
   - Replaced Twilio VoiceResponse class with Python's xml.etree.ElementTree
   - Changed class name to TeXMLResponse
   - Updated Polly voice references to use Neural variants (`Polly.Amy-Neural`)
   - Added `channels="single"` to `<Record>` to match Twilio behavior

2. **requirements.txt**: Added `telnyx>=2.0,<3.0`

3. **Environment Variables**:
   - `TELNYX_API_KEY` - Your Telnyx API Key v2
   - `TELNYX_PHONE_NUMBER` - Your Telnyx phone number
   - `TELNYX_CONNECTION_ID` - Your TeXML Application connection ID

## Local Development

1. Clone this repository and `cd` into its directory:

   ```bash
   git clone git@github.com:TelnyxDevEd/ivr-recording-django.git
   cd ivr-recording-django
   ```

1. The file `ivr/fixtures/agents.json` contains the agents phone numbers. Replace any of these phone numbers with yours.

    When the application asks you to select an agent, choose the one you just modified and it will then call your phone.

1. Create a local virtual environment and activate it:

   ```bash
   python -m venv venv && source venv/bin/activate
   ```

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Set environment variables:

   ```bash
   cp .env.example .env
   ```
   Then add values to:
   - `SECRET_KEY` - Django secret key
   - `TELNYX_API_KEY` - Your Telnyx API Key from https://portal.telnyx.com/#/app/api-keys
   - `TELNYX_PHONE_NUMBER` - Your Telnyx phone number in E.164 format
   - `TELNYX_CONNECTION_ID` - Your TeXML Application connection ID

   Note: `DEBUG` variable is False by default. Feel free to update it to True if needed.

1. Set up database and run migrations:

   ```bash
   python manage.py migrate
   ```

1. Load initial agents' data:

   ```bash
   python manage.py loaddata ivr/fixtures/agents.json
   ```

1. Make sure the tests succeed:

    ```bash
    python manage.py test
    ```

1. Run the application:

    ```bash
    python manage.py runserver
    ```

1. Check it out at [http://localhost:8000/ivr](http://localhost:8000/ivr).
   You can go to the [agents page](http://localhost:8000/ivr/agents) to see and listen the saved recordings.

1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/)
   To let our Telnyx Phone number use the callback endpoint we exposed, our development server will need to be publicly accessible.

   ```bash
   ngrok http 8000
   ```

1. Set up your TeXML Application in the Telnyx Mission Control Portal:
   - Navigate to **Voice** → **TeXML Applications**
   - Create a new TeXML Application
   - Set the Voice URL to `https://<your-ngrok-domain>/ivr/welcome`
   - Set the Voice Method to `POST`

## Telnyx Resources

- [Telnyx Voice API Documentation](https://developers.telnyx.com/docs/v2/voice?protocol=texml)
- [TeXML Verbs Reference](https://developers.telnyx.com/docs/v2/voice/texml/texml-overview)
- [Telnyx Python SDK](https://github.com/team-telnyx/telnyx-python)

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Built on Telnyx Voice API
