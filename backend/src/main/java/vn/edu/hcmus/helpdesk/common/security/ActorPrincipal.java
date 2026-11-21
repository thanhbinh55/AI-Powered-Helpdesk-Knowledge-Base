package vn.edu.hcmus.helpdesk.common.security;

import java.util.UUID;

public record ActorPrincipal(
        UUID userId,
        String email,
        UserRole role,
        boolean enabled
) {
    public boolean isCustomer() {
        return role == UserRole.CUSTOMER;
    }

    public boolean isAgent() {
        return role == UserRole.AGENT;
    }

    public boolean isAdmin() {
        return role == UserRole.ADMIN;
    }
}
