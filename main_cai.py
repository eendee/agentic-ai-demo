import os
from crewai import Agent, Task, Crew

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from cai_tools import fetch_weather
from cai_tools import publish
import app_config


# Load environment variables from .env file
load_dotenv()



# Create a ChatOpenAI instance
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = os.getenv('OPENAI_MODEL_NAME')
llm = ChatOpenAI(model_name=os.getenv('OPENAI_MODEL_NAME'), temperature=0)



weather_agent = Agent(
    role='Weather Agent',
    goal='Get weather information for a given city',
    backstory=app_config.WEATHER_AGENT,
    verbose=True,
    allow_delegation=False,
    tools=[fetch_weather],
    llm=llm
)

tour_agent = Agent(
    role='Tour Agent',
    goal='Create a tour plan for a given city',
    backstory=app_config.TOUR_AGENT,
    verbose=True,
    allow_delegation=False,
    llm=llm
)


writer_agent = Agent(
    role='Creative Writer Agent',
    goal='Rewrite content to be engagin, and come up with a catchy title for it',
    backstory=app_config.PUBLISH_AGENT,
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[publish],
)

city = "Berlin"
weather_task = Task(
    description=app_config.WEATHER_TASK,
    agent=weather_agent,
    expected_output='Gets weather information for a given city',
    verbose=True,
) 

tour_planner_task = Task(
    description=app_config.TOUR_TASK,
    agent=tour_agent,
    expected_output='Gets ideas for what to do in a given city depending on the weather conditions',
    verbose=True,
)

editor_task = Task(
    description=app_config.PUBLISH_TASK,
    agent=writer_agent,
    expected_output='Rewrites the tour plan for a given city to be engagin, and come up with a catchy title for it. After that, publish them to medium.',
    verbose=True,
)


crew = Crew(
    agents=[weather_agent, tour_agent, writer_agent,],
    tasks=[weather_task, tour_planner_task, editor_task],
    verbose=True,
)


if __name__ == '__main__':
    print("## Welcome to city tour planner")
    result = crew.kickoff()
    print(result)
