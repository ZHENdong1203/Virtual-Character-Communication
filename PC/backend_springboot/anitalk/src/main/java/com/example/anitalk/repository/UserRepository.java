package com.example.anitalk.repository;

import com.example.anitalk.model.PO.UserPO;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<UserPO, Long> {
    Optional<UserPO> findByUsername(String username);
}

