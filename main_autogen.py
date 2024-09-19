import os
from dotenv import load_dotenv
from autogen import ConversableAgent, UserProxyAgent
from autogen import register_function
from autogen_tools import fetch_weather
from autogen_tools import publish
import app_config

# Load environment variables from .env file
load_dotenv()

config_list = [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]
llm_config = {
    "config_list": config_list,
    "cache_seed": 42
}


user_proxy = UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config=False
)


weather_assistant = ConversableAgent(
    name="WeatherAssistant",
    system_message=app_config.WEATHER_AGENT,
    llm_config=llm_config,
)


tour_agent = ConversableAgent(
    name="TourAgent",
    system_message=app_config.TOUR_AGENT,
    llm_config=llm_config,
)

writer_agent = ConversableAgent(
    name="WriterAgent",
    system_message=app_config.PUBLISH_AGENT,
    llm_config=llm_config,
)


register_function(
    fetch_weather,
    caller=weather_assistant, 
    executor=user_proxy,
    name="fetch_weather",
    description="""Useful for finding information the weather of a given city for the next 7 days""",
)

register_function(
    publish,
    caller=writer_agent,
    executor=user_proxy,
    name="publish",
    description="""Useful for publishing articles to medium""", 
)

city = "Berlin"
weather_task = {
                "recipient": weather_assistant,
                "message": app_config.WEATHER_TASK,
                "max_turns": 3
            }
tour_task = {
                "recipient": tour_agent,
                "message": app_config.TOUR_TASK,
                "max_turns": 3
            }
writer_task = {
                "recipient": writer_agent,
                "message": app_config.PUBLISH_TASK,
                "max_turns": 3
            }


if __name__ == "__main__":

    chat_results = user_proxy.initiate_chats(
        [weather_task,tour_task,writer_task]
    )