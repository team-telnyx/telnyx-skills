package com.twilio.accountsecurity.controllers;

import com.twilio.accountsecurity.controllers.requests.VerifyTokenRequest;
import com.twilio.accountsecurity.exceptions.TokenVerificationException;
import com.twilio.accountsecurity.services.TokenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@RestController
@RequestMapping(value = "/api/token")
public class TokenController implements BaseController {

    private TokenService tokenService;

    @Autowired
    public TokenController(TokenService tokenService) {
        this.tokenService = tokenService;
    }

    @RequestMapping(value = "sms", method = RequestMethod.POST)
    public ResponseEntity<?> sms(HttpServletRequest request) {
        return runWithCatch(() ->
                tokenService.sendSmsToken(request.getUserPrincipal().getName()));
    }

    @RequestMapping(value = "voice", method = RequestMethod.POST)
    public ResponseEntity<?> voice(HttpServletRequest request) {
        return runWithCatch(() ->
                tokenService.sendVoiceToken(request.getUserPrincipal().getName()));
    }

    @RequestMapping(value = "onetouch", method = RequestMethod.POST)
    public ResponseEntity<?> oneTouch(HttpServletRequest request) {
        return runWithCatch(() -> {
            String uuid = tokenService.sendOneTouchToken(request.getUserPrincipal()
                    .getName());
            request.getSession().setAttribute("onetouchUUID", uuid);
        });
    }

    @RequestMapping(value = "onetouchstatus", method = RequestMethod.POST,
            produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> oneTouchStatus(HttpServletRequest request) {
        try {
            HttpSession session = request.getSession();
            boolean status = tokenService.retrieveOneTouchStatus(
                    (String) session.getAttribute("onetouchUUID"));
            session.setAttribute("authy", status);
            return ResponseEntity.ok(status);
        } catch (TokenVerificationException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(e.getMessage());
        }
    }

    @RequestMapping(value = "verify", method = RequestMethod.POST,
            consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> verify(@Valid @RequestBody VerifyTokenRequest requestBody,
                                 HttpServletRequest request) {
        return runWithCatch(() -> {
            tokenService.verify(request.getUserPrincipal().getName(), requestBody);
            request.getSession().setAttribute("authy", true);
        }, HttpStatus.BAD_REQUEST);
    }
}
