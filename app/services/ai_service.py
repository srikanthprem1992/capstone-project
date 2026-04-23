def generate_product_metadata(name: str):
    return {
        "description": f"{name} is a high-quality product with excellent performance and durability.",
        "tags": ["premium", "latest", "trending"],
        "category": "electronics"
    }

# import requests

# def generate_product_metadata(name: str):
#     prompt = f"""
#     Generate product metadata for: {name}
#     Return JSON with description, tags (list), category
#     """

#     response = requests.post(
#         "https://api.openai.com/v1/chat/completions",
#         headers={
#             "Authorization": "Bearer YOUR_API_KEY",
#             "Content-Type": "application/json"
#         },
#         json={
#             "model": "gpt-4o-mini",
#             "messages": [{"role": "user", "content": prompt}]
#         }
#     )

#     data = response.json()

#     # You’ll need to parse response properly
#     return {
#         "description": "Parsed description",
#         "tags": ["tag1", "tag2"],
#         "category": "category"
#     }