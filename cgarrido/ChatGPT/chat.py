#!/usr/bin/python3

import os
from dotenv import load_dotenv
import openai
openai.api_key = os.getenv("chatSecretKey")

if __name__ == "__main__":

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
    )

    print(completion.choices[0].message)
