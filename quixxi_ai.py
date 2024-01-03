from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from linkedin_scrapping import linkedin
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser, PersonIntel

quixxi_data = "App has malware"

summary_template = """
           given the information {information} about the issue in the mobile app can you provide
           1. Severity of the problem
           2. Top 3 fixes for the problem
       """

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template,
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

result = chain.run(information=quixxi_data)

