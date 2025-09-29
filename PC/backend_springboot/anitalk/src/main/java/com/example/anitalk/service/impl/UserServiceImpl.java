package com.example.anitalk.service.impl;

import com.example.anitalk.service.UserService;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.ThreadLocalRandom;

public class UserServiceImpl implements UserService {
    public String getRandomUserAvatar(String username) {
        String[] styles = {"icons", "shapes", "thumbs", "bottts-neutral", "fun-emoji"};
        int index = ThreadLocalRandom.current().nextInt(styles.length);
        String style = styles[index];

        int randomNumber = ThreadLocalRandom.current().nextInt(1000, 10000);
        String seed = username + "_" + randomNumber;
        String encodedSeed = URLEncoder.encode(seed, StandardCharsets.UTF_8);
        return String.format("https://api.dicebear.com/9.x/%s/svg?seed=%s", style, encodedSeed);

    }


}
