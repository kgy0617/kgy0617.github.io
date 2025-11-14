---
layout: post
title: "Measuring Korea’s Data Production Value and Data-Intensity in Occupations"
date: 2025-11-14 00:00:00 +0900
categories: [Digital-Economy, Data-Production, Data-Intensity, NLP, LLM]
---

# Measuring Korea’s Data Production Value and Data-Intensity in Occupations
This post presents an integrated framework for understanding how data functions as a production factor in Korea’s economy.  
It covers two major components:

1. Estimating Korea’s Data Production Value
2. Measuring the Data-Intensity of Occupations using NLP and LLMs

Both are foundational to building modern digital economy statistics aligned with OECD, IMF, and BIS guidelines.

---

# 1. Data as a Production Factor

Data generation, management, and analysis have become core drivers of productivity across industries.  
International organizations highlight the rapid rise of data-intensive occupations:

- OECD: Data work is increasingly embedded in job tasks  
- IMF: Digital capital and data-related activities fuel productivity  
- BIS: Data is an emerging economic asset  

To reflect this in National Accounts, countries must measure:

- The value created through data activities  
- The extent to which occupations rely on data-related tasks  

---

# 2. Estimating Korea’s Data Production Value

The data production value refers to the economic value generated through data collection, processing, storage, and utilization.

## 2.1 Method Overview
We follow an internationally harmonized approach combining:

- Cost-based measurement
  - Labor cost for data activities  
  - Infrastructure (cloud, servers, networks)  
  - Software and platform investment  
- Output-based measurement
  - Data-related service outputs  
  - Data-enabled products  

These are adapted to Korea’s industry structure and administrative data sources.

## 2.2 System Implementation
A reproducible, automated pipeline was developed:

- Python-based ETL for ingesting large data sources  
- Preprocessing, standardization, and cost aggregation  
- Annual statistical tables generated programmatically  
- Integration with internal metadata repositories  
- Version-controlled workflow for auditability  

## 2.3 Key Insights
- Korea’s data production value has grown steadily over the past decade  
- Highest data-related activities detected in:
  - Finance  
  - ICT  
  - Manufacturing  
- Supports digital transformation strategies and international comparison  

---

# 3. Measuring Data-Intensity in Occupations

To understand how deeply data permeates the labor market, we measure how much data-related work is embedded in each occupation using online job postings.

---

# 4. Why Use Online Job Postings?

Online recruitment data provides:

- Timely information on labor-market trends  
- Granular descriptions of tasks and skills  
- Scalable coverage across sectors  

But the data also presents challenges:

- Noise, duplication, and inconsistent formatting  
- Missing or ambiguous information  
- Significant linguistic variation  

Therefore, sophisticated text processing is required.

---

# 5. OECD Framework and Its Limitations

### OECD Method
Uses dictionary- and rule-based text matching to detect data-related tasks.

### Limitations
- **Context-insensitive**
  - “analysis” in finance ≠ “analysis” in logistics  
- Cannot capture emerging occupations
  - e.g., “AI strategy planner,” “data governance lead”  
- Lower performance in non-English languages
- Struggles with linguistic variation and complex phrasing  

---

# 6. Developing a Korea-Specific Framework

To adapt the methodology to Korean labor market conditions, we:

## 6.1 Localization Steps
- Built a large-scale Korean job-posting dataset  
- Applied Korean morphological analysis
- Incorporated Korean-specific terminology  
- Mapped to domestic occupational taxonomy (NCS, KSCO)  
- Rebuilt and extended the OECD dictionary and rule sets  
- Added domain terms reflecting modern data practice (ETL, ML ops, cloud infra, dashboards, etc.)  

---

# 7. Processing Pipeline
![alt text](/assets/images/image.png)


# 8. LLM Enhancements Beyond the OECD Method

LLM-based classification overcomes many of the OECD method’s limitations.

Capabilities
	•	Contextual understanding of job tasks
	•	Robustness to linguistic variation
	•	Identification of emerging or unstructured roles
	•	Generalization beyond fixed dictionaries
	•	Confidence scoring
	•	Evidence-based reasoning
	•	Task-share estimation:
	•	Input-level
	•	Management-level
	•	Analysis-level


# 9. Performance Comparison: NLP vs. LLM Models
<pre>
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


Main Findings
	•	GPT-4o Few-shot provides the best overall performance
	•	Gemini Flash Lite Few-shot yields strong ROC-AUC, good for sensitivity-driven detection
	•	LLM-based approaches significantly outperform dictionary-based baselines for Korean

⸻

# 10. Integrated Insights

Together, the two components provide a holistic view of Korea’s digital economy:

Data Production Value

→ Quantifies the economic value of data activities at the national level.

Data-Intensity in Occupations

→ Measures how data work is embedded in the labor market.

Combined Benefits
	•	Stronger statistical basis for digital economy policy
	•	Better understanding of industry-level differences
	•	Evidence for investment in data infrastructure and skills
	•	Alignment with international statistical standards

  </pre>