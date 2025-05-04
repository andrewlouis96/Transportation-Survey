import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ===============================
# 🚀 Page Setup
# ===============================
st.set_page_config(page_title="Missoula Commute Journey", layout="wide")

# ===============================
# 🛣️ Welcome
# ===============================

st.title("🛣️ From A to B: Missoula's Commute Story")

st.image("Picture1.jpg", caption="Downtown Missoula Survey Coverage")

# ===============================
# 🧩 Mini-Survey (Guess Your Income)
# ===============================

st.header("Want Us to Guess Your Income? 🎯")

# NEW expanded questions based on important features
mode = st.selectbox("How do you usually commute?", [
    "Drive Alone", "Bike", "Walk", "Bus", "Carpool/Vanpool", "Other"
])

need_car_for_work = st.selectbox(
    "Do you need your car for work purposes?", ["Yes", "No"]
)

flexibility_importance = st.selectbox(
    "How important is commute flexibility for you?", ["Not important", "Somewhat important", "Very important"]
)

commute_stress = st.selectbox(
    "How would you describe your commute experience?", ["Very stressful", "Somewhat stressful", "Neutral", "Somewhat enjoyable", "Very enjoyable"]
)

remote_policy = st.selectbox(
    "What is your company's remote work policy?", [
        "Must be in workplace daily",
        "1-2 days remote per week",
        "3-4 days remote per week",
        "Fully flexible"
    ]
)

way_to_go_program = st.selectbox(
    "Are you familiar with Missoula's 'Way to Go' program?", ["Yes", "No"]
)

age_group = st.selectbox(
    "What is your age group?", [
        "Under 25", "25–34", "35–44", "45–54", "55–64", "65 or older"
    ]
)

race_group = st.selectbox(
    "What race/ethnicity best describes you?", [
        "White/Caucasian", "Multiracial", "Other", "Prefer not to answer"
    ]
)

# ===============================
# 🔮 Load Real Income Model + Predict
# ===============================

try:
    with open('random_forest_income_model.pkl', 'rb') as file:
        rf_model = pickle.load(file)

    input_features = {}

    # Commute Mode Encoding
    commute_map = {
        "Drive Alone": "Q7_drive_alone_3",
        "Bike": "Q7_1",
        "Walk": "Q7_3",
        "Bus": None,  
        "Carpool/Vanpool": None,
        "Other": None
    }
    for commute_code in ["Q7_drive_alone_3", "Q7_1", "Q7_3"]:
        input_features[commute_code] = 0  # default

    if commute_map.get(mode):
        input_features[commute_map[mode]] = 1

    # Need car for work
    input_features["Q10_2_1"] = 1 if need_car_for_work == "Yes" else 0

    # Commute Flexibility Importance
    input_features["Q19_3_1"] = 1 if flexibility_importance == "Not important" else 0
    input_features["Q19_3_4"] = 1 if flexibility_importance == "Somewhat important" else 0
    input_features["Q19_3_5"] = 1 if flexibility_importance == "Very important" else 0

    # Commute Stress
    input_features["Q19_5_1"] = 1 if commute_stress == "Very stressful" else 0
    input_features["Q19_5_6"] = 1 if commute_stress == "Very enjoyable" else 0

    # Remote Work Policy
    input_features["Q18_1"] = 1 if remote_policy == "Must be in workplace daily" else 0
    input_features["Q18_4"] = 1 if remote_policy == "Fully flexible" else 0

    # Familiarity with Way to Go Program
    input_features["Q22_2"] = 1 if way_to_go_program == "Yes" else 0

    # Age Group
    input_features["Q26_3"] = 1 if age_group == "35–44" else 0
    input_features["Q26_5"] = 1 if age_group == "55–64" else 0
    input_features["Q26_8"] = 1 if age_group == "65 or older" else 0

    # Race Group
    input_features["Q28_7"] = 1 if race_group == "Multiracial" else 0
    input_features["Q28_9"] = 1 if race_group == "Other" else 0

    user_input_df = pd.DataFrame([input_features])

    model_features = rf_model.feature_names_in_
    missing_cols = [col for col in model_features if col not in user_input_df.columns]
    for col in missing_cols:
        user_input_df[col] = 0

    user_input_df = user_input_df[model_features]

    # Make prediction
    pred_income_class = rf_model.predict(user_input_df)[0]

    income_labels = {
        1: "Less than $15,000",
        2: "$15,000 to $24,999",
        3: "$25,000 to $34,999",
        4: "$35,000 to $49,999",
        5: "$50,000 to $74,999",
        6: "$75,000 to $99,999",
        7: "$100,000 to $149,999",
        8: "$150,000 or more"
    }

    predicted_income = income_labels.get(pred_income_class, "an unknown range")

    st.subheader("🎉 Based on your answers, we guess your income is:")
    st.markdown(f"### 💰 `{predicted_income}`")

except Exception as e:
    st.error(f"Prediction failed.\n\nError Details: {e}")
    st.info("Showing a sample guess: $50,000 to $74,999.")

# ===============================
# 📚 Introduction
# ===============================

st.header("Introduction")

st.write("""
The City of Missoula conducted a downtown employee commute survey, inspired by Seattle’s transportation surveys.  
The aim of the survey was to better understand how Missoulians commute, identify patterns and barriers, and ultimately design programs and policies to encourage more sustainable transportation choices.
""")

# ===============================
# 🧪 Survey Methods
# ===============================

st.header("Survey Methods")

st.write("""
The survey was delivered electronically to downtown employers, who distributed it to their employees.  
Responses were collected from approximately 900 employees.  
Data cleaning involved removing blank responses and duplicate entries.  
Analysis was conducted using Python (Pandas, scikit-learn), and geocoding was completed using OpenStreetMap.
""")

# ===============================
# 👥 Demographics
# ===============================

st.header("Demographics")

st.write(f"""
Three demographic questions regarding age, income, and race were asked in the survey. The results are as follows:

- Almost a third of respondents (**29.1%**) fell within the **35–44** age range, followed by the **25–34** age range (**26.8%**) and the **45–54** age range (**21.5%**).  
  The oldest group, **55–64**, contributed to **14%**, and the youngest group, **18–24**, contributed **5.6%**.  
  People over **65** were **2.4%**, and **0.5%** preferred not to answer.

- More than a third (**34.4%**) of the population that answered the income question (**N=707**) fell in the `$50,000 to $74,999` income group.  
- The second largest group (**22.9%**) was the `$35,000 to $49,999` group, followed by the `$75,000 to $99,999` group (**16.8%**).  
- **9.3%** make about `$100,000 to $149,999`, and **5.7%** make `$150,000 or more`.  

On the lower end:  
- `$25,000 to $34,999`: **6.4%**  
- `$15,000 to $24,999`: **3.8%**  
- `Less than $15,000`: **0.7%**

- Regarding race (**N=719**):  
  - **84.1%** identified as **White/Caucasian**  
  - **11.1%** reported **multiple ethnicities**  
  - **1.8%** were **Hispanic**  
  - **1.5%** were **American Indian or Alaskan Native**  
  - **0.7%** each identified as **Asian/Pacific Islander** and **Black or African American**
""")

# ===============================
# 🚗 Commute Modes
# ===============================

st.header("Commute Modes")

st.write("""
The most common primary mode of commuting reported was driving alone, with over 71.1% of respondents selecting it as their usual method. This was followed by biking, carpooling/vanpooling, walking, telecommuting, and taking the bus. A small portion of respondents reported using other forms of commuting, such as e-bikes, Uber/Lyft, or taxis.
""")

# ===============================
# 🏠 Remote Work Patterns
# ===============================

st.header("Remote Work Patterns")

st.write("""
Roughly one-third of respondents reported working remotely at least one day per week. Of those, most had some formal remote work policy through their employer.
Remote work frequency was notably higher among higher-income individuals. For example, 39.4% of people who said they work remotely make about $50,000 to $74,999 in annual income, and 35.9% of people who make $150,000 or more said they work remotely.
""")

# ===============================
# ❄️ Seasonal Variability
# ===============================

st.header("Seasonal Variability")

st.write("""
Nearly 48.7% of respondents reported not changing commute modes seasonally.  
However, summer months saw increased biking and walking, while winter months saw increased driving and bus use.  
Snow, ice, and darkness were significant deterrents to winter biking and walking.
""")

# ===============================
# 🚧 Barriers
# ===============================

st.header("Barriers to Sustainable Commuting")

st.write("""
The most common barriers to sustainable commuting were:
- Weather
- Distance
- Flexibility needs
- Time
- Commute stress
- Family responsibilities
- Lack of safe biking or walking infrastructure
""")

# ===============================
# 🎁 Incentives
# ===============================

st.header("Incentives for Changing Commute Mode")

st.write("""
Top incentives cited included:
- Cash rewards for sustainable commuting
- Safer biking and walking infrastructure
- More frequent and reliable bus service
- Guaranteed ride home programs
""")

# ===============================
# 🔍 Exploratory Analysis
# ===============================

st.header("Exploratory Analysis")

st.write("""
Chi-square tests revealed significant relationships between commuting mode and demographic factors, including income, age, and remote work ability.  
Sustainable commute behaviors were more common among those with flexible schedules and higher environmental concern.
""")

# ===============================
# 🔮 Predictive Modeling
# ===============================

st.header("Predictive Modeling")

st.write("""
Predictive models (Logistic Regression, Random Forest, XGBoost) were developed to predict interest in a sustainable commuting app.
Random Forest achieved the best accuracy (~50%).

Top predictors included:
- Current sustainable commuting behavior (e.g., biking, walking)
- Commute stress
- Incentive responsiveness
- Income level
- Environmental priority
""")

# ===============================
# 🏁 Conclusion
# ===============================

st.header("Conclusion")

st.write("""
Missoulians show strong willingness to shift commuting behavior under the right conditions.  
However, infrastructure improvements, flexible policies, and incentive programs are necessary to drive meaningful change.
""")

# ===============================
# 🎯 Recommendations
# ===============================

st.header("Recommendations")

st.write("""
- Expand protected bike lanes and walking infrastructure.
- Improve bus service frequency and hours.
- Launch commuting incentive programs with cash or prize rewards.
- Support remote work and flexible scheduling policies.
""")

# ===============================
# ⚠️ Study Limitations
# ===============================

st.header("Study Limitations")

st.write("""
- Survey results may be biased due to self-selection.
- Behavioral intent to use a commuting app may not translate directly to actual commuting behavior changes.
""")

# ===============================
# 🎉 Thank You!
# ===============================

st.write("""
🚲🚶‍♂️🚌 Thank you for traveling across Missoula's commuting landscape!
""")
