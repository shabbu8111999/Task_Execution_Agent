

# This sets up the LangChain agent with the tools and executes the plan.


from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.chat_models import ChatOpenAI
from agent.base_tools import scan_directory, delete_log_files, rename_drafts_to_final
import os
from dotenv import load_dotenv


load_dotenv()


def execute_task(task_description: str) -> str:
    llm = ChatOpenAI(temperature=0)

    tools = [scan_directory, delete_log_files, rename_drafts_to_final]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    result = agent.run(task_description)
    return result