import spacy
import pandas as pd

from datetime import datetime

nlp = spacy.load("en_core_web_sm")

def save_words(username, user_response, power_words, negative_words):
    print("Saving words...")
    for word in power_words:
        if word in user_response:
            user_response = user_response.replace(word, '')
    for word in negative_words:
        if word in user_response:
            user_response = user_response.replace(word, '')
            
    user_response = nlp(user_response)
    user_response_filtered_text = " ".join(token.text for token in user_response if not token.is_stop)
    user_response_filtered_text = user_response_filtered_text.replace(',', '').strip(" ")
    user_response_filtered_text = user_response_filtered_text.split(" ")
    
    try:
        df_existing = pd.read_excel('words.xlsx')
    except FileNotFoundError:
        df_existing = pd.DataFrame(columns=['Words'])
    new_words = [word for word in user_response_filtered_text if word not in df_existing['Words'].values]
    df_new = pd.DataFrame({'Words': new_words})
    
    if not df_new.empty:
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_existing
    df_combined.to_excel('words.xlsx', index=False)
    print("File Generated Successfully!")
