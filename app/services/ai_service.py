import os
import json
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print(os.getenv("GEMINI_API_KEY"))

def generate_product_metadata(name: str):
    prompt = f"""
    You are an expert e-commerce assistant.

    Given the product name: "{name}"

    Generate:
    1. A professional product description (2-3 sentences)
    2. 5 SEO-friendly tags (as a list)
    3. A suitable product category

    Return strictly in JSON format:
    {{
        "description": "...",
        "tags": ["...", "..."],
        "category": "..."
    }}
    """

    response = client.models.generate_content(
    model="gemini-flash-latest",  
    contents=prompt
)

    content = response.text

    try:
        return json.loads(content)
    except Exception:
        return {
            "description": content,
            "tags": [],
            "category": "general"
        }