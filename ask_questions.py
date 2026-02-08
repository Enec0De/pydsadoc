#!/usr/bin/env python

__version__ = "0.1"
__author__ = "Aina"

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI, Stream
from openai.types.chat import ChatCompletionChunk

PROMPT = """
You are a helpful assistant.
"""


def deppseek_chat(INPUT: str) -> Stream[ChatCompletionChunk]:
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        # model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": f"{PROMPT}"},
            {"role": "user", "content": f"{INPUT}"},
        ],
        stream=True,
    )

    return response


if __name__ == "__main__":
    load_dotenv()

    try:
        while True:
            response = deppseek_chat(input("❓: "))

            # print(response.choices[0].message.content)
            print("\n🤖: ", end="")
            for event in response:
                content = event.choices[0].delta.content
                if content is not None:
                    print(content, sep="", end="")
            print("\n")

    except KeyboardInterrupt:
        sys.exit()
