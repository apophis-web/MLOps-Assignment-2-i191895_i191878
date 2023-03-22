import pandas as pd
import requests
import streamlit as st
import altair as alt

with open("C:\\Users\\Hassa\\OneDrive\\Desktop\\docker_mlops\\data.txt", "r", encoding = "utf-8") as f:
    data = f.read().splitlines()

url = 'http://localhost:5000/sentiment'
sentences = data
pos = 0
neg = 0
for sentence in sentences:
    data = {'text': sentence}
    response = requests.post(url, json=data)
    if (response.json()["label"] == "POSITIVE"):
        pos = pos + 1
    else:
        neg = neg + 1

    st.set_page_config(page_title='Bar Chart with Two Entities')
    data = pd.DataFrame({
        'entity': ['Positive', 'Negative'],
        'value': [pos, neg]
    })

    bar_chart = alt.Chart(data).mark_bar().encode(
        x='entity',
        y='value'
    ).properties(
        width=alt.Step(80)
    )

    def app():
        st.title('Bar Chart with Two Entities')
        st.write('This app creates a bar chart with two entities')
        st.altair_chart(bar_chart, use_container_width=True)

    if __name__ == '__main__':
        app()
