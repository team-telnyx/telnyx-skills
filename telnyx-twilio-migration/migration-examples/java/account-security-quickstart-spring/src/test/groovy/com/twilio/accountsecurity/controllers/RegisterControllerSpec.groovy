package com.twilio.accountsecurity.controllers

import com.twilio.accountsecurity.controllers.requests.UserRegisterRequest
import com.twilio.accountsecurity.exceptions.UserExistsException
import com.twilio.accountsecurity.services.RegisterService
import org.springframework.test.web.servlet.MockMvc
import spock.lang.Specification
import spock.lang.Subject

import jakarta.servlet.ServletException
import jakarta.servlet.http.HttpServletRequest

import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup

class RegisterControllerSpec extends Specification {
    def registerService = Mock(RegisterService)
    def request = Mock(HttpServletRequest)
    @Subject def registerController = new RegisterController(registerService)

    MockMvc mockMvc = standaloneSetup(registerController).build()

    def username = 'user name'
    def password = 'password'
    def userRegisterRequest = new UserRegisterRequest(username, 'email', password, '1', '2')

    def 'register - returns 500 for ServletException'(){
        given:
        1 * registerService.register(_)
        1 * request.login(_, _) >> { throw new ServletException("message")}

        when:
        def response = registerController.register(userRegisterRequest, request)

        then:
        response.statusCode.value() == 500
        response.body == 'message'
    }

    def 'register - returns 409 for UserExistsException'(){
        given:
        1 * registerService.register(_) >> { throw new UserExistsException()}

        when:
        def response = registerController.register(userRegisterRequest, request)

        then:
        response.statusCode.value() == 412
        response.body == 'User already exists'
    }

    def 'register - returns 200'(){
        given:
        1 * registerService.register(_)
        1 * request.login(_, _)

        when:
        def response = registerController.register(userRegisterRequest, request)

        then:
        response.statusCode.value() == 200
    }

}
