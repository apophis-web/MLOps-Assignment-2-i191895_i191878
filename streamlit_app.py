import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='Bar Chart with Two Entities')

# Define data
data = pd.DataFrame({
    'entity': ['positive', 'negative'],
    'value': [10, 20]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    x='label',
    y='value'
).properties(
    width=alt.Step(80)
)

# Render streamlit app
def app():
    st.title('Bar Chart with Two Entities')
    st.write('This app creates a bar chart with two entities')
    st.altair_chart(bar_chart, use_container_width=True)

if __name__ == '__main__':
    app()
