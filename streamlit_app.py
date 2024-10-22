import streamlit as st
import pandas as pd

# Function to create a DataFrame for displaying in table format
def create_request_response_table(url, method, headers, body, status_code, response_body):
    data = {
        "Field": ["URL", "Method", "Headers", "Body", "Status Code", "Response Body"],
        "Value": [
            url,
            method,
            str(headers) if headers else "None",
            str(body) if body else "None",
            status_code,
            str(response_body)
        ]
    }
    return pd.DataFrame(data)

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
table1 = create_request_response_table(url1, method1, headers1, body1, 200, response_body1)
st.table(table1)

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
table2 = create_request_response_table(url2, method2, headers2, body2, 200, response_body2)
st.table(table2)

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
table3 = create_request_response_table(url3, method3, headers3, body3, 200, response_body3)
st.table(table3)
