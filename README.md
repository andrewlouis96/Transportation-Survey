# Missoula Downtown Commute Survey 2024

## Project Overview

This project analyzes data from a City of Missoula transportation survey inspired by the Seattle Commute Survey. While the survey captured a variety of transportation habits and demographic details, its primary aim was to understand potential interest in a mobile app that encourages more sustainable commuting options and map downtown employees travel pattern to work. A preview of the survey can be found [here](https://missoulaparks.qualtrics.com/jfe/preview/previewId/f77cbedb-4863-4bd0-96d7-629c03e4a169/SV_1NsyG54i5twwOk6?Q_CHL=preview&Q_SurveyVersionID=current).

The final deliverables for this project include:

- A **digital product** for visual storytelling  
- A **scientific paper** detailing the analysis and findings  
- A **final presentation** to communicate insights to stakeholders

This repository includes the scientific analysis used to support the paper.

## Repository Structure

- `Analysis_Code_BoscoLouis_20250309.ipynb`: Machine learning model scripts to predict interest in the sustainable commuting app  
- `Categorization_Code_BoscoLouis_20250309.ipynb`: Natural language processing code for summarizing free-text survey responses
- `Geocode_BoscoLouis_03312025.ipynb`: Code that gets the geolocation codes for mapping approximate location of respondents homes and work.
- `Maps_Code_BoscoLouis_03312025.ipynb`: Code that displays maps of transport patterns among different respondent groups.
- `commute_journey.py`: Code that creates a website on streamlit to convey the results along with a guessing game.
- `random_forest_income_model.pkl`: Code that uses a model on the website to guess the income based on a few questions.
- `surveydata.csv`: Cleaned survey responses
- `README.md`: This file

## Research Questions and Methodology

### 1. Predictive Modeling (Logistic Regression, Random Forest, XGBoost)

**Could we build a model to predict interest in a sustainable commuting app based on survey responses?**

Even though the survey wasn't optimized for machine learning, this task flipped a limitation into a strength. By modeling app interest, we identified the most predictive variables—offering a data-backed way to improve future survey design and outreach strategy.

📂 **Code:** `Analysis_Code_BoscoLouis_20250309.ipynb`

---

### 2. Commute Priorities by Demographics (Chi-Squared Tests)

**Are there patterns in how different demographic groups rank the importance of time, cost, reliability, and other commute factors?**

This analysis explores statistical relationships between demographic segments and what they value most in their commute, helping inform more equitable transportation planning.

📂 **Code:** `Analysis_Code_BoscoLouis_20250309.ipynb`

---

### 3. Summarizing Open-Ended Survey Responses (LLM Categorization)

**How can we analyze hundreds of open-ended responses quickly and effectively?**

Two open-ended survey questions produced hundreds of long-form answers about seasonal commute changes and general thoughts on Missoula transportation. Instead of manually coding these responses, we used Large Language Models (LLMs) to categorize and summarize major themes. This approach saved time and provided scalable insights.

📂 **Code:** `Categorization_Code_BoscoLouis_20250309.ipynb`

---

### 4. Geographic Patterns in Commutes (Geocoding & Mapping)

**Where do people live and work, and how do commute patterns vary across Missoula?**

We geocoded respondents' home and work locations to visualize commuting patterns across Missoula. These maps reveal how commuting behaviors differ by neighborhood and transportation mode. The goal was to replicate the Seattle Commute Survey’s geographic visualizations, adapted for Missoula. This work helps identify neighborhoods where targeted transportation improvements (e.g., transit access, bike lanes) would have the most impact.

📂 **Code and outputs:** `Geocode_BoscoLouis_03312025.ipynb` - `Maps_Code_BoscoLouis_03312025.ipynb`:

---

### 5. Digital Product (Website & Game)

**Convey survey results through a fun and interactive website.**

📂 **Code and outputs:** `commute_journey.py` - `random_forest_income_model.pkl`:

---

## Technologies Used

- **Python** (data cleaning, modeling, NLP)  
- **Pandas & Geopandas & Scikit-learn** (data processing, ML, Geocoding)  
- **XGBoost** (advanced modeling)  
- **OpenAI API** (text summarization)
- **Streamlit** (website hosting)
