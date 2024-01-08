from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


quixxi_data = "<p>An Android Activity provides the window in which the app draws its UI. This window typically fills the screen, but may be smaller than the screen and float on top of other windows. Generally, one Activity implements one screen in an app<br/> <br/> Most apps contain multiple screens, which means they comprise multiple Activities. Typically one of the activities in the app is specified as the Main Activity, which is the first screen to appear when the user launches the app<br/> <br/> Developers can switch from one Activity to another using Components known as Intents that can also pass in additional values to the subsequent screen. However if there are not enough security measures an attacker might launch directly the second Activity bypassing the first one</p>"
input_code = ""

summary_template = """
           given the information {information} about the issue in the mobile app can you provide
           1. Severity of the problem and its impact
           2. Top 3 fixes for the problem
           3. Sample code to fix the problem if any
           4. Get the CVSS score
           5. find the issue in the given {input_code} 
           6. where to insert the fix/code in the given {input_code}
       """

summary_prompt_template = PromptTemplate(
    input_variables=["information",], template=summary_template,
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

result = chain.run(information=quixxi_data)

print(result)
