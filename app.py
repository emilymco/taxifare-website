import streamlit as st
import requests

'''
# Welcome to the NYC Taxi Fare Predictor!
'''


# st.header("Enter your ride details:")
# date_and_time = st.text_input("Date and Time (YYYY-MM-DD HH:MM:SS):")
# pickup_longitude = st.number_input("Pickup Longitude:")
# pickup_latitude = st.number_input("Pickup Latitude:")
# dropoff_longitude = st.number_input("Dropoff Longitude:")
# dropoff_latitude = st.number_input("Dropoff Latitude:")
# passenger_count = st.number_input("Passenger Count:", min_value=1, max_value=8)

pickup_datetime = st.text_input("Date and Time (YYYY-MM-DD HH:MM:SS):", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup Longitude:", value=-73.950655)
pickup_latitude = st.number_input("Pickup Latitude:", value=40.783282)
dropoff_longitude = st.number_input("Dropoff Longitude:", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff Latitude:", value=40.769802)
passenger_count = st.number_input("Passenger Count:", min_value=1, max_value=8, value=2)

if st.button("Predict Fare"):


    url = 'https://taxifare.lewagon.ai/predict'

    # if url == 'https://taxifare.lewagon.ai/predict':

    #     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
        }

    response = requests.get(url, params=params)

    fare_pred = response.json()
    fare = fare_pred["fare"]

    st.write(f"Your predicted fare for this journey is ${round(fare, 2)}")





# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
