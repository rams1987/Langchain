from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from linkedin_scrapping import linkedin
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser


def ice_breaker(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")

    summary_template = """
            given the information {information} about a person from I want you to create:
            1. a short summary
            2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variable={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = linkedin.scrap_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    result = chain.run(information=linkedin_data)
    return result


if __name__ == "__main__":

    print("Hello LangChain")
    name = "Eden Marco"
    result = ice_breaker(name)
    print(result)
