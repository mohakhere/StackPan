# import necessary libraries
import requests
import json

# Define ERP API endpoints and credentials
ERP_BASE_URL = "https://your-erp-api-url.com"
ERP_API_KEY = "your_api_key"
ERP_API_SECRET = "your_api_secret"

# Function to authenticate with the ERP API
def authenticate():
    auth_url = f"{ERP_BASE_URL}/auth"
    auth_data = {
        "api_key": ERP_API_KEY,
        "api_secret": ERP_API_SECRET
    }

    response = requests.post(auth_url, data=auth_data)
    if response.status_code == 200:
        auth_token = response.json().get("token")
        return auth_token
    else:
        raise Exception(f"Authentication failed. Status code: {response.status_code}, Response: {response.text}")

# Function to make API requests to ERP
def erp_api_request(endpoint, method="GET", data=None):
    url = f"{ERP_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {authenticate()}",
        "Content-Type": "application/json"
    }

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    else:
        raise Exception(f"Unsupported HTTP method: {method}")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ERP API request failed. Status code: {response.status_code}, Response: {response.text}")

# Example: Get list of customers from ERP
def get_customers():
    endpoint = "customers"
    customers = erp_api_request(endpoint)
    return customers

# Example: Create a new order in ERP
def create_order(order_data):
    endpoint = "orders"
    response = erp_api_request(endpoint, method="POST", data=order_data)
    return response

