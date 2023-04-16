package com.example.demo.controller;

import com.example.demo.entities.RequestOnlyUrl;
import com.example.demo.entities.Response;
import com.example.demo.entities.SusURL;
import com.example.demo.service.PhishService;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@AllArgsConstructor
public class PhishController {

    @Autowired
    PhishService phishService;
    @GetMapping("/phishing/cache/{url}")
    public String infer_big_cache(@PathVariable String url){
        String cache_hit = (String) phishService.infer_big_cache(url);
        if(cache_hit==null){
            return infer_model(url).getPred();
        }
        else{
            return phishService.infer_big_cache(url);
        }
    }
    @CrossOrigin(origins = "chrome-extension://jiaipfgopannfabcnmpdbieclilllmii")
    @PostMapping("/phishing/detect")
    public SusURL infer_detect_post(@RequestBody RequestOnlyUrl url){

        String cache_hit = (String) phishService.infer_big_cache(url.getUrl());
//        System.out.println(cache_hit.getClass());
        if(cache_hit==null){
            System.out.println("===========Infering Model===========");
            System.out.println(infer_model(url.getUrl()).getPred());
            return infer_model(url.getUrl());
        }
        else{
            System.out.println("===========Not Infering Model===========");
            return new SusURL(url.getUrl(), "big cache hit","1.0");
        }
    }

    @CrossOrigin(origins = "chrome-extension://jiaipfgopannfabcnmpdbieclilllmii")
    @GetMapping("/phishing/detect/{url}")
    public SusURL infer_detect_get(@PathVariable String url){

        String cache_hit = (String) phishService.infer_big_cache(url);
//        System.out.println(cache_hit.getClass());
        if(cache_hit==null){
            System.out.println("===========Infering Model===========");
            System.out.println(infer_model(url).getPred());
            return infer_model(url);
        }
        else{
            System.out.println("===========Not Infering Model===========");
            return new SusURL(url, "big cache hit","1.0");
        }
    }

    @GetMapping("/phishing/model/{url}")
    public SusURL infer_model(@PathVariable String url){
        return phishService.infer_model(url);
    }
}
