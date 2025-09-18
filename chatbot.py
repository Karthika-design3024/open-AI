import openai
openai.api_key="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"
openai.api_base="https://openrouter.ai/api/v1"
while True:
    user_input=input("you:")
    if user_input.lower() in  ["exit","quit","bye"]:
        print("chatbot: Goodbye|")
        break
    response=openai.chatcompletion.create(
        models="mistralai/mistral-7b-instruct",
        messages=[
            {"role":"system","content":"you are a helpful and friendly AI assisant."},
            {"role":"user","content":user_input}
            ]
        )
    reply=response['choices'][0]['message']['content'].strip()
    print(f"chatbot:{reply}\n")

