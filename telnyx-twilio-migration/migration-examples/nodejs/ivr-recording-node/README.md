<a href="https://www.telnyx.com">
  <img src="https://www.telnyx.com/images/logo.svg" alt="Telnyx" width="250" />
</a>

# IVR Call Recording and Agent Conference (Migrated to Telnyx).

IVRs (interactive voice response) are automated phone systems that can facilitate communication between callers and businesses. In this tutorial you will learn how to screen and send callers to voicemail if an agent is busy.

This is a migrated version of the original Twilio sample application, now using Telnyx TeXML.

[Read the original Twilio tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/ivr-screening/node/express)!

## Local Development

1. This sample application stores data in a [MongoDB](https://www.mongodb.org/) database using [Mongoose](http://mongoosejs.com/). You can download and run MongoDB yourself (OS X, Linux, Windows).

   On OS X, maybe the easiest way to get MongoDB running locally is to install via [Homebrew](http://brew.sh/):

   ```bash
   brew tap mongodb/brew
   brew install mongodb-community
   ```

   You should then be able to run a local server with:

   ```bash
   brew services start mongodb-community
   ```

1. Clone this repository and `cd` into its directory:

   ```bash
   git clone git@github.com:TelnyxDevEd/ivr-recording-node.git
   cd ivr-recording-node
   ```

1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TELNYX_API_KEY` at https://portal.telnyx.com/#/app/api-keys.
   You will also need a `TELNYX_PHONE_NUMBER` and `TELNYX_CONNECTION_ID` (TeXML Application ID).

1. The file `seed/agents.js` contains the agents phone numbers. Replace any of these phone numbers with yours. Then seed the initial data into the database by running the following:

   ```bash
   mongo localhost/call-screening seed/agents.js
   ```
    When the application asks you to select an agent, choose the one you just modified and it will then call your phone.

1. Install dependencies:

   ```bash
   npm install
   ```

1. Make sure the tests succeed:

    ```bash
    npm test
    ```

1. Run the application:

    ```bash
    npm start
    ```

1. Check it out at [http://localhost:3000](http://localhost:3000)

1. Expose the application to the wider Internet using [ngrok](https://ngrok.com/)
   To let our Telnyx Phone number use the callback endpoint we exposed, our development server will need to be publicly accessible. [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).

   ```bash
   ngrok http 3000
   ```

1. Provision a number under the [Manage Numbers page](https://portal.telnyx.com/#/app/numbers/my-numbers) on your account. Set the voice webhook for the number to `http://<your-ngrok-subdomain>.ngrok.io/ivr/welcome`.

That's it!

## Migration Notes

This application was migrated from Twilio to Telnyx:
- Twilio SDK (`twilio`) → Telnyx SDK (`telnyx`)
- Twilio `VoiceResponse` → Telnyx `TeXML.VoiceResponse`
- Voice attribute `voice: 'Polly.Amy'` → `voice: 'Polly.Amy-Neural'`
- Added `channels: 'single'` to `<Record>` for mono recording

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education, migrated to Telnyx.
