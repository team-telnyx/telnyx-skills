package com.twilio.accountsecurity.services;

import org.springframework.stereotype.Service;

@Service
public class Settings {

    public String getAuthyId(){
        return System.getenv("ACCOUNT_SECURITY_API_KEY");
    }

    public String getAccountSid() {
        return System.getenv("TWILIO_ACCOUNT_SID");
    }

    public String getAuthToken() {
        return System.getenv("TWILIO_AUTH_TOKEN");
    }

    public String getVerificationSid() {
        return System.getenv("TWILIO_VERIFICATION_SID");
    }

    // Telnyx configuration for Verify API
    public String getTelnyxApiKey() {
        return System.getenv("TELNYX_API_KEY");
    }

    public String getTelnyxVerifyProfileId() {
        return System.getenv("TELNYX_VERIFY_PROFILE_ID");
    }
}
