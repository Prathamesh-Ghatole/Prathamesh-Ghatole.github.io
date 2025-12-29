---
title: "Portfolio"
date: 2024-01-11
draft: false
---
{{<image src="/cover.png">}}
`Updated Dec 29 2025`

#### Data & Gen AI Engineer | 2x Google Summer of Code | GCP Professional Data Engineer | Open Source

[**Email**](mailto:prathamesh.s.ghatole@gmail.com) | 
[**Linkedin**](https://www.linkedin.com/in/prathamesh-ghatole) | 
[**Twitter**](https://twitter.com/PrathameshG69) | 
[**GitHub**](https://github.com/Prathamesh-Ghatole/)

---

# 💫 About Me

Hi, I'm Prathamesh, a Data / Gen AI Engineer experienced in shipping end-to-end, data-driven software in fast-paced startup environments with a great track record of open-source contributions. I'm a Google Cloud certified Professional Data Engineer and have an academic background in Data Science & AI @ IIT Madras and Pune University.

---
## 🔬 Work Experience


#### **Data Engineer Consultant | [Gekko](https://www.gekko.io/)** `[Apr '24 - Current]`

- **AI for Oil Drilling**: Architected a hybrid ML system from the ground up, combining classification, entity extraction, and proprietary algorithms to infer drilling operations & parameters and reconstruct activity timelines from unstructured reports with 95%+ accuracy, saving 4 hrs/well across 1000s of wells.

- Selected a combination of small LLMs (qwen, gpt-oss, gemini), fast fine-tuned transformer models (BERT, GLiNER), and decision trees to meet strict latency and cost constraints. Implemented context-aware corrections and domain-specific guardrails to ensure physically consistent outputs.

- **Data mining**: Engineered a pipeline to mine structured insights from PDFs using multi-modal LLMs (gemini-2.5-flash) with pre-defined schemas, few shot examples, and text rules; outperformed SOTA tools like Docling for our use case. Optimized w/ annotation caching, input pruning, etc

- **Vessel & Fuel Analytics**: Designed a data warehousing solution & a Dagster pipeline to process vessel telemetry & geospatial data, saving clients $1.2M annually in fuel costs through clever fuel reporting using PostgreSQL, Dagster, Polars, Power BI.

- **Leadership**: Promoted to technical lead, responsible for architectural decisions and team building to drive automation, platform modernization. Led the delivery of 10+ misson-critical projects with a team of 6 engineers.

- **Tech Stack**: Python, Langchain, PyTorch, Pydantic, FastAPI, Dagster, PostgreSQL, Polars, Power BI, GCP, Docker, Git, etc.

#### **Data Engineer Intern | [New Engen Inc.](https://www.newengen.com/)** `[Dec '23 - Mar '24]`
- Assisted with Data Modelling and implementing Data Pipelines to Extract, Load, and Transform raw Facebook Ads data for Business Intelligence and Data Analytics teams at New Engen.

- Migrated complex pipelines from Salesforce Datorama and Adverity to a custom, In-house solution using GCP BigQuery, dbt, Apache Airflow, and Python.

- **Tech Stack**: Python, dbt, Google Cloud Platform, BigQuery, Airflow, Adverity, SalesForce Intelligence (Datorama), Git, etc.

#### **Data Engineering & Analytics Contributor | [Google Summer of Code 2023 @ Metabrainz](https://summerofcode.withgoogle.com/programs/2023/projects/TsPwhRct)** `[May '23 - Nov 2023]`

- Assembled an ETL pipeline from Wikidata to the MusicBrainz database, facilitating a 60% increase in new location data, and slashing manual data feeding by 90%. [[link](https://community.metabrainz.org/t/automate-areas-management-in-musicbrainz-gsoc-23-proposal/630489)]
- Independently designed and developed a scalable, production ready solution using Python (pandas, multiprocessing, requests, sqlalchemy), SQL (PostgreSQL), and Docker. [[architecture](https://blog.metabrainz.org/2023/11/06/gsoc-23-automating-area-management-in-musicbrainz/)] [[code](https://github.com/Prathamesh-Ghatole/MusicBrainz-AreaBot)]
- Conducted extensive research and experimentation, optimizing SPARQL queries to cater to Wikidata’s graph data structure to significantly improve data quality and extraction efficiency. [[details](https://community.metabrainz.org/t/automate-areas-management-in-musicbrainz-gsoc-23-proposal/630489##wikidata-musicbrainz-area-coverage-comparison-spam-detection-11)]

- **Tech Stack**: Python, SQL (PostgreSQL), SPARQL, Pandas, Git, Docker, Shell Scripting.
- **Domain**: Data Engineering, Data Analytics.

#### **Data Engineering & Analytics Contributor | [Google Summer of Code 2022 @ Metabrainz](https://summerofcode.withgoogle.com/programs/2022/projects/OARdCHQq)** `[May '22 - Oct 2022]`

- Enriched, cleaned, and combined 27 billion rows of music streaming data using Python (Pandas, Multiprocessing), SQL (PostgreSQL), and Apache Arrow – achieving high efficiency in Python without Spark. [[details](https://community.metabrainz.org/t/clean-up-the-music-listening-histories-dataset-gsoc-2022-proposal/579503)]
- Researched, experimented with, and implemented cutting-edge technologies like Zstandard and Apache Arrow to optimize data lake efficiency, resulting in a 53% reduction in storage and a 9% improvement in read/write speeds. [[details](https://blog.metabrainz.org/2022/10/28/cleaning-up-the-music-listening-histories-dataset/)]
- Performed Data Analytics and published Benchmarks, Dashboards, and Reports to help the collaborating teams better understand and utilize the data to train state-of-the-art Music Recommendation Systems.

- **Tech Stack**: Python, SQL (PostgreSQL), Pandas, Apache Arrow, Matplotlib, Git, Shell Scripting.
- **Domain**: Data Engineering, Data Analytics.
- **Project Summary**: https://blog.metabrainz.org/?p=9785

---

# 🎯 Skills:

- **Languages / Tools**: 
  - Python, SQL, Bash, Git, Linux, Docker
- **Data Engineering**: 
  - Pandas, Polars, Apache Arrow, PySpark, BigQuery, PostgreSQL, Dagster, Airflow, dbt
- **Applied AI**:
  - Langchain, Pydantic AI, n8n, GCP Vertex AI, OpenAI API
  - PyTorch, RAG & Vector Search (FAISS, Milvus), Prompt Engineering, Fine Tuning, (PEFT on ModernBERT using LoRA)
- **Cloud / DevOps**: CI/CD, GitHub Actions, Google Cloud (BigQuery, Vertex AI, Composer, Dataproc, IAM, etc), Azure (App Service, Virtual Machines)
- **Data Analytics**:
  - Power BI, Plotly Dash, Streamlit
- **Backend**: 
  - FastAPI, Pydantic, HTML, CSS, JavaScript

---

# 🏫 Education:

#### [BS. Data Science and Applications](https://study.iitm.ac.in/ds/) | Indian Institute of Technology, Madras ```[2021 - 2025]```
  - Dropped out to pursue full-time opportunities in Engineering.
  - **CGPA**: 8.24

#### [Btech. Artificial Intelligence](https://ghrcem.raisoni.net/artificial-intelligence) | G.H. Raisoni College of Engineering & Management, Pune ```[2020 - 2024]```
  - **CGPA**: 8.88

---

# 🏗️ Projects:

[**entityxtract**](https://github.com/Prathamesh-Ghatole/entityxtract/): Open Source document intelligence platform enabling structured data extraction from unstructured files. Alternative to GCP Document AI with bring-your-own-key support. Built using Python, LangChain, OpenRouter, Pydantic.

#### Freelance Project 1 | [proprietary]
  - Scalable, fault-tolerant data pipeline to scrape BSE/NSE notices, extract intelligence using Google Gemini, and publish email updates.
  - Written in Python, orchestrated with Cron. Containerized and Deployed on client VPS. This project was very heavy on Data Scraping and Cleaning using Beautiful Soup, PyPDF, and RegEx.
  - **Tech Stack**: Python, SQL (PostgreSQL), Cron, Linux, RegEX, Beautiful Soup
  - **Skills Used**: Data Scraping, ETL, DevOps

---

# 🏆 Achievements

  - Selected twice (Top 2% of 43K+ applicants) for Google Summer of Code 2022 & 2023.
  - Elected President (Student’s Association) and Vice President (IEEE Student Chapter).
  - Represented the South East Asia Cluster at IEEE Asia Pacific’s CLAP (2021) program.

---

# 🤝 Leadership / Extracurriculars

#### **Teaching Assistant (Machine Learning) | Dept. of Artificial Intelligence, GHRCEM Pune** ```[Mar 2023 '21 - May 2023]```
  -  Conducted hands-on Machine Learning, Data Processing, and Data Visualization sessions for 70+ sophomore students at the Dept. of AI (GHRCEM).
  - Introduced students to Machine Learning concepts like Linear Regression, Naive Bayes (incl. Text Classification), KNN, and Support Vector Machines, etc. using Python, scikit-learn, Pandas, Numpy, Matplotlib, and Seaborn.

#### **President | [Student's Association of Artificial Intelligence, GHRCEM, Pune](https://www.linkedin.com/company/saai-ghrcem)** ```[Nov '21 - Mar 2022]```
  - Operated Human Resources, Planning, and Execution for all events at the Department of AI, GHRCEM, Pune.
  - **Hosted events and workshops** like “Tech Talks 1.0: Biostatistics w/ Mr. Shariq Mohammed, Boston University”, and “YOU 2.0: The complete personality upliftment program” with **200+ attendees** and **4.59/5.00 average event ratings**.

#### **Co-Chair | IEEE Student's Chapter, GHRCEM Pune** ```[Mar '21 - Feb 2023]```
  - **Hosted several flagship events at IEEE Pune Section** - like IEEE CODE-STROM [2022], EAC Funded Cloud and
  Data Engineering Workshop [2022]
  - **Represented the South East Asia Cluster** at **IEEE Asia Pacific’s CLAP [2021]** program.

#### **Speaker and Project Lead | [Ek Bharat Shrestha Bharat Club, GHRCEM, Pune](https://ekbharat.gov.in/images/InstituteActivities/Documents/205720210909102002/News%20Report%20on%20Culinary%20Festivals%20of%20Maharashtra%20with%20Opportunity%20to%20Learn%20in%20Culinary%20Practices%20of%20Odisha.pdf)** ```[Sep '21 - Nov 2021]```
  - Designed and presented **5+ inter-state presentations** to Aryan Institute of Technology, Bhubaneshwar, Odisha; while **Representing** GH Raisoni College of Engineering and Management Pune, Maharashtra.

#### **Vice President - Music Club, GH Raisoni College of Engineering & Management, Pune** ```[Aug 2021 - Nov 2021]```
  - Operated Human Resources, Planning, and execution for 6+ introductory and jamming sessions.

---

# ⌨️ Blogs:

- [```🔗 Google Summer of Code 101: A Practical Guide with Resources!```](https://prathamesh-ghatole.hashnode.dev/google-summer-of-code-101-a-practical-guide-with-resources)

- [```🔗 Automating Area Management in MusicBrainz using Wikidata | GSoC 2023```](https://blog.metabrainz.org/2023/11/06/gsoc-23-automating-area-management-in-musicbrainz/)

- [```🔗 Cleaning The Music Listening Histories Dataset```](https://blog.metabrainz.org/2022/10/28/cleaning-up-the-music-listening-histories-dataset/)