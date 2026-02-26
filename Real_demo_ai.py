from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(prompt):
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
            {"role":"system", "content":"You are a helpful assisstant."},
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content


while True:
    user_input=input("You: ")

    if user_input.lower()=="exit":
        break
    reply=ask_ai(user_input)
    print("AI:",reply)
    print()


