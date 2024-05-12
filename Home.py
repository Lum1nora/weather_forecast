import streamlit as st
import plotly.express as px
from functions import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox(label="Select data to view: ",
                      options=('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}.")

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
