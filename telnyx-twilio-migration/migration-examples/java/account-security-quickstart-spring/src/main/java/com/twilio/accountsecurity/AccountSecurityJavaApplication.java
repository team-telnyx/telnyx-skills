package com.twilio.accountsecurity;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccountSecurityJavaApplication implements CommandLineRunner {
    public static void main(String[] args) {
        SpringApplication.run(AccountSecurityJavaApplication.class, args);
    }

    /**
     * Method that runs on app initialization. It will parse and insert the questions in the DB
     * on every app initialization
     */
    @Override
    public void run(String... strings) throws Exception {
    }
}
