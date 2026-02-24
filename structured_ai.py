import json

def build_request(user_message):
    request_payload={
        "model":"fake-gpt",
        "messages":[
            {"role": "system", "content": "You are a helpful finance assistant."},
            {"role": "user", "content": user_message}

        ]
    }
    return request_payload

def fake_model_response(request_payload):
    user_message = request_payload["messages"][1]["content"].lower()

    if "save" in user_message:
        reply = "Saving regularly is a smart financial habit."
    elif "spend" in user_message:
        reply = "You should review your monthly spending categories."
    else:
        reply = "I received your message."  

    response = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": reply
                }
            }
        ]
    }

    return response


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    request_data = build_request(user_input)
    print("DEBUG request_data:", request_data)

    print("\n--- JSON Sent to Model ---")
    print(json.dumps(request_data, indent=2))

    response = fake_model_response(request_data)

    ai_reply = response["choices"][0]["message"]["content"]

    print("AI:", ai_reply)
    print()

