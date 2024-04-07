

pip install google-search-results -q

pip install langchain openai pymysql --upgrade -q

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

import os
os.environ['OPENAI_API_KEY'] = "your generateed Key"
os.environ["SERPAPI_API_KEY"] = "your generated key"

from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase

db_user = "username"
db_password = "password"
db_host = "hostname"
db_name = "dbname"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=False)

agent_executor.run("Describe Employee related Table")

agent_executor.run("which Employee have more salary")

p=input("enter Your Query: ")
agent_executor.run(p)