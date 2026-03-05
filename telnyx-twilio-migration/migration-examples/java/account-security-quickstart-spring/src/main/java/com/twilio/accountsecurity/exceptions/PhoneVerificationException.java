package com.twilio.accountsecurity.exceptions;

public class PhoneVerificationException extends RuntimeException{
    public PhoneVerificationException(String message) {
        super(message);
    }
}
