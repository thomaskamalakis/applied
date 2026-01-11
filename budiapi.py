import requests

# Replace key value with the one obtained by the budibase UI as described in the docs 
KEY = '945837439453845849ig7487486847669486849684986498682itorituriy48859485498594594854'

# Replace the IP address with your own and tableId with the id of the table you wish to download (see also the budibase documentation)
TABLE_ID = 'ta_fdbe12ba3230476197ac08a38ee6df61'
SERVER_IP = '10.100.52.60'
SERVER_PORT = 10000
APP_ID = 'app_cc3b874204d14304afbdd77f62d8eafb'

# URL endpoint
URL = f"http://{SERVER_IP}:{SERVER_PORT}/api/public/v1/tables/{TABLE_ID}/rows/search"

# Headers for the request
headers = {
    "accept": "application/json",
    "x-budibase-app-id": APP_ID,
    "content-type": "application/json",
    "x-budibase-api-key": KEY
}

# Get data from the server
response = requests.post(URL, headers=headers)

# Parse data as a Python dictionary
data = response.json()['data']

# Print specific information about each table row
for element in data:
    print(element['given_name'],element['surname'])