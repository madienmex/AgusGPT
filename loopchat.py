import openai
import json
import os
import cfunctions as cf
import mongodb
from config import config


def run_conversation(user_input, messages):
    dbEnabled = False
    if openai.api_key is None:
        openai.api_key = config.get_api_key()
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        #functions=cf.schema,
        #function_call="auto",
    )
    response_message = response.choices[0].message.content
    return response_message, messages


# Start the conversation loop if this is the main call - debugging MODE
if __name__ == '__main__':
    messages = []
    openai.api_key = os.getenv("OPENAI_API_KEY")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print("\nEOFError caught. Exiting...")
            break
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chat ended. Goodbye!")
            break
        response, messages = run_conversation(user_input, messages)
        print(f"Assistant: {response}")


