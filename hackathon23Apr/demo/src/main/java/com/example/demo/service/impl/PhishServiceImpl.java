package com.example.demo.service.impl;

import com.example.demo.entities.SusURL;
//import com.example.demo.repo.SusURLRepo;
import com.example.demo.service.PhishService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PhishServiceImpl implements PhishService {

    @Autowired
    RedisTemplate<String, String> template;
    @Autowired
    RestTemplate tmpl;

//    ValueOperations<String, String> ops = redisTemplate.opsForValue();
    @Override
    public String infer_big_cache(String url){

        System.out.println(url);
        String prediction = template.opsForValue().get(url);
        System.out.println(prediction);
//        SusURL res = new SusURL(result.toString(),"None");
        return prediction;
    }
    @Override
    public SusURL infer_model(String url){
        SusURL res = tmpl.postForObject("http://localhost:8000/predict_this",
                new SusURL(url,"0","0"), SusURL.class);
        System.out.println("============================Infered Model============================");
        System.out.println(res);
        return res;
    }

//    public void add_url(){
//        SusURL student = new SusURL(
//                "Eng2015001", "John Doe", Student.Gender.MALE, 1);
//        studentRepository.save(student);

//    }


}
