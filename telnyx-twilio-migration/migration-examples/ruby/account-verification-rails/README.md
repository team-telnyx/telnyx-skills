# Account Verification Rails

## About

Verify new user accounts by sending them a one-time code via Telnyx Verify API. Reduce
fraudulent signups in your applications and ensure your users are in fact
living, breathing human beings.

## Local development

This project is built using [Ruby on Rails](http://rubyonrails.org/) and [NodeJS](https://nodejs.org/en/) Frameworks.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git://github.com/TwilioDevEd/account-verification-rails.git
   $ cd account-verification-rails
   ```

1. Install Rails the dependencies.
   ```
   $ bundle install
   ```

1. Install Webpack the dependencies.
   ```
   $ npm install
   ```

1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TELNYX_API_KEY` in your
   [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/api-keys).
   You will also need a `TELNYX_PHONE_NUMBER` (a phone number purchased or ported to your Telnyx account).

1. Create database and run migrations.

   _Make sure you have installed [PostgreSQL](http://www.postgresql.org/). If on a Mac, I recommend [Postgres.app](http://postgresapp.com)_. 
   
   This project uses SQLite by default for testing.

   ```bash
   $ bundle exec rails db:setup
   ```

1. Make sure the tests succeed.

   ```bash
   $ bundle exec rails test
   ```

1. Start the server.

   ```bash
   $ bundle exec rails s
   ```

1. Check it out at [http://localhost:3000](http://localhost:3000)

## Migration Notes

This application has been migrated from Twilio/Authy to Telnyx:

- **Verification**: Now uses Telnyx Verify API instead of Authy
- **Messaging**: Success confirmation SMS uses Telnyx Messaging API
- **Authentication**: Uses Telnyx API Key (Bearer token) instead of Twilio Account SID/Auth Token

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Migrated to Telnyx by Telnyx Migration Skill.
