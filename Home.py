import streamlit as st
import functions


st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox(label="Select data to view: ",
                      options=('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}.")



