<a href="https://telnyx.com">
  <img src="https://uploads-ssl.webflow.com/5e1f85a748254f375b15d297/5e3a0f6b1c7a1b2e4a9d7c36_Telnyx-Logo-RGB-Black.svg" alt="Telnyx" width="250" />
</a>

# Click to Call with Flask

> This repository has been migrated from Twilio to Telnyx.

## Set up

### Requirements

- [Python](https://www.python.org/) **3.6**, **3.7** or **3.8** version.

In some environments when both version 2
and 3 are installed, you may substitute the Python executables below with
`python3` and `pip3` unless you use a version manager such as
[pyenv](https://github.com/pyenv/pyenv).

### Telnyx Account Settings

This application should give you a ready-made starting point for writing your own application.
Before we begin, we need to collect all the config values we need to run the application:

| Config Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TELNYX_API_KEY  | Your Telnyx API Key (v2) - find this [in the Portal](https://portal.telnyx.com/#/app/api-keys). |
| TELNYX_CALLER_ID | A Telnyx phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://portal.telnyx.com/#/app/numbers) |
| TELNYX_CONNECTION_ID | Your TeXML Application Connection ID - create one [here](https://portal.telnyx.com/#/app/voice/texml) |

### Local development

1. First clone this repository and `cd` into it.

   ```bash
   git clone https://github.com/TwilioDevEd/clicktocall-flask.git
   cd clicktocall-flask
   ```

2. Create the virtual environment, load it and install the dependencies.

    ```bash
    make install
    ```

3. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   See [Telnyx Account Settings](#telnyx-account-settings) to locate the necessary environment variables.

4. Start the development server, it will run on port 5000. Before running the following command, make sure the virtual environment is activated.

   ```bash
   make serve
   ```

5. Expose your application to the wider internet using ngrok. You can click
   [here](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html) for more details. This step
   is important because the application won't work as expected if you run it through localhost.

   ```bash
   ngrok http 5000
   ```

6. Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

### Docker

If you have [Docker](https://www.docker.com/) already installed on your machine, you can use our `docker-compose.yml` to setup your project.

1. Make sure you have the project cloned.
2. Setup the `.env` file as outlined in the [Local Development](#local-development) steps.
3. Run `docker-compose up`.
4. Follow the steps in [Local Development](#local-development) on how to expose your port to Telnyx using a tool like [ngrok](https://ngrok.com/) and configure the remaining parts of your application.


### Tests

To execute tests, run the following command in the project directory. Before running the following command, make sure the virtual environment is activated.

```bash
make test
```

### Migration Notes

This application was migrated from Twilio to Telnyx. Key changes:

- **Twilio SDK** (`twilio`) → **Telnyx SDK** (`telnyx>=2.0,<3.0`)
- **TwiML** (`twilio.twiml.VoiceResponse`) → **Raw TeXML** (TwiML-compatible XML)
- **Basic Auth** (Account SID + Auth Token) → **Bearer Token** (TELNYX_API_KEY)
- **Environment Variables**: `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_CALLER_ID` → `TELNYX_API_KEY`, `TELNYX_CALLER_ID`, `TELNYX_CONNECTION_ID`

The TeXML format is compatible with TwiML, so the XML structure remains largely the same.

## Resources

- Telnyx Voice Documentation: https://developers.telnyx.com/docs/voice
- TeXML Reference: https://developers.telnyx.com/docs/voice/texml
- Telnyx Python SDK: https://github.com/team-telnyx/telnyx-python

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[telnyx]: https://telnyx.com
