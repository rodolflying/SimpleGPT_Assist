
import os
import openai
import dotenv

# Load .env file
dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")

def ask_chatgpt(question):
    '''Ask chatgpt'''
    # Ask chatgpt
    print("Asking chatgpt:  ", question, " ")
    openai.api_key = API_KEY
    prompt = f"{question} "
    response = openai.Completion.create(
        engine="text-davinci-003", prompt = prompt, max_tokens = 2000)
    return response['choices'][0]['text']

def main():
    # Ask chatgpt
    question = input("Question: ")
    answer = ask_chatgpt(question)
    print("Answer: ", answer)

if __name__ == "__main__":
    main()
    