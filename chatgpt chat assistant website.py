import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a python expert "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "My python assistant")

demo.launch(share=True)