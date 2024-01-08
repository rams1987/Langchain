from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import tweepy


def get_twitter_data():
    api_key = "2xZ8EHsjKO0IbtHqXU42yPqJh"
    api_key_secret = "DKHFL5Xn73QWlBZueojHQ43NZaZlnffvMbOKmu0z90ZgyFFKm5"
    Authentication_Bearer_token = "AAAAAAAAAAAAAAAAAAAAANqhrgEAAAAASc%2BU38TUxZMgsL4x%2FbrTsrP%2B3JQ%3DIURGM1mPq9gTSGY1BNQ09iZ5IdD4t5D0rK4Dq3s2l0uJOAyK8V"
    access_token = "300968619-2sHE09vGeRdbtiH9snTVoGe3czgORgvU1ED4FBJk"
    access_token_secret = "UnTlmbZLmUO2O4zGNxYln8aixtsKr6KItKCw4JKxbuDau"

    client_id = "UHpqWEJMQjR6TlpJZC1VQTJJVW86MTpjaQ"
    client_secret = "1L_vAp4ot3rEGPGn4K5gexnq5yUpxM2nkkMIv1rvLL2KFSu8gn"

    user_id = "300968619"
    user_name = "ramasamy1986"

    # auth = tweepy.OAuthHandler(api_key, api_key_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    # user1 = api.get_user(user_id=user_id)

    auth = tweepy.OAuth1UserHandler(
        api_key, api_key_secret, access_token, access_token_secret
    )
    apiv1 = tweepy.API(auth)

    apiv1.get_user(user_id=user_id)

    #    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token,
    #                          access_token_secret=access_token_secret)

    # client = tweepy.Client(bearer_token=Authentication_Bearer_token)

    query = "covid"
    response = client.search_recent_tweets(query=query)

    # tweets = client.get_user(username=user_name)

    print("User Name: " + tweets)


def modify_data_using_llm(data: str):

    template = """ given the twitter data {twitter data} make a professional description of the person
    """

    prompt_template = PromptTemplate(
        input_variables=["twitter data"], template=template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
    chain = LLMChain(llm=llm, prompt=prompt_template)



if __name__ == "__main__":
    print("LLM Based Twitter Data Processing")
    get_twitter_data()
    modify_data_using_llm()
