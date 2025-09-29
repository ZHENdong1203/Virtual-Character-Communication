package com.example.anitalk;

import org.springframework.boot.SpringApplication;

public class TestAnitalkApplication {

    public static void main(String[] args) {
        SpringApplication.from(AnitalkApplication::main).with(TestcontainersConfiguration.class).run(args);
    }

}
