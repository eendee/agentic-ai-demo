# agentic-ai-demo
This repository provides an implementation of Agentic workflow that fetches the current weather condition for a provided city, generates a tour plan given the weather conditions, and publishes the plan as an article on Medium. The workflow is implemented in both AutoGen and CrewAI.

## To Run:
-  Create a free account at http://www.weatherapi.com/ and obtain the API key for the weather tool. More details at https://www.weatherapi.com/docs/
-  Create a free Medium account (If you do not already have one), and generate an API key. More details at https://github.com/Medium/medium-api-docs.
-  Create an OpenAI API key. More details at https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key.
-  Rename `example.env` to `.env` and provide the correct values for the variables
-  Create Python Virtual Environment
-  Install Requirements `pip install -r requirements.txt`.
-  To run the AutoGen example: `python main_autogen.py`.
-  To run the CrewAI example: `python main_cai.py`.