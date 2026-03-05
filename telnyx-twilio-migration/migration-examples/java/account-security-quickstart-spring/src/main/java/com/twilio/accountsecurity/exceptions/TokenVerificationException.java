package com.twilio.accountsecurity.exceptions;

public class TokenVerificationException extends RuntimeException {
    public TokenVerificationException(String message) {
        super(message);
    }
}
