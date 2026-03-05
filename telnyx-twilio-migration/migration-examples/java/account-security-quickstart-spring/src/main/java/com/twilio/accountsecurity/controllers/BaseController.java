package com.twilio.accountsecurity.controllers;

import com.twilio.accountsecurity.utils.ThrowingRunnable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

public interface BaseController {

    default <E extends Exception> ResponseEntity<? extends Object> runWithCatch(ThrowingRunnable<E> runnable, HttpStatus status) {
        try {
            runnable.run();
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            return ResponseEntity.status(status)
                    .body(e.getMessage());
        }
    }

    default <E extends Exception> ResponseEntity<? extends Object> runWithCatch(ThrowingRunnable<E> runnable) {
        return this.runWithCatch(runnable, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
