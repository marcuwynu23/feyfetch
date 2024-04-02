<div align="center">

# FeyFetch

[![GitHub license](https://img.shields.io/github/license/marcuwynu23/feyfetch)](https://github.com/marcuwynu23/feyfetch/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/marcuwynu23/feyfetch)](https://github.com/marcuwynu23/feyfetch/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/marcuwynu23/feyfetch)](https://github.com/marcuwynu23/feyfetch/issues)

</div>

FeyFetch is an automated testing tool crafted for efficient testing of REST API routes. It simplifies the process of testing API endpoints, ensuring reliability and performance with ease.

## Features

- **Automated Testing**: FeyFetch automates the testing of REST API routes, reducing manual effort and ensuring consistent testing procedures.
- **Configurable Headers**: Easily configure common headers to be included in all API requests for uniformity and ease of management.
- **Flexible Request Handling**: Support for various HTTP methods (GET, POST, PUT, DELETE, etc.) and optional request bodies allows for comprehensive testing of API endpoints.
- **Directory-Based Organization**: FeyFetch reads API requests from a specified directory, enabling easy organization and management of test cases.
- **Whimsical Charm**: With its playful name and mystical inspiration, FeyFetch adds a touch of whimsy to your testing endeavors.

## Installation

To install FeyFetch, simply clone this repository:

```bash
git clone https://github.com/marcuwynu23/feyfetch.git
```

## Usage

1. Create a `requests.json`or any name for your requests file in your `requests` directory with the following structure:

```json
{
  "name": "Application API Requests",
  "root": "http://localhost:9000/api",
  "headers": {
    "Content-Type": "application/json"
  },
  "routes": [
    {
      "path": "/auth/login",
      "method": "GET"
    },
    {
      "path": "/auth/login",
      "method": "POST",
      "body": {
        "email": "admin@admin.com",
        "password": "admin"
      }
    },
    {
      "path": "/auth/register",
      "method": "POST",
      "body": {
        "email": "admin@admin.com",
        "password": "admin",
        "role": "admin"
      }
    },
    {
      "path": "/auth/recovery",
      "method": "POST",
      "body": {
        "email": "admin@admin.com"
      }
    },
    {
      "path": "/auth/reset",
      "method": "POST",
      "body": {
        "email": "admin@admin.com",
        "password": "admin",
        "token": "123"
      }
    },
    {
      "path": "/auth/logout",
      "method": "GET"
    },
    {
      "path": "/users",
      "method": "GET"
    }
  ]
}
```

2. Run FeyFetch by executing the main script and providing the path to the directory containing your requests configuration file:

```bash
fey <filename>
```

3. FeyFetch will automate the testing of your API routes based on the requests defined in request json file for example `requests.json` inside the requests folder, providing insights into the functionality and performance of your endpoints.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve FeyFetch and make it even more magical.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
