import pandas as pd
import requests

with open("C:\\Users\\Hassa\\OneDrive\\Desktop\\docker_mlops\\data.txt", "r", encoding = "utf-8") as f:
    data = f.read().splitlines()

url = 'http://localhost:5000/sentiment'
sentences = data
for sentence in sentences:
    data = {'text': sentence}
    response = requests.post(url, json=data)
    print(response.json())