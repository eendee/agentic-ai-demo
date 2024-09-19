import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def publish_to_medium(title:str, content:str) -> str:

    # Replace with your integration token
    headers = {
        "Authorization": f"Bearer {os.getenv('MEDIUM_API_KEY')}",
        "Content-Type": "application/json"
    }

    # Replace with your Medium user ID
    user_id = os.getenv('MEDIUM_USER_ID')

    # Article data
    data = {
        "title": title,
        "contentFormat": "markdown",  # or "html" if you prefer HTML content
        "content": content,
        "publishStatus": "draft"  # Save as a draft
    }

    try:
         # Make the request
        response = requests.post(f"https://api.medium.com/v1/users/{user_id}/posts", headers=headers, json=data)

        # Print the response from Medium
        print(response.json())
        return "success"
    except Exception as e:
        print(e)
        return "failed"



def get_weather(city: str) -> dict:

    url = f"https://api.weatherapi.com/v1/forecast.json?q={city}&days=7&key={os.getenv('WEATHER_API_KEY')}"

    payload={}
    headers = {
    'Authorization': os.getenv('WEATHER_API_TOKEN')
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    print(data)
    data = data['forecast']['forecastday']

    # We reduce the amount of data we need to process
    # We only need the date, maxtemp_c, mintemp_c, and condition
    # We also rename the condition to just 'condition' for better readability

    new_data = [
        {
            'date':d['date'], 
            'maxtemp_c':d['day']['maxtemp_c'], 
            'mintemp_c':d['day']['mintemp_c'], 
            'condition':d['day']['condition']['text']
        } for d in data
    ]
    print(new_data)

    return new_data


if __name__ == "__main__":
    print(get_weather('London'))
