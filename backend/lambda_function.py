import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')  # NewsAPI key from environment variable
NEWS_API_URL = f"https://newsapi.org/v2/everything?q=media&apiKey={NEWS_API_KEY}"

def lambda_handler(event, context):
    try:
        response = requests.get(NEWS_API_URL)
        data = response.json()

        # Extract the top 5 headlines
        headlines = [article['title'] for article in data.get('articles', [])][:5]
        print(headlines)

        return {
            'statusCode': 200,
            'body': json.dumps({'headlines': headlines})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
