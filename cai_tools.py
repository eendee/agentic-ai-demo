from langchain_community.tools import tool
from tools_functions import get_weather
from  tools_functions import publish_to_medium


@tool("publish")
def publish(title:str, content:str) -> str:
    """Useful for publishing articles to medium"""
    print("CrewAI: Executing publish")
    return publish_to_medium(title, content)

@tool("fetch_weather")
def fetch_weather(city: str) -> dict:
   """Useful for finding information the weather of a given city for the next 7 days"""
   return get_weather(city)