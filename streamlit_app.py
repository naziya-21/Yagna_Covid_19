import streamlit as st
import requests
import json

# API base URL
API_URL = "http://127.0.0.1:5000/covid"

# Function to display COVID data
def display_covid_data():
    st.header("COVID-19 Data")
    
    # Fetch current COVID-19 case numbers by region
    response = requests.get(f"{API_URL}/cases")
    if response.status_code == 200:
        cases_data = response.json()
        st.json(cases_data)
    else:
        st.error("Failed to retrieve COVID-19 data.")

    # Update COVID-19 Data
    st.subheader("Update COVID-19 Data")
    region = st.text_input("Enter region (e.g., 'USA'):")
    new_data = st.text_area("Enter new data as JSON (e.g., {'active_cases': 51000, 'recoveries': 46000, 'deaths': 5200})")
    
    if st.button("Update Data"):
        try:
            updates = json.loads(new_data)
            payload = {"region": region, "updates": updates}
            update_response = requests.post(f"{API_URL}/cases/update", json=payload)
            if update_response.status_code == 200:
                st.success("COVID-19 data updated successfully!")
            else:
                st.error(update_response.json().get("error", "Failed to update data."))
        except json.JSONDecodeError:
            st.error("Invalid JSON format.")

# Function to display vaccination status
def display_vaccination_status():
    st.header("Vaccination Status")
    
    # Fetch vaccination status
    response = requests.get(f"{API_URL}/vaccination-status")
    if response.status_code == 200:
        vaccination_data = response.json()
        st.json(vaccination_data)
    else:
        st.error("Failed to retrieve vaccination data.")

# Function to display hospital resources
def display_hospital_resources():
    st.header("Hospital Resources")
    
    # Fetch hospital resources
    response = requests.get(f"{API_URL}/hospitals/resources")
    if response.status_code == 200:
        resources_data = response.json()
        st.json(resources_data)
    else:
        st.error("Failed to retrieve hospital resources.")
    
    # Update Hospital Resources
    st.subheader("Update Hospital Resources")
    new_hospital_data = st.text_area("Enter new hospital resources as JSON (e.g., {'available_beds': 250})")
    
    if st.button("Update Hospital Resources"):
        try:
            updates = json.loads(new_hospital_data)
            update_response = requests.post(f"{API_URL}/hospitals/resources/update", json=updates)
            if update_response.status_code == 200:
                st.success("Hospital resources updated successfully!")
            else:
                st.error(update_response.json().get("error", "Failed to update hospital resources."))
        except json.JSONDecodeError:
            st.error("Invalid JSON format.")

# Main app layout
st.title("Healthcare Data Dashboard")
display_covid_data()
display_vaccination_status()
display_hospital_resources()
