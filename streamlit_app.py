import streamlit as st
import pandas as pd
import altair as alt

# Set page title
st.set_page_config(page_title='Bar Chart with Two Entities')

# Define data
data = pd.DataFrame({
    'entity': ['Entity 1', 'Entity 2'],
    'value': [10, 20]
})

# Create bar chart using Altair
bar_chart = alt.Chart(data).mark_bar().encode(
    x='entity',
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
