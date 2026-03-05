<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>
 
# Airtng App: Part 2 - Anonymous Calling and SMS with Twilio

![](https://github.com/TwilioDevEd/anonymous-communications-rails/actions/workflows/build.yml/badge.svg)

Protect your customers' privacy, and create a seamless interaction by provisioning Twilio numbers on the fly, and routing all voice calls, and messages through your very own 3rd party. This allows you to control the interaction between your customers, while putting your customer's privacy first.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/masked-numbers/ruby/rails)!

## Local Development

This project is built using [Ruby on Rails](http://rubyonrails.org/) Framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/anonymous-communications-rails.git
   $ cd anonymous-communications-rails
   ```

1. Install the dependencies.

   ```bash
   $ bundle install
   ```

1. Expose your application to the wider internet using [ngrok](http://ngrok.com). This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   $ ngrok http 3000
   ```

   Your ngrok URL should look something like this: `http://9a159ccf.ngrok.io`

   You can read [this blog post](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
   for more details on how to use ngrok.

1. Configure Twilio App to call your webhooks.

   Before you can run this app you need to go into your account portal and [create a new Twilio Application](https://www.twilio.com/console/phone-numbers/runtime/twiml-apps). Once you have created an app the urls should look like:

   Voice: `https://<ngrok_subdomain>.ngrok.io/reservations/connect_voice`

   SMS & MMS: `https://<ngrok_subdomain>.ngrok.io/reservations/connect_sms`

1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/console/account/settings).
   You will also need a `TWILIO_NUMBER`, which you may find [here](https://www.twilio.com/console/phone-numbers/incoming).

1. Create database and run migrations. Be sure to have [SQLite](https://www.sqlite.org/index.html) installed before running this command.

   ```bash
   $ bundle exec rails db:setup
   ```

1. Make sure the tests succeed.

   ```bash
   $ bundle exec rspec
   ```

1. Start the server.

   ```bash
   $ bundle exec rails s
   ```

That's it!

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.
