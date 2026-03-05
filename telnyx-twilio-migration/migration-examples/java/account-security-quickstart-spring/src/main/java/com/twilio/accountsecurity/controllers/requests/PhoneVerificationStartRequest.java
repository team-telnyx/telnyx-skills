package com.twilio.accountsecurity.controllers.requests;

import jakarta.validation.constraints.NotNull;

public class PhoneVerificationStartRequest {

    @NotNull
    private String phoneNumber;
    @NotNull
    private String via;

    public PhoneVerificationStartRequest() {
    }

    public PhoneVerificationStartRequest(String phoneNumber, String via) {
        this.phoneNumber = phoneNumber;
        this.via = via;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getVia() {
        return via;
    }

    public void setVia(String via) {
        this.via = via;
    }
}
