//package com.example.demo.sec;
//
//import org.springframework.boot.autoconfigure.web.servlet.WebMvcAutoConfiguration;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.ComponentScan;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.web.servlet.config.annotation.CorsRegistry;
//import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
//
////import javax.servlet.Filter;
//
//
//@Configuration
//@ComponentScan
//public class CorsConfiguration {
//
////This can be used in combination with @CrossOrigin on the controller & method.
//
//    @Bean
//    public WebMvcConfigurer corsConfigurer() {
//        return new WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter() {
//            @Override
//            public void addCorsMappings(CorsRegistry registry) {
//                registry.addMapping("/**")
//                        .allowedMethods("HEAD","OPTIONS")
//                        .allowedHeaders("Origin", "X-Requested-With", "Content-Type", "Accept");
//            }
//        };
//    }
//}
