from langchain.prompts import PromptTemplate
#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

from icebreaker.output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser
from decouple import config
import openai


openai.api_key = config('api_key')

llm = ChatOpenAI(openai_api_key="api_key", temperature=0, model_name="gpt-3.5-turbo")
llm_creative = ChatOpenAI(openai_api_key="api_key", temperature=1, model_name="gpt-3.5-turbo")


def get_summary_chain() -> LLMChain:
    summary_template = """
         given the information about a person from linkedin {information}, and I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
    """
    # summary_template = """
    #      given the information about a person from linkedin {information}, and twitter posts {twitter_posts} I want you to create:
    #      1. a short summary
    #      2. two interesting facts about them
    #      \n{format_instructions}
    # """

    summary_prompt_template = PromptTemplate(
        #input_variables=["information", "twitter_posts"],
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
            
        },
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_interests_chain() -> LLMChain:
    interesting_facts_template = """
         given the information about a person from linkedin {information}, I want you to create:
         3 topics that might interest them
        \n{format_instructions}
    """
    # interesting_facts_template = """
    #      given the information about a person from linkedin {information}, and twitter posts {twitter_posts} I want you to create:
    #      3 topics that might interest them
    #     \n{format_instructions}
    # """

    interesting_facts_prompt_template = PromptTemplate(
        #input_variables=["information", "twitter_posts"],
        input_variables=["information"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm, prompt=interesting_facts_prompt_template)


def get_ice_breaker_chain() -> LLMChain:
    # ice_breaker_template = """
    #      given the information about a person from linkedin {information}, and twitter posts {twitter_posts} I want you to create:
    #      2 creative Ice breakers with them that are derived from their activity on Linkedin and twitter, preferably on latest tweets
    #     \n{format_instructions}
    #  """
    ice_breaker_template = """
         given the information about a person from linkedin {information},I want you to create:
         2 creative Ice breakers with them that are derived from their activity on Linkedin and twitter, preferably on latest tweets
        \n{format_instructions}
    """

    ice_breaker_prompt_template = PromptTemplate(
        #input_variables=["information", "twitter_posts"],
        input_variables=["information"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm_creative, prompt=ice_breaker_prompt_template)
 
