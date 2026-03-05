package com.twilio.accountsecurity.controllers

import com.twilio.accountsecurity.controllers.requests.VerifyTokenRequest
import com.twilio.accountsecurity.exceptions.TokenVerificationException
import com.twilio.accountsecurity.services.TokenService
import org.springframework.test.web.servlet.MockMvc
import spock.lang.Specification
import spock.lang.Subject

import jakarta.servlet.http.HttpServletRequest
import jakarta.servlet.http.HttpSession
import java.security.Principal

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup

class TokenControllerSpec extends Specification {
    def tokenService = Mock(TokenService)
    @Subject def tokenController = new TokenController(tokenService)

    MockMvc mockMvc = standaloneSetup(tokenController).build()

    def username = 'user name'

    def 'sms - returns 500 for TokenVerificationException'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendSmsToken(username) >> {
            throw new TokenVerificationException('message')}

        when:
        def response = mockMvc
                .perform(post('/api/token/sms').principal(principal))
                .andReturn().response

        then:
        response.status == 500
        response.contentAsString == 'message'
    }

    def 'sms - returns 200'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendSmsToken(username)

        when:
        def response = mockMvc
                .perform(post('/api/token/sms').principal(principal))
                .andReturn().response

        then:
        response.status == 200
    }

    def 'voice - returns 500 for TokenVerificationException'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendVoiceToken(username) >> {
            throw new TokenVerificationException('message')}

        when:
        def response = mockMvc
                .perform(post('/api/token/voice').principal(principal))
                .andReturn().response

        then:
        response.status == 500
        response.contentAsString == 'message'
    }

    def 'voice - returns 200'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendVoiceToken(username)

        when:
        def response = mockMvc
                .perform(post('/api/token/voice').principal(principal))
                .andReturn().response

        then:
        response.status == 200
    }

    def 'onetouch - returns 500 for TokenVerificationException'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendOneTouchToken(username) >> {
            throw new TokenVerificationException('message')}

        when:
        def response = mockMvc
                .perform(post('/api/token/onetouch').principal(principal))
                .andReturn().response

        then:
        response.status == 500
        response.contentAsString == 'message'
    }

    def 'onetouch - returns 200'(){
        given:
        def principal = Mock(Principal)
        2 * principal.getName() >> username
        1 * tokenService.sendOneTouchToken(username)

        when:
        def response = mockMvc
                .perform(post('/api/token/onetouch').principal(principal))
                .andReturn().response

        then:
        response.status == 200
    }

    def 'onetouchstatus - return 200 for status true'() {
        given:
        def session = Mock(HttpSession)
        def request = Mock(HttpServletRequest)
        1 * request.getSession() >> session
        1 * session.getAttribute('onetouchUUID') >> 'uuid'
        1 * tokenService.retrieveOneTouchStatus('uuid') >> true
        1 * session.setAttribute('authy', true)

        when:
        def response = tokenController.oneTouchStatus(request)

        then:
        response.statusCode.value() == 200
        response.body == true
    }

    def 'onetouchstatus - return 500 for TokenVerificationException'() {
        given:
        def session = Mock(HttpSession)
        def request = Mock(HttpServletRequest)
        1 * request.getSession() >> session
        1 * session.getAttribute('onetouchUUID') >> 'uuid'
        1 * tokenService.retrieveOneTouchStatus('uuid') >> {
            throw new TokenVerificationException('message')}

        when:
        def response = tokenController.oneTouchStatus(request)

        then:
        response.statusCode.value() == 500
        response.body == 'message'
    }

    def 'verify - returns 200'() {
        given:
        def requestBody = new VerifyTokenRequest('token')
        def session = Mock(HttpSession)
        def request = Mock(HttpServletRequest)
        def principal = Mock(Principal)
        1 * request.getUserPrincipal() >> principal
        1 * principal.getName() >> username
        1 * request.getSession() >> session
        1 * tokenService.verify(username, requestBody)
        1 * session.setAttribute('authy', true)

        when:
        def response = tokenController.verify(requestBody, request)

        then:
        response.statusCode.value() == 200
    }

    def 'verify - returns 400 for failed verification'() {
        given:
        def requestBody = new VerifyTokenRequest('token')
        def session = Mock(HttpSession)
        def request = Mock(HttpServletRequest)
        def principal = Mock(Principal)
        1 * request.getUserPrincipal() >> principal
        1 * principal.getName() >> username
        0 * request.getSession() >> session
        1 * tokenService.verify(username, requestBody) >>
                {throw new TokenVerificationException('message')}
        0 * session.setAttribute('authy', true)

        when:
        def response = tokenController.verify(requestBody, request)

        then:
        response.statusCode.value() == 400
        response.body == 'message'
    }
}
