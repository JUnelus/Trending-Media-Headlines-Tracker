# Trending Media Headlines Tracker

This project demonstrates a cloud-native serverless application built using AWS Lambda, API Gateway, Python, and JavaScript. It fetches live media and entertainment headlines using the NewsAPI and displays them in a simple frontend.

## Features
- Serverless backend (AWS Lambda)
- REST API for fetching trending news headlines
- JavaScript-based frontend for displaying the headlines
- Automated unit testing for the Lambda function
- CI/CD pipeline for automated deployment using GitHub Actions

## Technologies Used
- **Backend**: Python, AWS Lambda, API Gateway
- **Frontend**: HTML, JavaScript
- **CI/CD**: GitHub Actions, AWS SAM
- **Testing**: PyTest

## Setup Instructions

### Requirements
- AWS Account
- Python 3.11
- NewsAPI key (Get from https://newsapi.org/)

### Steps to Deploy

1. Clone the repository.
2. Navigate to the `backend/` directory and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the AWS Lambda function and API Gateway using AWS SAM:
    ```bash
    sam build
    sam deploy --guided
    ```
4. Deploy the frontend (optional):
    - Host the frontend files (`index.html`, `script.js`, `style.css`) on an S3 bucket or use a local web server.

### Running Tests
To run unit tests locally for the Lambda function, execute:
```bash
pytest backend/test_lambda_function.py
```
