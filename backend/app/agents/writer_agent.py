from openai import OpenAI
from app.config import OPENROUTER_API_KEY

# OpenRouter yapılandırması
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def write_content(topic: str, context: str) -> str:
    prompt = (
        f"Write an informative and engaging introduction article about '{topic}'.\n\n"
        f"Background info:\n{context}\n\n"
        f"Make it clear, concise, and approximately 3 paragraphs long. Use markdown."
    )

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",  # veya "openai/gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a skilled professional writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error generating content: {str(e)}"