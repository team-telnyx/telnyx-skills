package com.twilio.accountsecurity.filters;

import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.web.filter.OncePerRequestFilter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

public class TwoFAFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        Object authy = request.getSession().getAttribute("authy");
        if (requiresFilter(request) && (authy == null || !((Boolean)authy))) {
            response.sendRedirect(request.getContextPath() + "/login/index.html");
            return;
        }
        filterChain.doFilter(request, response);
    }

    private boolean requiresFilter(HttpServletRequest request) {
        return new AntPathRequestMatcher("/protected/**").matches(request);
    }
}
