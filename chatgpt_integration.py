##################################
# Date of creation: 24.01.2024
# Programmer: Ondrej Tomasek
# LinkedIn: linkedin.com/in/ondrat
##################################

# GLOBAL IMPORTS
import requests
import json
import base64

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

    # Analyze image from file
    def analyze_image(image_name, image_file_extension=".jpg", prompt_to_ask="What’s in this image? Be specific and shortly tell me something about it, focus on the main thing", model = "gpt-4-vision-preview", max_tokens_response = 150, CHATGPT_API_KEY = CHATGPT_API_KEY):
    
        if image_name == None:
            return False
        
        else:
            # Function to encode the image, because the image needs to be sent in base64 format
            def encode_image(image_path):
                with open(image_path, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode('utf-8')

            # Path to image you want to send
            image_path = f"{image_name}{image_file_extension}"

            # Getting the base64 string encoded format
            base64_image = encode_image(image_path)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {CHATGPT_API_KEY}"
            }

            payload = {
                "model": model,
                "messages": [
                {
                    "role": "user",
                    "content": [
                    {
                        "type": "text",
                        "text": prompt_to_ask # ADJUST YOUR PROMPT TO ASK
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                    ]
                }
                ],
                "max_tokens": max_tokens_response
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response_json = response.json()
            # Extract content from the API response
            content = response_json['choices'][0]['message']['content']

            return content
