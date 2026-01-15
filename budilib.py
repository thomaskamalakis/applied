import requests
import os
from dotenv import load_dotenv

# Load values for .env file
load_dotenv()

# Load system variables
KEY = os.getenv('KEY')
TABLE_ID = os.getenv('TABLE_ID')
SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT = os.getenv('SERVER_PORT')
APP_ID = os.getenv('APP_ID')


def read_table_data(server_ip = SERVER_IP,
                    server_port = SERVER_PORT,
                    api_key = KEY,
                    table_id = TABLE_ID,
                    app_id = APP_ID):
    """
    Read data from budibase table using the public API
    
    :param server_ip: IP address (or domain name) of the server
    :param server_port: Port of the server
    :param api_key: The API key used for authorization
    :param table_id: The table id of the table
    :param app_id: The app id
    """

    # URL endpoint
    URL = f"http://{server_ip}:{server_port}/api/public/v1/tables/{table_id}/rows/search"

    # Headers for the request
    headers = {
        "accept": "application/json",
        "x-budibase-app-id": app_id,
        "content-type": "application/json",
        "x-budibase-api-key": api_key
    }

    # Get data from the server
    response = requests.post(URL, headers=headers)

    # Parse data as a Python dictionary
    data = response.json()['data']

    return data

