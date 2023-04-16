package com.example.demo.config;

import com.example.demo.entities.Quote;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.logging.Logger;

@ComponentScan
@Component
public class RestClientConfig {
//    private static final Logger log = LoggerFactory.getLogger(RestClientConfig.class);
    @Bean
    @Primary
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder.build();
    }

//    @Bean
//    public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
//        return args -> {
//            Quote quote = restTemplate.postForObject(
//                    "http://localhost:8000/detect_this", new Quote(sus_url), Quote.class);
//            System.out.println(quote.toString());
//        };


}
