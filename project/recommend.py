import pymongo
import requests
from icecream import ic

client = pymongo.MongoClient(
    "mongodb+srv://wazedkhan119399:7LRU8OS2BQv2N00U@cluster0.edtgmjj.mongodb.net/?retryWrites=true&w=majority"
)
db = client.sample_mflix
collection = db.movies


hugging_face_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

response = requests.post(
    embedding_url,
    headers={
        "Authorization": f"Bearer {hugging_face_token}",
    },
)
