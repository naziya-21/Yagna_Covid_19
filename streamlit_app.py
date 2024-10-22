import streamlit as st
import json

# Function to display API request and simulated response
def display_api_output(url, method, headers, body, status_code, response_body):
    st.write("### Request")
    st.write(f"**URL:** {url}")
    st.write(f"**Method:** {method}")
    if headers:
        st.write(f"**Headers:** {json.dumps(headers, indent=2)}")
    if body:
        st.write(f"**Body:** {json.dumps(body, indent=2)}")
    
    # Simulated response
    st.write("### Response")
    st.write(f"**Status Code:** {status_code}")
    st.write(f"**Body:** {json.dumps(response_body, indent=2)}")

# Title of the app
st.title("COVID-19 Tracking API Outputs")

# Screenshot 1: GET /covid/cases
st.header("Screenshot 1: GET /covid/cases")
url1 = "https://your-api-endpoint.com/covid/cases"
method1 = "GET"
headers1 = {"Authorization": "Bearer your_token"}  # Example header
body1 = None
response_body1 = {
    "region": "India",
    "totalCases": 100000,
    "activeCases": 50000,
    "recovered": 40000,
    "deaths": 10000
}
display_api_output(url1, method1, headers1, body1, 200, response_body1)

# Screenshot 2: GET /covid/cases/{region}
st.header("Screenshot 2: GET /covid/cases/{region}")
url2 = "https://your-api-endpoint.com/covid/cases/India"
method2 = "GET"
headers2 = {"Authorization": "Bearer your_token"}  # Example header
body2 = None
response_body2 = {
    "region": "India",
    "totalCases": 100000,
    "activeCases": 50000,
    "recovered": 40000,
    "deaths": 10000,
    "vaccinationProgress": {
        "totalDoses": 1000000,
        "percentageVaccinated": 20
    },
    "hospitalResources": {
        "beds": 1000,
        "ventilators": 200,
        "icuCapacity": 50
    }
}
display_api_output(url2, method2, headers2, body2, 200, response_body2)

# Screenshot 3: POST /covid/cases/update
st.header("Screenshot 3: POST /covid/cases/update")
url3 = "https://your-api-endpoint.com/covid/cases/update"
method3 = "POST"
headers3 = {"Authorization": "Bearer your_token"}  # Example header
body3 = {
    "region": "India",
    "newCases": 1000
}
response_body3 = {
    "message": "Case count updated successfully"
}
display_api_output(url3, method3, headers3, body3, 200, response_body3)
