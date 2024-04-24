import os
import json
import requests
from requests.auth import HTTPBasicAuth

# Credentials
username = 'STUDENT96'
password = '1kin1xBo+W6lG4Kobo49dueAZPSixbMstbPhEh7aVQg='

# API URLs
api_urls = [
    'http://erp.foi.hr:19148/BC_P/api/v2.0/items',
    'http://erp.foi.hr:19148/BC_P/api/v2.0/customers',
    'http://erp.foi.hr:19148/BC_P/api/v2.0/vendors',
    'http://erp.foi.hr:19148/BC_P/api/v2.0/salesInvoices',
    # Add more URLs as needed
]

# Initialize an empty dictionary to store all the data
all_data = {}

# Function to retrieve data from API
def get_data(api_url):
    try:
        # Make the request with HTTP Basic Authentication
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Process the retrieved data as needed
            # print(f"Data from {api_url}: {data}")

            # Add the data to the all_data dictionary
            all_data[api_url] = data

            # Create a filename from the API URL
            filename = 'files/' + api_url.split('/')[-1] + '.json'

            # Write the data to a JSON file
            with open(filename, 'w') as f:
                json.dump(data, f)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Loop through API URLs and retrieve data
for url in api_urls:
    get_data(url)

# Write all the data to a single JSON file
with open('files/all_data.json', 'w') as f:
    json.dump(all_data, f)