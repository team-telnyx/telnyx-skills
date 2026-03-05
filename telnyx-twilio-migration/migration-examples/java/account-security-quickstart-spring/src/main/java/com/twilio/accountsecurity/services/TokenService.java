package com.twilio.accountsecurity.services;

import com.authy.AuthyApiClient;
import com.authy.AuthyException;
import com.authy.OneTouchException;
import com.authy.api.*;
import com.twilio.accountsecurity.controllers.requests.VerifyTokenRequest;
import com.twilio.accountsecurity.repositories.UserRepository;
import com.twilio.accountsecurity.exceptions.TokenVerificationException;
import com.twilio.accountsecurity.models.UserModel;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TokenService {

    private static final Logger LOGGER = LoggerFactory.getLogger(TokenService.class);

    private AuthyApiClient authyClient;
    private UserRepository userRepository;

    @Autowired
    public TokenService(AuthyApiClient authyClient, UserRepository userRepository) {
        this.authyClient = authyClient;
        this.userRepository = userRepository;
    }


    public void sendSmsToken(String username) throws AuthyException {
        Hash hash = authyClient
                .getUsers()
                .requestSms(getUserAuthyId(username));

        if(!hash.isOk()) {
            logAndThrow("Problem sending token over SMS. " + hash.getMessage());
        }
    }

    public void sendVoiceToken(String username) throws AuthyException {
        UserModel user = userRepository.findFirstByUsername(username);

        Hash hash = authyClient.getUsers().requestCall(user.getAuthyId());
        if(!hash.isOk()) {
            logAndThrow("Problem sending the token on a call. " + hash.getMessage());
        }
    }

    public String sendOneTouchToken(String username) throws AuthyException {
        UserModel user = userRepository.findFirstByUsername(username);

        try {
            ApprovalRequestParams params = new ApprovalRequestParams
                    .Builder(user.getAuthyId(), "Login requested for Account Security account.")
                    .setSecondsToExpire(120L)
                    .addDetail("Authy ID", user.getAuthyId().toString())
                    .addDetail("Username", user.getUsername())
                    .addDetail("Location", "San Francisco, CA")
                    .addDetail("Reason", "Demo by Account Security")
                    .build();
            OneTouchResponse response = authyClient
                    .getOneTouch()
                    .sendApprovalRequest(params);

            if(!response.isSuccess()) {
                logAndThrow("Problem sending the token with OneTouch");
            }
            return response.getApprovalRequest().getUUID();
        } catch (OneTouchException e) {
            logAndThrow("Problem sending the token with OneTouch: " + e.getMessage());
        }
        return null;
    }

    public void verify(String username, VerifyTokenRequest requestBody) throws AuthyException {
        Token token = authyClient
                .getTokens()
                .verify(getUserAuthyId(username), requestBody.getToken());

        if(!token.isOk()) {
            logAndThrow("Token verification failed. " + token.getError().toString());
        }
    }

    public boolean retrieveOneTouchStatus(String uuid) {
        try {
            return authyClient
                    .getOneTouch()
                    .getApprovalRequestStatus(uuid)
                    .getApprovalRequest()
                    .getStatus()
                    .equals("approved");
        } catch (OneTouchException e) {
            logAndThrow(e.getMessage());
        }
        return false;
    }

    private void logAndThrow(String message) {
        LOGGER.warn(message);
        throw new TokenVerificationException(message);
    }

    private Integer getUserAuthyId(String username) {
        UserModel user = userRepository.findFirstByUsername(username);
        return user.getAuthyId();
    }
}
