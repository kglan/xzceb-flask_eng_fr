import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey ='YEdlLB3kMenhjzb1TYdsKojGu4a0Vp9RH58zAjWFfjza'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/89a17e3d-bab9-45b1-bd8d-1e1da115933e'


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text1):
    french_text = language_translator.translate( text=english_text1 , model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text1):
    english_text = language_translator.translate( text=french_text1 , model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']