package com.twilio.accountsecurity.controllers

import com.twilio.accountsecurity.controllers.requests.PhoneVerificationStartRequest
import com.twilio.accountsecurity.controllers.requests.PhoneVerificationVerifyRequest
import com.twilio.accountsecurity.exceptions.PhoneVerificationException
import com.twilio.accountsecurity.services.PhoneVerificationService
import org.json.JSONObject
import org.springframework.http.MediaType
import org.springframework.test.web.servlet.MockMvc
import spock.lang.Specification
import spock.lang.Subject

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.request
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup

class PhoneVerificationControllerSpec extends Specification {

    def phoneVerificationService = Mock(PhoneVerificationService)
    @Subject
    def phoneVerificationController = new PhoneVerificationController(phoneVerificationService)

    MockMvc mockMvc = standaloneSetup(phoneVerificationController).build()

    static phone = '1'
    static via = 'sms'
    static token = 'token'

    def "start - returns 200"() {
        given:
        def request = new PhoneVerificationStartRequest(phone, via)
        def requestBody = new JSONObject(request).toString()
        1 * phoneVerificationService.start(phone, via)

        when:
        def response = mockMvc.perform(post('/api/phone-verification/start')
                .content(requestBody)
                .contentType(MediaType.APPLICATION_JSON))
                .andReturn().response

        then:
        response.status == 200
    }

    def "start - returns 500 for PhoneVerificationException"() {
        given:
        def request = new PhoneVerificationStartRequest(phone, via)
        def requestBody = new JSONObject(request).toString()
        1 * phoneVerificationService.start(phone, via) >> {
            throw new PhoneVerificationException('message')
        }

        when:
        def response = mockMvc.perform(post('/api/phone-verification/start')
                .content(requestBody)
                .contentType(MediaType.APPLICATION_JSON))
                .andReturn().response

        then:
        response.status == 500
        response.contentAsString == 'message'
    }

    def "verify - returns 200"() {
        given:
        def httpRequest = new PhoneVerificationVerifyRequest(phone, token)
        def requestBody = new JSONObject(httpRequest).toString()
        1 * phoneVerificationService.verify(phone, token)

        expect:
        mockMvc
            .perform(post('/api/phone-verification/verify')
                    .content(requestBody)
                    .contentType(MediaType.APPLICATION_JSON))
            .andExpect(status().isOk())
            .andExpect(request().sessionAttribute("ph_verified", true))
    }

    def "verify - returns 500 for PhoneVerificationException"() {
        given:
        def httpRequest = new PhoneVerificationVerifyRequest(phone, token)
        def requestBody = new JSONObject(httpRequest).toString()
        1 * phoneVerificationService.verify(phone, token) >> {
            throw new PhoneVerificationException('message')
        }

        when:
        def response = mockMvc.perform(post('/api/phone-verification/verify')
                .content(requestBody)
                .contentType(MediaType.APPLICATION_JSON))
                .andReturn().response

        then:
        response.status == 500
        response.contentAsString == 'message'
    }
}
