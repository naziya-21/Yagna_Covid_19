import streamlit as st
import pandas as pd

# Configure the app
st.set_page_config(page_title="COVID-19 Tracking and Info App")
st.sidebar.header("COVID-19 Tracker")
st.sidebar.write("Stay updated with real-time COVID-19 data.")

# Load data
@st.cache_data
def load_data():
    # Replace with the path to your CSV file
    url = "C:/Users/91833/OneDrive/Desktop/country_wise_latest.csv"  # Provide the actual URL or file path
    data = pd.read_csv(url)
    return data

# Load the COVID-19 data
covid_data = load_data()

# Display the app header
st.header("COVID-19 Tracking and Information")
st.subheader("Real-time updates on COVID-19 cases, vaccination, and hospital resources.")

# Display COVID-19 cases
if st.checkbox("Show COVID-19 Case Data"):
    st.write("### Global and Regional COVID-19 Case Numbers")
    st.write(covid_data)

# Filter data by region
selected_region = st.selectbox("Select a Region", covid_data["region"].unique())
filtered_data = covid_data[covid_data["region"] == selected_region]

# Display region-specific data
st.write(f"### COVID-19 Statistics for {selected_region}")
st.write(filtered_data)

# Display vaccination status
if st.checkbox("Show Vaccination Status"):
    st.write("### Vaccination Progress")
    st.write(filtered_data[["region", "doses_given", "percent_vaccinated"]])

# Display hospital resources
if st.checkbox("Show Hospital Resources"):
    st.write("### Hospital Resources Availability")
    st.write(filtered_data[["region", "beds", "ventilators", "icu_capacity"]])

# Footer
st.write("Stay safe and stay informed with the COVID-19 Tracker.")
