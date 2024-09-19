from tools_functions import get_weather
from  tools_functions import publish_to_medium


def publish(title:str, content:str) -> str:
    print("AutoGen Executing publish")
    return publish_to_medium(title, content)

def fetch_weather(city: str) -> dict:
    return get_weather(city)