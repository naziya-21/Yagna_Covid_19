import streamlit as st
import pandas as pd
import requests

st.title("COVID-19 Tracking and Information API")

# Define base API URL
BASE_API_URL = "http://your-flask-api-url"

# Function to get COVID-19 cases by region
def get_covid_cases(region=None):
    if region:
        response = requests.get(f"{BASE_API_URL}/covid/cases/{region}")
    else:
        response = requests.get(f"{BASE_API_URL}/covid/cases")
    return response.json()

# Function to get vaccination status
def get_vaccination_status():
    response = requests.get(f"{BASE_API_URL}/covid/vaccination-status")
    return response.json()

# Function to get hospital resources
def get_hospital_resources():
    response = requests.get(f"{BASE_API_URL}/covid/hospitals/resources")
    return response.json()

# Streamlit interface
st.header("COVID-19 Data")
region = st.text_input("Enter region (e.g., country, state, city):")
if st.button("Get COVID-19 Cases"):
    data = get_covid_cases(region)
    st.write(data)

st.header("Vaccination Status")
if st.button("Get Vaccination Status"):
    vaccination_data = get_vaccination_status()
    st.write(vaccination_data)

st.header("Hospital Resources")
if st.button("Get Hospital Resources"):
    hospital_data = get_hospital_resources()
    st.write(hospital_data)
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
covid_data = {
    "global": {"cases": 1000000, "recoveries": 800000, "deaths": 50000},
    "usa": {"cases": 500000, "recoveries": 400000, "deaths": 20000},
}

vaccination_data = {
    "global": {"doses_given": 500000000, "percent_vaccinated": 60},
    "usa": {"doses_given": 200000000, "percent_vaccinated": 70},
}

hospital_resources = {
    "global": {"beds": 100000, "ventilators": 10000, "icu_capacity": 8000},
    "usa": {"beds": 50000, "ventilators": 5000, "icu_capacity": 4000},
}

# Endpoints
@app.route('/covid/cases', methods=['GET'])
def get_cases():
    return jsonify(covid_data)

@app.route('/covid/cases/<region>', methods=['GET'])
def get_cases_by_region(region):
    return jsonify(covid_data.get(region, "Region not found"))

@app.route('/covid/vaccination-status', methods=['GET'])
def get_vaccination():
    return jsonify(vaccination_data)

@app.route('/covid/hospitals/resources', methods=['GET'])
def get_hospital():
    return jsonify(hospital_resources)

if __name__ == "__main__":
    app.run(debug=True)

