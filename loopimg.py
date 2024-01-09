import openai
import json
import os
import cfunctions as cf
import mongodb
from config import config


def gen_image(user_input):
    dbEnabled = False
    openai.api_key = config.get_api_key()
    myimage = openai.images.generate(
        model="dall-e-3",
        prompt=user_input,
        n=1,
        size="1792x1024",
    )
    return myimage.data[0]


# Start the conversation loop if this is the main call - debugging MODE
if __name__ == '__main__':
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
        response = gen_image(user_input)
        print(f"Generation: {response}")


