package com.example.gpt.controller;

import com.example.gpt.service.TextGenerationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class TextGenerationController {

    @Autowired
    private TextGenerationService textGenerationService;

    @PostMapping("/generate")
    public String generateText(@RequestBody Map<String, String> request) {
        String prompt = request.get("prompt");
        return textGenerationService.generateText(prompt);
    }
}