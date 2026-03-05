package com.twilio.accountsecurity.controllers;

import com.twilio.accountsecurity.controllers.requests.PhoneVerificationStartRequest;
import com.twilio.accountsecurity.controllers.requests.PhoneVerificationVerifyRequest;
import com.twilio.accountsecurity.services.PhoneVerificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@RestController
@RequestMapping(path = "/api/phone-verification")
public class PhoneVerificationController implements BaseController {

    private PhoneVerificationService phoneVerificationService;

    @Autowired
    public PhoneVerificationController(PhoneVerificationService phoneVerificationService) {
        this.phoneVerificationService = phoneVerificationService;
    }

    @RequestMapping(path = "start", method = RequestMethod.POST,
            consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> start(@Valid @RequestBody PhoneVerificationStartRequest requestBody) {
        return runWithCatch(() -> {
            phoneVerificationService.start(
                    requestBody.getPhoneNumber(),
                    requestBody.getVia());
        });
    }

    @RequestMapping(path = "verify", method = RequestMethod.POST)
    public ResponseEntity<?> verify(@Valid @RequestBody PhoneVerificationVerifyRequest requestBody,
                                 HttpSession session) {
        return runWithCatch(() -> {
            phoneVerificationService.verify(
                    requestBody.getPhoneNumber(),
                    requestBody.getToken());
            session.setAttribute("ph_verified", true);
        });
    }
}

