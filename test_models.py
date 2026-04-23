from google import genai
import os

client = genai.Client(api_key="AIzaSyBeMfKKY9S8eQjG-NPRJkfrQOEdbYk_wpc")

for m in client.models.list():
    print(m.name)