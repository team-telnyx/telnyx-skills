package com.twilio.accountsecurity.repositories;

import com.twilio.accountsecurity.models.UserModel;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<UserModel, Integer> {

    UserModel findFirstByUsername(String username);
}
