import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='Bar Chart with Positive Negative Reviews')

data = pd.DataFrame({
    'entity': ['positive', 'negative'],
    'value': [10, 20]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    x='Label',
    y='Count'
).properties(
    width=alt.Step(80)
)

def app():
    st.title('Bar Chart with Positive Negative Reviews)
    st.write('This app creates a bar chart with positive negative reviews')
    st.altair_chart(bar_chart, use_container_width=True)

if __name__ == '__main__':
    app()
