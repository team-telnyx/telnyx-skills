package com.twilio.accountsecurity.utils;

@FunctionalInterface
public interface ThrowingRunnable<E extends Exception> {
  public void run() throws E;
}
