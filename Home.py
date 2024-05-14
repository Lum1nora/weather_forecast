import streamlit as st
import plotly.express as px
from functions import get_data
from datetime import datetime

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place", placeholder="")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox(label="Select data to view: ",
                      options=('Temperature', 'Sky'))
try:
    if place:
        data = get_data(place, days)
        st.subheader(f"{option} for the next {days} days in {place}.")
        dates = [dict['dt_txt'] for dict in data]
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict['weather'][0]['main'] for dict in data]
            dates = [datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
                     for i in dates]
            dates = [i.strftime("%a, %b %d %H:%M") for i in dates]
            img_dict = {"Clear": "images/clear.png",
                        "Clouds": "images/cloud.png",
                        "Rain": "images/rain.png", "Snow": "images/snow.png"}
            img_path = [img_dict[sky] for sky in sky_conditions]
            st.image(img_path, width=115, caption=dates)
except KeyError:
    st.info("Please enter a valid city. Thank you")
