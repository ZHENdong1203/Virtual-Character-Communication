package com.example.anitalk.controller;

import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;

@RestController
@RequiredArgsConstructor
public class CaptchaController {
    private final HttpSession session;

    @GetMapping("/api/captcha")
    public void getCaptcha(HttpServletResponse response) throws IOException {
        String code = String.valueOf(new Random().nextInt(9000) + 1000);
        session.setAttribute("captcha_code", code);

        BufferedImage image = new BufferedImage(100, 40, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = image.createGraphics();
        g.setColor(Color.WHITE); g.fillRect(0, 0, 100, 40);
        g.setFont(new Font("Arial", Font.BOLD, 24));
        g.setColor(Color.BLACK); g.drawString(code, 20, 28);

        response.setContentType("image/png");
        ImageIO.write(image, "PNG", response.getOutputStream());
    }
}

