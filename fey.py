import json
from token import ENCODING
import requests
import os
import sys


# ANSI color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Constants
REQUESTS_DIR = "requests"
RECORDS_DIR = "requests/records"
LOGS_DIR = "requests/logs"
ENCODING = "utf-8"


def colorize(text, color):
    return f"{color}{text}{RESET}"


def execute_requests_from_json(json_filename):
    try:
        with open(f'{REQUESTS_DIR}/{json_filename}.json', 'r') as file:
            request_data = json.load(file)
            name = request_data['name']
            root = request_data['root']
            print(f"Executing requests for: {name}")

            headers = request_data.get('headers', {})
            routes = request_data.get('routes', [])
            # Check if the root URL responds
            try:
                root_response = requests.head(root)
                if not root_response.ok:
                    pass
            except requests.ConnectionError:
                print(
                    f"Error: Failed to connect to {root}. Is the server running?")
                sys.exit(1)

            try:
                for route_info in routes:
                    path = route_info['path']
                    method = route_info.get('method', 'GET')
                    body = route_info.get('body', None)

                    url = root + path

                    try:
                        if method == 'GET':
                            response = requests.get(url, headers=headers)
                        elif method == 'POST':
                            response = requests.post(
                                url, json=body, headers=headers)
                        elif method == 'UPDATE':
                            response = requests.put(
                                url, json=body, headers=headers)
                        elif method == 'DELETE':
                            response = requests.delete(
                                url, json=body, headers=headers)
                        # Add support for other HTTP methods as needed

                        status_code = response.status_code
                        if 200 <= status_code < 300:
                            color_status = colorize(status_code, GREEN)
                        else:
                            color_status = colorize(status_code, RED)

                        print(
                            f"Request to {url} ({method}): {color_status}")
                        if response.ok:
                            # make directory if it doesn't exist for requests
                            if not os.path.exists(RECORDS_DIR):
                                os.makedirs(RECORDS_DIR)

                            # write the response to a file if there's content
                            if response.text:
                                RECORD_TEXT = f"{RECORDS_DIR}/output_{method.lower()}_{path.replace('/', '_')}.txt"
                                with open(RECORD_TEXT, 'w', encoding=ENCODING) as f:
                                    f.write(response.text)
                            elif response.json():
                                RECORD_JSON = f"{RECORDS_DIR}/output_{method.lower()}_{path.replace('/', '_')}.json"
                                with open(RECORD_JSON, 'w', encoding=ENCODING) as f:
                                    json.dump(response.json(), f)
                            else:
                                print("No content")
                        else:
                            # make directory if it doesn't exist for logs
                            if not os.path.exists(LOGS_DIR):
                                os.makedirs(LOGS_DIR)
                            # write the response to a file if there's content
                            if response.text:
                                LOG_TEXT = f"{LOGS_DIR}/log_{method.lower()}_{path.replace('/', '_')}.txt"
                                with open(LOG_TEXT, 'w', encoding=ENCODING) as f:
                                    f.write(response.text)
                            elif response.json():
                                LOG_JSON = f"{LOGS_DIR}/log_{method.lower()}_{path.replace('/', '_')}.json"
                                with open(LOG_JSON, 'w', encoding=ENCODING) as f:
                                    json.dump(response.json(), f)
                            else:
                                print("No content")

                    except requests.ConnectionError:
                        print(
                            f"Error: Failed to connect to {url}. Is the server running?")
                        sys.exit(1)
                    except requests.Timeout:
                        print(f"Error: Request to {url} timed out")
                        sys.exit(1)

            except requests.ConnectionError:
                print(
                    f"Error: Failed to connect to {root}. Is the server running?")
                sys.exit(1)

    except FileNotFoundError:
        print(
            f"Error: File '{json_filename}.json' not found in 'requests' directory")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fey <request-filename>")
        sys.exit(1)
    JSON_FILENAME = sys.argv[1]
    execute_requests_from_json(JSON_FILENAME)
