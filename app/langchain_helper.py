import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
#from dotenv import load_dotenv
#load_dotenv()
class BabyNameGenerator:
    def __init__(self,api_key):
        self.llm = OpenAI(api_key=api_key,temperature=0.8)

    def generate_baby_names(self, number_of_names, country, gender):
        prompt_template_baby_name = PromptTemplate(
            input_variables=['number_of_names', 'gender', 'country'],
            template='Suggest baby name {number_of_names} for a {gender} child from {country}'
        )
        baby_name_chain = LLMChain(llm=self.llm, prompt=prompt_template_baby_name, output_key='baby_names')

        prompt_template_baby_name_meaning = PromptTemplate(
            input_variables=['baby_names'],
            template='Tell me the meaning of these {baby_names} in English'
        )
        baby_name_meaning_chain = LLMChain(llm=self.llm, prompt=prompt_template_baby_name_meaning,
                                           output_key='baby_name_meanings')

        baby_name_meaning_chain = SequentialChain(chains=[baby_name_chain, baby_name_meaning_chain],
                                                 input_variables=['number_of_names', 'gender', 'country'],
                                                 output_variables=['baby_names', 'baby_name_meanings'])
        response = baby_name_meaning_chain({'number_of_names': number_of_names, 'gender': gender, 'country': country})

        return response

