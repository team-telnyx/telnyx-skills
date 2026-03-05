<a href="https://www.telnyx.com">
  <img src="https://www.telnyx.com/logo-dark.svg" alt="Telnyx" width="250" />
</a>

# Airtng App: Part 2 - Workflow Automation with Telnyx Python | Flask

![](https://github.com/TwilioDevEd/airtng-masked-numbers-flask/workflows/Flask/badge.svg)

Protect your customers' privacy by creating a seamless interaction by provisioning Telnyx numbers on the fly. Route all voice calls and messages through your very own 3rd party. This allows you to control the interaction between your customers, while putting your customer's privacy first.

## Configure Telnyx to call your webhooks

You will need to configure Telnyx to send requests to your application when SMSs are received.

You will need to provision at least one Telnyx number with SMS capabilities so the application's users can make property reservations. You can buy a number [right here](https://portal.telnyx.com/#/app/numbers/search). Once you have a number you need to configure it to work with your application. Open [the number management page](https://portal.telnyx.com/#/app/numbers/my-numbers) and configure your number's webhook URLs.

Remember that the number where you change the _SMS webhook_ must be the same one you set on the `TELNYX_PHONE_NUMBER` setting.

[Learn how to configure a Telnyx phone number for Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice)

 To start using `ngrok` in our project you'll have execute to the following line in the _command prompt_.

```bash
ngrok http 5000 -host-header="localhost:5000"
```

Keep in mind that our endpoint is:

```
http://<your-ngrok-subdomain>.ngrok.io/reservations/confirm
```


## Create a TeXML App

This project is configured to use a _TeXML App_ that allows us to easily set the voice URLs for all Telnyx phone numbers we purchase in this app.

[Create a new TeXML app](https://portal.telnyx.com/#/app/call-control/connections?type=texml) and use its `Connection ID` as the `TELNYX_CONNECTION_ID` application setting.

[Learn more about creating a TeXML app here](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)

Once you have created your TeXML app, configure your Telnyx phone number to use it ([instructions here](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)).

If you don't have a Telnyx phone number yet, you can purchase a new number in your [Telnyx Account Dashboard](https://portal.telnyx.com/#/app/numbers/search).

You'll need to update your TeXML app's voice and SMS URL setting to use your `ngrok` hostname. It will look something like this:

```
http://<your-ngrok-subdomain>.ngrok.io/exchange/sms
http://<your-ngrok-subdomain>.ngrok.io/exchange/voice
```

## Local Development

1. Clone this repository and `cd` into it.

   ```bash
   git clone git@github.com:TwilioDevEd/airtng-flask.git
   ```

1. Create a new virtual environment.

   - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

       ```bash
       virtualenv venv
       source venv/bin/activate
       ```

   - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

       ```bash
       mkvirtualenv airtng-flask
       ```

1. Install the requirements.

   ```bash
   pip install -r requirements.txt
   ```

1. Edit the following keys/values for the `config.py` file inside the  `airtng_flask/` directory. Be sure to replace the place holders and connection strings with real information or reuse the provided one, like the connection string.

   ```
   TELNYX_API_KEY = 'your_telnyx_api_key'
   TELNYX_PUBLIC_KEY = 'your_telnyx_public_key'
   TELNYX_PHONE_NUMBER = 'your_telnyx_phone_number'
   TELNYX_MESSAGING_PROFILE_ID = 'your_messaging_profile_id'
   TELNYX_CONNECTION_ID = 'your_telnyx_connection_id'

   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
   ```

1. Run the migrations.

   ```bash
   python manage.py db upgrade
   ```

1. Start the development server.

   ```bash
   python manage.py runserver
   ```

1. Check it out at [http://localhost:5000](http://localhost:5000)


## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```bash
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
