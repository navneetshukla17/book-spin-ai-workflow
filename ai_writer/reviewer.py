import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_FILE = "ai_writer/spun_chapter.txt"
OUTPUT_FILE = "ai_writer/reviewed_chapter.txt"

def review_chapter(text):
    prompt = f"""
    You are an AI editor. Carefully review and refine the following rewritten chapter. Focus on improving clarity, grammar, flow and style. Keep the creative tone but make it more polished.
    Rewritten Chapter:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content":prompt}],
        temperature=0.6,
        max_tokens=2000
    )
    return response['choices'][0]['message']['content']

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        rewritten = f.read()
    reviewed = review_chapter(rewritten)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(reviewed)
    print("Reviewed chapter saved to: {OUTPUT_FILE}")

    
