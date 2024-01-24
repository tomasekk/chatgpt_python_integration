##################################
# Date of creation: 24.01.2024
# Programmer: Ondrej Tomasek
# LinkedIn: linkedin.com/in/ondrat
##################################

# GLOBAL IMPORTS
# None

# OWN IMPORTS
import chatgpt_integration

# Data
API_KEY = "YOUR_API_KEY"

# Code
TEST1 = chatgpt_integration.ChatGPT.ask("What do you do?", CHATGPT_API_KEY = API_KEY)

TEST2 = chatgpt_integration.ChatGPT.ask("What do you do?", assistant_prompt = "You are a teacher of mathematics.", CHATGPT_API_KEY = API_KEY)

print(f"{TEST1}\n{TEST2}")
