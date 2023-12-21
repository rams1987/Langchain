from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from linkedin_scrapping import linkedin
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the wealthiest person in the world, with an estimated net worth of US$222 billion as of December 2023, according to the Bloomberg Billionaires Index, and $244 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6] He is the founder, chairman, CEO, and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation.]
A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.
"""

if __name__ == "__main__":

    print("Hello LangChain")

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = linkedin.scrap_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    print(chain.run(information=linkedin_data))
