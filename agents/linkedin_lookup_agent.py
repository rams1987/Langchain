from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import Tool, initialize_agent, AgentType


def lookup(name: str) -> str:

    """Initialize llm and template"""
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
    template = "Given the full name {name_of_person} I want to get the LinkedIn profile URL. Your answer should contain only the URL"

    """Initialize Tools"""
    tools_for_agents = [
        Tool(
            name="Crawl Google for Linkedin page",
            func="?",
            description="Useful when you want to get Linkedin url of a person",
        )
    ]

    """Initialize agent"""
    agent = initialize_agent(
        tools=tools_for_agents,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return "linkedin_profile_url"
