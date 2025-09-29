package com.example.anitalk.model.DTO;

import lombok.Data;

@Data
public class ChangePasswordRequest {
    private Long userId;
    private String confirmPassword;
}

