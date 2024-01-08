from langchain.agents import tool
from langchain import PromptTemplate
from langchain.tools.render import render_text_description
from langchain.chat_models import ChatOpenAI



@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct LangChain")
    tools = [get_text_length]
    print(get_text_length(text="DOG"))

    template = """
    
    Answer the following question. You have access for the following tools: 
    {tools}
    
    use the following format: 
    
    Question: the input question you must answer
    Thought: you should always think about what to do 
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action (this Thought/Action/Action Input/Observation can be repeat N time)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question 
    
    Begin! 
    
    Question: {input}
    Thought:     
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=".".join([t.name for t in tools]),
    )

    llm = ChatOpenAI(temperature=0, stop=["\nObservation"], model_name="gpt-3.5-turbo-1106")
    agent = {"input": lambda x: x["input"]}| prompt | llm
