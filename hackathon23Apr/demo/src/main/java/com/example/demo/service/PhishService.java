package com.example.demo.service;

import com.example.demo.entities.SusURL;
import org.springframework.stereotype.Service;

@Service
public interface PhishService {

    public String infer_big_cache(String url);
    public SusURL infer_model(String url);
}
