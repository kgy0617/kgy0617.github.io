---
layout: post
title: "Korea Data Production & Data Intensity Measurement Project (Full Version)"
date: 2025-11-14 00:00:00 +0900
categories: [Digital-Economy, Data-Production, Data-Intensity, NLP, LLM]
---

# Korea’s Data Production Value & Data-Intensity Measurement  
This post integrates two major strands of work:  
1) Estimating Korea’s Data Production Value  
2) Building a Korea-adapted Data Intensity Measurement Framework**  

---

# 1. Estimation of Korea’s Data Production Value  
Estimating Korea’s data production value is essential for understanding the national digital economy and aligning with international statistical frameworks (OECD, IMF, UNSD).

## Objectives
- Quantify the economic value generated from data collection, processing, storage, and utilization  
- Adapt global guidelines to the Korean context  
- Build a reproducible statistical & computational pipeline  

## Methodology Summary
- Collected national-level administrative & survey datasets  
- Estimated:
  - Labor cost for data activities  
  - Infrastructure & cloud expenditure  
  - Software/platform investment  
- Combined cost-based & output-based valuation models  
- Automated ETL + statistical computing pipeline (Python-based)

## System Implementation
- Version-controlled workflow  
- Annual update process  
- Automated table/chart generation  
- Integration with internal metadata and statistical systems  

---

# 2. Korea-Adapted Data Intensity Measurement  
A complementary project assessing how much **data-related work** exists across occupations using job-posting data.

Highlights include:
- Large-scale Korean job-posting corpus  
- Korean morphological analysis  
- Localized terminology + occupation taxonomy  
- LLM-based contextual classification  

---


# 3. LLM Performance Table 

Model          Prompt   Accuracy Precision Recall F1-Score ROC-AUC
NLP Baseline   -        0.9138   0.4013    0.4217 0.4112   0.6867
GPT-3.5-ZS     Zero     0.9106   0.3937    0.4685 0.4279   0.7065
GPT-3.5-FS     Few-shot 0.9343   0.6359    0.1847 0.2863   0.5883
GPT-4o-ZS      Zero     0.9321   0.5332    0.3869 0.4484   0.6804
GPT-4o-FS      Few-shot 0.9403   0.5953    0.5100 0.5494   0.7417
Gemini-FL-ZS   Zero     0.8819   0.3052    0.5127 0.3826   0.7115
Gemini-FL-FS   Few-shot 0.7589   0.1963    0.7684 0.3127   0.7633
Gemma-27B-ZS   Zero     0.8269   0.2188    0.5542 0.3138   0.7011
Gemma-27B-FS   Few-shot 0.8878   0.3339    0.5743 0.4222   0.7431
Qwen3-30B-ZS   Zero     0.9166   0.3925    0.3079 0.3451   0.6356
Qwen3-30B-FS   Few-shot 0.9359   0.6000    0.3052 0.4046   0.6448
