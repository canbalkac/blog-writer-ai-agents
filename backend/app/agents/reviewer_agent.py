from openai import OpenAI
from app.config import OPENROUTER_API_KEY

client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")

def review_content(content: str) -> list[str]:
    prompt = (
        "You are an expert editor and reviewer.\n"
        "Your job is to read the following article and provide 3 bullet-point feedback items that assess:\n"
        "- clarity\n"
        "- tone\n"
        "- structure and coherence\n"
        "- suggestions for improvement (if needed)\n\n"
        "Be specific, concise, and helpful. Write each item as a complete sentence.\n\n"
        f"ARTICLE:\n{content}"
    )

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional content reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=300
        )
        feedback_text = response.choices[0].message.content.strip()
        feedback_lines = [line.strip("-•– ") for line in feedback_text.split("\n") if line.strip()]
        return feedback_lines[:3]
    except Exception as e:
        return [f"⚠️ Error generating review: {str(e)}"]
