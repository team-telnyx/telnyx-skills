<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# SMS Two-Factor Authentication

[![Build Status](https://travis-ci.org/TwilioDevEd/sms2fa-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/sms2fa-flask)

<!--
  You can grab the appropriate description from https://www.twilio.com/docs/tutorials.
-->
SMS Two-Factor Authentication (SMS-2FA) helps keep your user accounts secure by validating two "factors" of identity. Most login systems only validate a password known by the user. You can make it harder for evildoers to compromise a user account by also validating something a user has, such as their mobile phone.

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/sms2fa-flask.git
   $ cd sms2fa-flask
   ```

1. Create a new virtual environment.

    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```bash
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```bash
        mkvirtualenv automated-survey
        ```

1. Install the dependencies.

    ```bash
    pip install -r requirements.txt
    ```


1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/console).
   You will also need a `TWILIO_NUMBER`, which you may find [here](https://www.twilio.com/console/phone-numbers/incoming).

   Run `source .env` to export the environment variables.

1. Run the migrations.

    Our app uses SQLite, so you probably will not need to install additional software.

    ```bash
    python manage.py db upgrade
    ```

1. Make sure the tests succeed.

    ```bash
    $ coverage run manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```

1. Check it out at: [http://localhost:5000/](http://localhost:5000/).

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
