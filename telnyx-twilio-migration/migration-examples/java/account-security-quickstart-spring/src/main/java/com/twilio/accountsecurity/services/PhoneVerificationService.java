package com.twilio.accountsecurity.services;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.twilio.accountsecurity.exceptions.TokenVerificationException;

@Service
public class PhoneVerificationService {

    private static final Logger LOGGER = LoggerFactory.getLogger(PhoneVerificationService.class);
    private static final String TELNYX_API_BASE = "https://api.telnyx.com/v2";

    private final Settings settings;
    private final RestTemplate restTemplate;
    private final ObjectMapper objectMapper;

    @Autowired
    public PhoneVerificationService(Settings settings) {
        this.settings = settings;
        this.restTemplate = new RestTemplate();
        this.objectMapper = new ObjectMapper();
    }

    public void start(String phoneNumber, String via) {
        String url = TELNYX_API_BASE + "/verifications/" + ("call".equals(via) ? "call" : "sms");
        
        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + settings.getTelnyxApiKey());
        headers.set("Content-Type", "application/json");

        String requestBody = String.format(
            "{\"phone_number\":\"%s\",\"verify_profile_id\":\"%s\"}",
            phoneNumber, settings.getTelnyxVerifyProfileId()
        );

        HttpEntity<String> request = new HttpEntity<>(requestBody, headers);
        
        try {
            ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);
            if (!response.getStatusCode().is2xxSuccessful()) {
                logAndThrow("Failed to start verification: " + response.getBody());
            }
        } catch (Exception e) {
            logAndThrow("Error starting verification: " + e.getMessage());
        }
    }

    public void verify(String phoneNumber, String token) {
        String url = TELNYX_API_BASE + "/verifications/by_phone_number/" + phoneNumber + "/actions/verify";
        
        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + settings.getTelnyxApiKey());
        headers.set("Content-Type", "application/json");

        String requestBody = String.format(
            "{\"code\":\"%s\",\"verify_profile_id\":\"%s\"}",
            token, settings.getTelnyxVerifyProfileId()
        );

        HttpEntity<String> request = new HttpEntity<>(requestBody, headers);
        
        try {
            ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);
            if (!response.getStatusCode().is2xxSuccessful()) {
                logAndThrow("Failed to verify token. ");
            }

            JsonNode jsonResponse = objectMapper.readTree(response.getBody());
            JsonNode data = jsonResponse.path("data");
            String responseCode = data.path("response_code").asText();
            
            if (!"accepted".equals(responseCode)) {
                logAndThrow("Error verifying token. ");
            }
        } catch (Exception e) {
            logAndThrow("Error verifying token: " + e.getMessage());
        }
    }

    private void logAndThrow(String message) {
        LOGGER.warn(message);
        throw new TokenVerificationException(message);
    }
}
