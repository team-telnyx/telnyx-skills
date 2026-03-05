package com.twilio.accountsecurity.controllers.requests;

import jakarta.validation.constraints.NotNull;

public class PhoneVerificationVerifyRequest {
    @NotNull
    private String phoneNumber;
    @NotNull
    private String token;

    public PhoneVerificationVerifyRequest() {
    }

    public PhoneVerificationVerifyRequest(String phoneNumber, String token) {
        this.phoneNumber = phoneNumber;
        this.token = token;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
