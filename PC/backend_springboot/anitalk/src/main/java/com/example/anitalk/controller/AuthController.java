package com.example.anitalk.controller;

import com.example.anitalk.model.DTO.LoginRequest;
import com.example.anitalk.model.DTO.RegisterRequest;
import com.example.anitalk.model.PO.UserPO;
import com.example.anitalk.repository.UserRepository;
import com.example.anitalk.service.UserService;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final UserRepository userRepository;
    private final BCryptPasswordEncoder passwordEncoder;
    private final HttpSession httpSession;

    @Autowired
    private UserService userService;

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest req) {
        String captcha = (String) httpSession.getAttribute("captcha_code");
        if (captcha == null || !captcha.equalsIgnoreCase(req.getCaptcha())) {
            return ResponseEntity.badRequest().body(Map.of("success", false, "message", "验证码错误"));
        }

        if (userRepository.findByUsername(req.getUsername()).isPresent()) {
            return ResponseEntity.badRequest().body(Map.of("success", false, "message", "用户名已存在"));
        }

        UserPO userPO = UserPO.builder()
                .username(req.getUsername())
                .password(passwordEncoder.encode(req.getPassword()))
                .build();
        userRepository.save(userPO);

        return ResponseEntity.ok(Map.of("success", true, "message", "注册成功"));
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest req, HttpServletResponse response) {
        Optional<UserPO> opt = userRepository.findByUsername(req.getUsername());
        if (opt.isEmpty() || !passwordEncoder.matches(req.getPassword(), opt.get().getPassword())) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(Map.of("success", false,
                    "message", "用户名或密码错误"));
        }

        UserPO userPO = opt.get();

        if (userPO.getAvatarUrl() == null) {
            userPO.setAvatarUrl(userService.getRandomUserAvatar(userPO.getUsername()));
            userRepository.save(userPO);
        }

        httpSession.setAttribute("user_id", userPO.getId());

        return ResponseEntity.ok(Map.of("success", true, "message", "登录成功"));
    }

    @PostMapping("/logout")
    public ResponseEntity<?> logout() {
        httpSession.invalidate();
        return ResponseEntity.ok(Map.of("success", true, "message", "退出成功"));
    }

}

