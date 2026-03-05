// Hardcoded config to bypass environment variable issues
// This connection ID is for "Aisling WebRTC Webapp" credential connection
module.exports = {
  telnyxApiKey: process.env.TELNYX_API_KEY,
  telnyxPhoneNumber: process.env.TELNYX_PHONE_NUMBER || '+353857688030',
  telnyxConnectionId: '2695736746993256422',
  port: process.env.PORT || 3000,
};