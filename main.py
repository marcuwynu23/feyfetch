
import json
import requests
import os

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def colorize(text, color):
    return f"{color}{text}{RESET}"


def execute_requests_from_json(json_file):
    with open(json_file, 'r') as file:
        try:
            request_data = json.load(file)
            name = request_data['name']
            print(f"Executing requests for: {name}")

            headers = request_data.get('headers', {})
            urls = request_data.get('urls', [])

            for url_info in urls:
                url = url_info['url']
                method = url_info.get('method', 'GET')
                body = url_info.get('body', None)

                if method == 'GET':
                    response = requests.get(url, headers=headers)
                elif method == 'POST':
                    response = requests.post(url, json=body, headers=headers)
                elif method == 'UPDATE':
                    response = requests.put(url, json=body, headers=headers)
                elif method == 'DELETE':
                    response = requests.delete(url, json=body, headers=headers)
                # Add support for other HTTP methods as needed

                status_code = response.status_code
                if 200 <= status_code < 300:
                    color_status = colorize(status_code, GREEN)
                else:
                    color_status = colorize(status_code, RED)

                print(f"Request to {url} ({method}): {color_status}")
                if response.ok:
                    # make directory if it doesn't exist request
                    if not os.path.exists('requests'):
                        os.makedirs('requests')
                    if response.text:
                        # write the response to a file
                        with open("requests/output.txt", 'w', encoding='utf-8') as f:
                            f.write(response.text)
                    elif response.json():
                        # write the response to a file
                        with open("requests/output.json", 'w', encoding='utf-8') as f:
                            json.dump(response.json(), f)

                    else:
                        print("No content")
                else:
                    print(
                        f"{colorize('Request failed with status code', RED)} {color_status}")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e.msg}")


if __name__ == "__main__":
    JSON_FILE = "requests/requests.json"
    execute_requests_from_json(JSON_FILE)
