import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('APIKEY')
URL = os.getenv('URL')
VERSION = os.getenv('VERSION')

authenticator = IAMAuthenticator(APIKEY)
lt = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
lt.set_service_url(URL)

def english_to_french(english_text):
    """
    translates english to french
    """
    if english_text is None:
        return None
    response = lt.translate(text=english_text,model_id="en-fr").get_result()
    french_text = response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    translates french to english
    """
    if french_text is None:
        return None
    response = lt.translate(text=french_text,model_id="fr-en").get_result()
    english_text = response['translations'][0]['translation']
    return english_text
