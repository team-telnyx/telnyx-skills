<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# IVR Phone Tree: IVR for beginners. Powered by Twilio - Node.js/Express

[![Node.js CI](https://github.com/TwilioDevEd/ivr-phone-tree-node/actions/workflows/node.js.yml/badge.svg)](https://github.com/TwilioDevEd/ivr-phone-tree-node/actions/workflows/node.js.yml)

Create a seamless customer service experience by building an IVR Phone Tree for your company. IVR systems allow your customers to access the people and information they need.

[Read the full tutorial here!](https://www.twilio.com/docs/tutorials/walkthrough/ivr-phone-tree/node/express)

## Local Development

This project is build using [Express](http://expressjs.com/) web framework and
depends on [MongoDB](https://www.mongodb.com).


1. First clone this repository and `cd` into it.

   ```bash
   git clone git@github.com:TwilioDevEd/ivr-phone-tree-node.git \
   cd ivr-phone-tree-node
   ```
1. Install project's dependencies.

   ```bash
   npm install
   ```

1. Make sure the tests succeed.

   ```bash
   npm test
   ```

1. Start the development server.

   ```bash
   npm start
   ```

   Alternatively you might also consider using [nodemon](https://github.com/remy/nodemon) for this. It works just like
   the node command, but automatically restarts your application when you change any source code files.

   ```bash
   npm install -g nodemon \
   nodemon .
   ```

1. Check it out at [http://localhost:3000](http://localhost:3000).

1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/).

   ```bash
   ngrok http 3000
   ```

1. Provision a number under the [Twilio's Manage Numbers](https://www.twilio.com/console/phone-numbers/incoming)
   page on your account. Set the voice URL for the number to http://[your-ngrok-subdomain].ngrok.io/ivr/welcome

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
