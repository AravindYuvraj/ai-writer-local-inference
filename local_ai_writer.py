import gradio as gr
import requests
import datetime

# Talk to local Ollama model
def generate_blog_intro(topic, temperature):
    prompt = f"Write a blog introduction about: {topic}"

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama3',
            'prompt': prompt,
            'temperature': temperature,
            'stream': False
        }
    )

    result = response.json()['response']

    # Log to file
    with open("ai_writer_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - Topic: {topic}\n{result}\n\n")

    return result


# Build UI
ui = gr.Interface(
    fn=generate_blog_intro,
    inputs=[
        gr.Textbox(label="Enter a topic for your blog intro"),
        gr.Slider(0, 1, value=0.7, label="Temperature (creativity)")
    ],
    outputs=gr.Textbox(label="Generated Blog Intro"),
    title="✍️ Local AI Blog Writer (LLaMA3)",
    description="Runs entirely offline using Ollama and local LLMs like LLaMA 3"
)

# Launch UI
if __name__ == "__main__":
    ui.launch()
