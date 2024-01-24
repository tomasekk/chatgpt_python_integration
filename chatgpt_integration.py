##################################
# Date of creation: 24.01.2024
# Programmer: Ondrej Tomasek
# LinkedIn: linkedin.com/in/ondrat
##################################

# GLOBAL IMPORTS
import requests
import json

# OWN IMPORTS
# None

# Data
CHATGPT_API_KEY = "YOUR_API_KEY"

# Code
class ChatGPT:
    # Ask ChatGPT anything over chat prompt
    def ask(prompt, assistant_prompt = "You are a helpful assistant.", model = "gpt-3.5-turbo", max_tokens_response = 100, CHATGPT_API_KEY = CHATGPT_API_KEY):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CHATGPT_API_KEY}",
            
        }
        data = {
            "messages": [
            {"role": "system", "content": assistant_prompt},
            {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens_response,
            "model": model
        }
        
        # Send and receive request data
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = response.json()

        # Filter only the reponse
        content = response_data['choices'][0]['message']['content']

        return content
