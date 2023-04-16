package com.example.demo.entities;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;
import org.springframework.stereotype.Component;

import java.util.List;

@Getter
@Setter
//@RedisHash("susUrl")
//@AllArgsConstructor
public class SusURL {

    @Id
    private String url;

    private String pred;
    private String proba;

    public SusURL(String url, String prediction, String proba){
        this.url=url;
        this.pred=pred;
        this.proba=proba;
    }
}

