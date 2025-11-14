---
layout: post
title: "News Sentiment Index: Migration from Oracle Batch Processing to Spark-based In-Memory Pipeline"
date: 2024-12-30 00:00:00 +0900
categories: [NLP, Spark, Sentiment-Index, Data-Engineering]
---

## 1. Overview
To develop the News Sentiment Index (NSI), the traditional workflow relied on Oracle-based batch processing to handle large-scale news datasets. As data volume and update frequency increased, the Oracle batch approach reached its performance and scalability limits. To address these issues, I redesigned the processing pipeline using Apache Spark to enable distributed, in-memory computation.

## 2. Background
- Previous workflow: Oracle stored procedures and batch jobs for large news text files  
- Challenges:
  - Slow I/O-bound processing  
  - High latency for iterative NLP tasks  
  - Limited scalability with growing data volume  
- Requirement: A high-performance pipeline capable of processing millions of text records for sentiment scoring, topic extraction, and daily updates

## 3. Spark-based In-Memory Processing Pipeline
### Key Improvements
1. Adoption of Apache Spark for distributed, in-memory data processing  
2. Replacement of Oracle-based ETL with Spark DataFrame operations  
3. Integration with Python NLP modules for feature extraction and sentiment scoring  
4. Parallelization of tokenization, vectorization, and model inference tasks  
5. Support for incremental ingestion of new news articles

### Architecture Summary
- Input Source: Large-scale raw news text files (daily ingestion)  
- Processing Engine: Spark cluster (in-memory execution)  
- NLP Layer: Python-based sentiment analysis and feature engineering  
- Output Target: Structured sentiment index dataset for downstream analysis and visualization  

## 4. Performance Gains
- Significant reduction in processing time (batch → near real-time capability)  
- Improved scalability for multi-day or multi-year news archives  
- Efficient handling of large files (GB-TB scale) without Oracle I/O bottlenecks  
- Better resource utilization through distributed memory execution  

## 5. Impact on the News Sentiment Index (NSI)
- Enabled timely sentiment updates required for economic indicators  
- Improved consistency and accuracy of text-based metrics  
- Provided a foundation for future enhancements such as:
  - Transformer-based sentiment models  
  - Topic clustering and anomaly detection  
  - Real-time news monitoring  

## 6. Summary
The migration from Oracle batch processing to a Spark-based in-memory pipeline transformed the performance and scalability of the News Sentiment Index development workflow. This architectural shift significantly improved processing efficiency and enabled more advanced NLP techniques to be integrated into the index calculation system.