import streamlit as st
import requests

# dockerized host
url = 'http://fastapi:8080/predict'

# what choices are there?
age_choices = ['Under 15 yrs', '15 to 17 yrs', '18 to 19 yrs', '20 to 24 yrs', '25 to 29 yrs', '30 to 34 yrs', '35 to 39 yrs', '40 to 44 yrs', '45 to 49 yrs', '50+ yrs']
race_ethnicity_choices = ['White, non-Hispanic', 'Black, non-Hispanic', 'Hispanic (of any race)', 'Asian, non-Hispanic']
birth_choices = ['None', 'One, Two, Three or More']
tobacco_choices = ['Yes', 'No']
care_choices = ['Inadequate', 'Adequate']

st.title("Template Prediction")
with st.form(key='my_form'):
    age_input = st.selectbox('Mother\'s Age', age_choices)
    race_input = st.selectbox('Mother\'s Race/Ethnicity', race_ethnicity_choices)
    birth_input = st.selectbox('Previous Births', birth_choices)
    tobacco_input = st.selectbox('Tobacco Use During Pregnancy?', age_choices)
    care_input = st.selectbox('Access to Adequte Prenatal Care?', care_choices)
    submit_button = st.form_submit_button(label='Submit')

# make a prediction
with st.spinner(text='In progress'):
    response = requests.post(url, json = {
        "age_group": age_input,
        "reported_race_ethnicity": race_input,
        "previous_births": birth_input,
        "tobacco_use_during_pregnancy": tobacco_input,
        "adequate_prenatal_care": care_input
    })    
    st.success(response.text)

