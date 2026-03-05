package com.twilio.accountsecurity.controllers;

import com.twilio.accountsecurity.controllers.requests.LoginRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.logout.SecurityContextLogoutHandler;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import java.io.IOException;

@RestController
@RequestMapping(value = "/api")
public class LoginController {

    @RequestMapping(path = "/login", method = RequestMethod.POST)
    public ResponseEntity login(@Valid @RequestBody LoginRequest loginRequest,
                                HttpServletRequest request, HttpServletResponse response) {
        try {
            request.login(loginRequest.getUsername(), loginRequest.getPassword());
            response.sendRedirect(request.getContextPath() + "/2fa/index.html");
            return ResponseEntity.ok().build();
        } catch (ServletException | IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(e.getMessage());
        }
    }

    @RequestMapping(path = "/logout", method = RequestMethod.GET)
    public ResponseEntity logout(HttpServletRequest request, HttpServletResponse response) {
        try {
            Authentication auth = SecurityContextHolder.getContext().getAuthentication();
            if (auth != null){
                new SecurityContextLogoutHandler().logout(request, response, auth);
            }
            response.sendRedirect(request.getContextPath() + "/index.html");
            return ResponseEntity.ok().build();
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(e.getMessage());
        }
    }
}
