<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# IVR Phone Tree: IVR for beginners. Powered by Twilio - Python/Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/ivr-phone-tree-python.svg?branch=master)](https://travis-ci.org/TwilioDevEd/ivr-phone-tree-python)

This is an application example implementing an automated phone line using
Python 2.7 and [Flask](http://flask.pocoo.org/) web framework.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/ivr-phone-tree/python/flask)!

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/ivr-phone-tree-python.git
   $ cd ivr-phone-tree-python
   ```

1. Create a new virtual environment.

    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```bash
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```bash
        mkvirtualenv ivr-phone-tree-python
        ```

1. Install the dependencies.

    ```bash
    pip install -r requirements.txt
    ```

1. Make sure the tests succeed.

    ```bash
    $ coverage run manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```

1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/).

    ```bash
    ngrok http 5000 -host-header="localhost:5000"
    ```

1. Configure Twilio to call your webhooks

  You will also need to configure Twilio to call your application when calls are
  received in your [*Twilio Number*](https://www.twilio.com/user/account/messaging/phone-numbers).
  The voice url should look something like this:

  ```
  http://<your-ngrok-subdomain>.ngrok.io/ivr/welcome
  ```

  ![Configure Voice](http://howtodocs.s3.amazonaws.com/twilio-number-config-all-med.gif)


## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
