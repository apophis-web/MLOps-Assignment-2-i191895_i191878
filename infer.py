import pandas as pd
import requests
import streamlit as st
import altair as alt

with open("data.txt", "r", encoding = "utf-8") as f:
    sentences = f.read().splitlines()

url = 'http://localhost:5000/sentiment'

st.title("Sentiment Analysis Results")
chart_placeholder = st.empty()

pos = 0
neg = 0

for sentence in sentences:
    data = {'text': sentence}
    response = requests.post(url, json=data)
    sentiment = response.json()["label"]
    if sentiment == "POSITIVE":
        pos += 1
    else:
        neg += 1
    df = pd.DataFrame({"Sentiment": ["Positive", "Negative"], "Count": [pos, neg]})
    chart = alt.Chart(df).mark_bar().encode(x="Sentiment", y="Count")
    chart_placeholder.altair_chart(chart, use_container_width=True)
