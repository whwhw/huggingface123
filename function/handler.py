import os
import requests

# assert "HGF_TOKEN" in os.environ, "No HGF_TOKEN env variable, you should add HGF_TOKEN as an env variable in the yaml file."

API_URL = os.environ.get("API_URL", "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5")
headers = {"Authorization": os.environ.get("HGF_TOKEN", "Bearer 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")}

def query(inputs):
    response = requests.post(API_URL, headers=headers, json=inputs)
    
    return response.content