import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_FILE = "scraping/chapter_1.txt"
OUTPUT_FILE = "ai_writer/spun_chapter.txt"

def spin_chapter(text):
    prompt = f"""
    You are a creative AI writer. Rewrite (spin) the following book chapter in a new, engaging, yet faithful style. Keep the meaning the same, but change the sentence structure and vocabulary. Do NOT summarize. Preserve detail and narrative flow.
    Chapter to Rewrite:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}],
        temperature=0.8,
        max_tokens=2000
    )
    return response['choices'][0]['message']['content']

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        original_text = f.read()
    rewritten_text = spin_chapter(original_text)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(rewritten_text)
    print(f"Rewritten chapter saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()


