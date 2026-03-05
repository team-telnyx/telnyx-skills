# Appointment Reminders (Django)

[![Actions Status](https://github.com/TwilioDevEd/appointment-reminders-django/workflows/Django%20CI/badge.svg)](https://github.com/TwilioDevEd/appointment-reminders-django/actions)

## About

Use Telnyx to create automatic appointment reminders for your business's clients.

Implementations in other languages:

| .NET | Java | Ruby | PHP | NodeJS |
| :--- | :--- | :--- | :-- | :----- |
| [Done](https://github.com/TwilioDevEd/appointment-reminders-csharp) | [Done](https://github.com/TwilioDevEd/appointment-reminders-java) | [Done](https://github.com/TwilioDevEd/appointment-reminders-rails) | [Done](https://github.com/TwilioDevEd/appointment-reminders-laravel) | [Done](https://github.com/twilio-labs/sample-appointment-reminders-node) |

## Set up

### Requirements

- [Python](https://www.python.org/downloads) version >= **3.6.x**.
- [ChromeDriver](https://chromedriver.chromium.org/) for the `Selenium` tests. Ensure the `chromedriver` executable is on the OS `path`. For Linux/Mac the easiest way to do this is to install it through the OS package manager:
  - Mac:
    ```bash
    brew install --cask chromedriver
    ```
  - Ubuntu:
    ```bash
    sudo apt-get install chromium-chromedriver
    sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
    ```
- [Redis](http://redis.io/) as its task queue.
- A Telnyx account - [sign up](https://telnyx.com/sign-up)

### Telnyx Account Settings

This application should give you a ready-made starting point for writing your
own appointment reminder application. Before we begin, we need to collect
all the config values we need to run the application:

| Config Value | Description |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TELNYX_API_KEY | Your Telnyx API Key - find this [in the Portal](https://portal.telnyx.com/#/app/api-keys). |
| TELNYX_PHONE_NUMBER | A Telnyx phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://portal.telnyx.com/#/app/numbers) |
| TELNYX_MESSAGING_PROFILE_ID | Your Telnyx Messaging Profile ID - you can [create one here](https://portal.telnyx.com/#/app/messaging) |

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it.

   ```bash
   git clone https://github.com/TwilioDevEd/appointment-reminders-django.git
   cd appointment-reminders-django
   ```

2. Create a virtual environment, activate it and install dependencies.

   ```bash
   make install
   ```

3. Set your environment variables.

   ```bash
   cp .env.example .env
   ```

   See [Telnyx Account Settings](#telnyx-account-settings) to locate the necessary environment variables.

4. Run migrations.
   ```bash
   make serve-setup
   ```

5. Configure pre-commit hooks.

   ```bash
   pre-commit install
   ```

6. Run the application.

   ```bash
   make serve
   ```

   This will start a development server on port `8000`. It will reload whenever you change any files.

This project uses [Dramatiq](https://dramatiq.io) to asynchronously send SMS reminders to users. To start the Dramatiq process:

7. Start [Redis](http://redis.io/).
8. Start a new terminal session and activate your virtual environment.
9. Open a new terminal session and start Dramatiq worker with the command:
   ```bash
   make start-dramatiq
   ```

10. Navigate to [http://localhost:8000/](http://localhost:8000/).

That's it!

### Docker

If you have [Docker](https://www.docker.com/) already installed on your machine, you can use our `docker-compose.yml` to setup your project.

1. Make sure you have the project cloned.
2. Setup the `.env` file as outlined in the [Local Development](#local-development) steps.
3. Run `docker-compose up`.


### Tests

**NOTE:** Be sure you have Google Chrome installed with the same version as the `chromedriver` installed earlier. Usually it's the latest version. 

You can run the tests locally by typing:

```bash
python3 manage.py test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/sample-template-django/tree/master) |

**Some notes:**

- For Heroku, please [check this](https://devcenter.heroku.com/articles/django-app-configuration) to properly configure the project for deployment.

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                                                                           |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                                                                                                                       |

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

[Visit the project on GitHub](https://github.com/twilio-labs/sample-template-nodejs)

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.
