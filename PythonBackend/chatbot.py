import os
import openai

openai.api_key = (os.environ["OPENAI_KEY"])

def chat_with_bot(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Financial Bot: {message}",
        max_tokens=100  
    )
    return response.choices[0].text.strip()

print("Chat with the financial bot. Type 'EXIT' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    response = chat_with_bot(user_input)
    print("Financial Bot: ", response)
