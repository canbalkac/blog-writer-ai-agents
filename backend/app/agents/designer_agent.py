import openai
from app.config import OPENROUTER_API_KEY

openai.api_key = OPENROUTER_API_KEY
openai.api_base = "https://openrouter.ai/api/v1"

def get_images_for_topic(topic: str) -> list[str]:
    try:
        response = openai.Image.create(
            model="openai/dall-e-3",  # OpenRouter DALLE modeli
            prompt=f"Futuristic concept art about {topic}, high quality, digital art",
            n=2,
            size="1024x1024"
        )
        return [img["url"] for img in response["data"]]
    except Exception as e:
        return [f"Image generation failed: {str(e)}"]
