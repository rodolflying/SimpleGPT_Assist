
import os
import openai
import dotenv
import datetime

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

    # Return the query, but the one that chat gpt resume in its response
    # query = response['choices'][0]['text'].split(" ")[0]
    print("Response: ", response)

    # Return the id of the answer and the date it was created
    id = response['id']
    date = response['created']
    #format date to be readable
    date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    
    return response['choices'][0]['text'], id, date

def save_result(question, answer, id, date):
    '''Save result to file'''
    # Save result to file as json containg question and answer
    #naming the file depending on the question, so that we can easily find the answer later
    # not using the full question, since it might be too long for a file name
    print("Saving result to file")
    file_name = question.replace(" ", "_")
    file_name = file_name[:20]
    #clean file_name from all special characters that aren't allowed in file names
    file_name = "".join([char for char in file_name if char.isalnum() or char == "_"])
    with open(f"{file_name}.json", "w" ) as f:
        f.write(f'{{"question": "{question}", "answer": "{answer}", "id": "{id}", "date": "{date}"}}')


def main():
    # Ask chatgpt
    question = input("Question: ")
    answer, id, date  = ask_chatgpt(question)

    # Save result to file
    save_result(question, answer, id, date)

    print("Answer: ", answer)

if __name__ == "__main__":
    main()
    