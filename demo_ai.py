def demo_ai(prompt):
    prompt=prompt.lower()

    if "hello"in prompt:
        return "Hi! how can I help you Today?"
    elif "your name" in prompt:
        return "I am a simple Python AI Simulation"
    elif "advice" in prompt:
        return "keep learning a little every day. Consistency beats intensity"
    else:
        return "sorry, I don't understand that yet "
    
while True:
    user_input=input("You: ")

    if user_input.lower()=="exit":
        break
    
    response=demo_ai(user_input)
    print("AI:", response)