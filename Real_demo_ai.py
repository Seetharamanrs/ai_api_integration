from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv()
def create_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(client,prompt):
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
            {"role":"system", "content":"You are a helpful assisstant."},
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content


def main():
    client=create_client()
    print("AI Assistant(type 'exit' to quit)\n")
    while True:
        user_input=input("You: ")

        if user_input.lower()=="exit":
            break
        reply=ask_ai(client,user_input)
        print("AI:",reply)
        print()
if __name__=="__main__":
    main()
