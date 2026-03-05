package com.twilio.accountsecurity.controllers;

import com.authy.AuthyException;
import com.twilio.accountsecurity.controllers.requests.UserRegisterRequest;
import com.twilio.accountsecurity.exceptions.UserExistsException;
import com.twilio.accountsecurity.services.RegisterService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;

@RestController
public class RegisterController {

    private static final Logger LOGGER = LoggerFactory.getLogger(RegisterController.class);

    private RegisterService registerService;

    @Autowired
    public RegisterController(RegisterService registerService) {
        this.registerService = registerService;
    }

    @RequestMapping(value = "/api/register",
            method = {RequestMethod.GET, RequestMethod.POST},
            consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> register(@Valid @RequestBody UserRegisterRequest newUserRequest,
                                      HttpServletRequest request) {
        try {
            registerService.register(newUserRequest);
            request.login(newUserRequest.getUsername(), newUserRequest.getPassword());
            return ResponseEntity.ok().build();
        } catch (UserExistsException e) {
            return ResponseEntity.status(HttpStatus.PRECONDITION_FAILED)
                    .body("User already exists");
        } catch (AuthyException | ServletException e) {
            LOGGER.error("Register Error: " + e.getMessage());
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(e.getMessage());
        }
    }
}
