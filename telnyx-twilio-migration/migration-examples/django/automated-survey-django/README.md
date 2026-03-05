# Automated surveys (Django)
[![Build Status](https://travis-ci.org/TwilioDevEd/automated-survey-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/automated-survey-django)

Use Twilio to conduct automated phone surveys.

[Read the full tutorial](https://www.twilio.com/docs/tutorials/walkthrough/automated-survey/python/django)!

## Quickstart

### Local development

This project is built using the [Django](https://www.djangoproject.com/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into it. Then:

1. Create a new virtual environment:

    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then `source venv/bin/activate`.
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv automated-surveys`.

1. Install the requirements with `pip install -r requirements.txt`.

1. Start a local PostgreSQL database and create a database called `surveys`.

    - If on a Mac, we recommend
      [Postgres.app](http://postgresapp.com/). After installing, run `createdb surveys;`.
    - If Postgres is already installed locally, you can just run `createdb surveys` from a terminal.

1. Copy the `.env.example` file to `.env`, and edit it to match your database.

1. Run the migrations with `python manage.py migrate`.

1. Optionally create a superuser so you can access the Django admin: `python manage.py createsuperuser`.

1. Start the development server: `python manage.py runserver`.

### Configure Twilio to call your webhooks

You will also need to configure Twilio to call your application when
calls are received. To be able to do this you would need to
to provision at least one Twilio number with voice
capabilities so the application's users can take surveys. You can buy
a number
[right here](https://www.twilio.com/user/account/phone-numbers/search). Once
you have a number you need to configure it to work with your
application. Open
[the number management page](https://www.twilio.com/user/account/phone-numbers/incoming)
and open a number's configuration by clicking on it. ![Open a number's configuration](https://raw.github.com/TwilioDevEd/automated-survey-django/master/images/number-conf.png)

Next, edit the "Request URL" field under the "Voice" section and point
it towards your ngrok-exposed application `/automated-survey/first-survey/` route. Set
the HTTP method to POST. If you are running the application
in production somewhere, you need to point Twilio to
`http://<your-app-name>.com/automated-survey/first-survey/`.

See the images below as an example on how to do it:

You can then visit the application at [http://localhost:8000/](http://localhost:8000/).

Mind the trailing slash.

![Webhook Voice configuration](https://raw.github.com/TwilioDevEd/automated-survey-django/master/images/webhook-conf-voice.png)

The same endpoint for Voice is being used for Messaging, so you can repeat this step on the Messaging section.
![Webhook SMS configuration](https://raw.github.com/TwilioDevEd/automated-survey-django/master/images/webhook-conf-sms.png)

## Run the tests

Configure your test database by editing `.env.test` file. You can then run the tests locally using `py.test`

```
$ py.test automated_survey/tests/ --cov=automated_survey
```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
