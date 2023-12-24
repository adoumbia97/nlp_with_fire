import wikipedia
from textblob import TextBlob

def search_wikipedia(name):
    """ Search topic in Wikipedia"""
    print(f"Searching in wikipedia for name: {name}")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """Summarize wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """ Getting text blob """
    blob=TextBlob(text)
    return blob

def get_phrases(name):
    """ Find wikipedia name and return sentence"""
    #name=search_wikipedia(name)[0]
    text= summarize_wikipedia(name) 
    blob=get_text_blob(text)  
    phrases=blob.sentences
    return phrases
