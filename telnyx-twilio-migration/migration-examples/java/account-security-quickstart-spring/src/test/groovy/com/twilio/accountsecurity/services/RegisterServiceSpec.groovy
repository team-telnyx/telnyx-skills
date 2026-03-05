package com.twilio.accountsecurity.services

import com.authy.AuthyApiClient
import com.authy.api.Error
import com.authy.api.User
import com.authy.api.Users
import com.twilio.accountsecurity.controllers.requests.UserRegisterRequest
import com.twilio.accountsecurity.exceptions.UserRegistrationException
import com.twilio.accountsecurity.repositories.UserRepository
import com.twilio.accountsecurity.exceptions.UserExistsException
import com.twilio.accountsecurity.models.UserModel
import com.twilio.accountsecurity.models.UserRoles
import org.springframework.security.crypto.password.PasswordEncoder
import spock.lang.Specification
import spock.lang.Subject

class RegisterServiceSpec extends Specification {

    @Subject RegisterService service

    PasswordEncoder passwordEncoder = Mock()
    UserRepository userDao = Mock()
    AuthyApiClient authyApiClient = Mock()
    Users users = Mock()

    def username = 'username'
    def authyId = 123
    def request = new UserRegisterRequest(username, 'email', 'password', '1', '1234567')

    def setup() {
        service = new RegisterService(userDao, passwordEncoder, authyApiClient)
    }

    def 'register should fail when the username already exist'() {
        given:
        1 * userDao.findFirstByUsername(username) >> new UserModel()

        when:
        service.register(request)

        then:
        thrown UserExistsException
    }

    def 'register should fail for Authy create failure'() {
        given:
        def authyUser = new User()
        def error = new com.authy.api.Error()
        error.message = 'authy error'
        authyUser.setError(error)

        def expectedUser = request.toModel()
        expectedUser.setAuthyId(authyId)
        expectedUser.setRole(UserRoles.ROLE_USER)
        1 * userDao.findFirstByUsername(username) >> null
        1 * authyApiClient.getUsers() >> users
        1 * users.createUser(request.email, request.phoneNumber, request.countryCode) >>
                authyUser
        0 * userDao.save(_)

        when:
        service.register(request)

        then:
        UserRegistrationException e = thrown()
        e.getMessage() == 'authy error'
    }

    def 'register should save new user'() {
        given:
        def authyUser = new User()
        authyUser.setId(authyId)
        def expectedUser = request.toModel()
        expectedUser.setAuthyId(authyId)
        expectedUser.setRole(UserRoles.ROLE_USER)
        1 * userDao.findFirstByUsername(username) >> null
        1 * authyApiClient.getUsers() >> users
        1 * users.createUser(request.email, request.phoneNumber, request.countryCode) >>
                authyUser
        1 * userDao.save(expectedUser)

        when:
        service.register(request)

        then:
        notThrown UserExistsException
    }

}