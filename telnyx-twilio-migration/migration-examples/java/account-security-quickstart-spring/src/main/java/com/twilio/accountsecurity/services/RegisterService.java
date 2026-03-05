package com.twilio.accountsecurity.services;

import com.authy.AuthyApiClient;
import com.authy.AuthyException;
import com.authy.api.User;
import com.twilio.accountsecurity.controllers.RegisterController;
import com.twilio.accountsecurity.controllers.requests.UserRegisterRequest;
import com.twilio.accountsecurity.exceptions.UserRegistrationException;
import com.twilio.accountsecurity.repositories.UserRepository;
import com.twilio.accountsecurity.exceptions.UserExistsException;
import com.twilio.accountsecurity.models.UserModel;
import com.twilio.accountsecurity.models.UserRoles;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class RegisterService {

    private static final Logger LOGGER = LoggerFactory.getLogger(RegisterController.class);

    private UserRepository userRepository;
    private PasswordEncoder passwordEncoder;
    private AuthyApiClient authyClient;

    @Autowired
    public RegisterService(UserRepository userRepository,
                           PasswordEncoder passwordEncoder,
                           AuthyApiClient authyClient) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.authyClient = authyClient;
    }

    public void register(UserRegisterRequest request) throws AuthyException {
        UserModel userModel = userRepository.findFirstByUsername(request.getUsername());

        if(userModel != null) {
            LOGGER.warn(String.format("User already exist: {}", request.getUsername()));
            throw new UserExistsException();
        }

        User authyUser = authyClient.getUsers().createUser(request.getEmail(),
                request.getPhoneNumber(),
                request.getCountryCode());

        if(authyUser.getError() != null) {
            throw new UserRegistrationException(authyUser.getError().getMessage());
        }
        UserModel newUserModel = request.toModel(passwordEncoder.encode(request.getPassword()));
        newUserModel.setRole(UserRoles.ROLE_USER);
        newUserModel.setAuthyId(authyUser.getId());
        userRepository.save(newUserModel);
    }
}
