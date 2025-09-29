package com.example.anitalk.controller;

import com.example.anitalk.model.DTO.ChangePasswordRequest;
import com.example.anitalk.model.PO.UserPO;
import com.example.anitalk.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/user")
@RequiredArgsConstructor
public class UserController {
    private final UserRepository userRepository;
    private final BCryptPasswordEncoder passwordEncoder;

    @PostMapping("/change-password")
    public ResponseEntity<?> changePassword(@RequestBody ChangePasswordRequest req) {
        var userOpt = userRepository.findById(req.getUserId());
        if (userOpt.isEmpty()) {
            return ResponseEntity.badRequest().body(Map.of("success", false, "message", "用户不存在"));
        }

        UserPO user = userOpt.get();
        user.setPassword(passwordEncoder.encode(req.getConfirmPassword()));
        userRepository.save(user);

        return ResponseEntity.ok(Map.of("success", true, "message", "密码修改成功"));
    }
}

