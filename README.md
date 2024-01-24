# ChatGPT Integration in Python

This repository contains a Python script (`chatgpt_integration.py`) that allows you to interact with OpenAI's ChatGPT model using the OpenAI API. You can ask ChatGPT anything by providing a prompt, and the script will return the model's response.

### DEFAULT VALUES USED IN FUNCTIONS:
```
(Values below can be manually adjusted while calling the function)

model: "gpt-3.5-turbo"
assistant: "You are a helpful assistant."
max tokens: 100
```

## Usage

1. **API Key Setup**: Obtain your OpenAI API key and replace the placeholder `YOUR_API_KEY` with your actual API key in the `CHATGPT_API_KEY` variable.

2. **Code Integration**: Import the `ChatGPT` class into your project or script.

3. **Asking Questions**: Use the `ask` method of the `ChatGPT` class to interact with the ChatGPT model. Provide a prompt, and the method will return the model's response.

   ```python
   response = ChatGPT.ask(prompt="What is the meaning of life?")
   print(response)
   ```

You can also customize the assistant's prompt, choose the model version, and set the maximum number of tokens in the response.

```python
response = ChatGPT.ask(prompt="Tell me a joke.", assistant_prompt="You are a funny assistant.", model="gpt-3.5-turbo", max_tokens_response=50)
print(response)
```

## Requirements

- Python 3.x
- Needed libraries can be automatically installed by opening `dependencies.bat` on Windows computer

## Example code

```python
# Example Usage
import chatgpt_integration

# Replace 'YOUR_API_KEY' with your actual API key
CHATGPT_API_KEY = "YOUR_API_KEY"

# Set your API key
chatgpt_integration.CHATGPT_API_KEY = CHATGPT_API_KEY

# Ask a question
response = chatgpt_integration.ChatGPT.ask("What is the capital of France?")
print(response)
```

## Contact

- **Programmer:** Ondrej Tomasek
- **LinkedIn:** [linkedin.com/in/ondrat](https://www.linkedin.com/in/ondrat/)

Feel free to reach out if you have any questions or feedback!
