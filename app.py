import streamlit as st
import requests
import pandas as pd

# 1️⃣ Last Updated Timestamp.Show when the traffic data was fetched:

from datetime import datetime
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.set_page_config(
    page_title="Mumbai Traffic Checker",
    page_icon="🚦",
    layout="centered"
)

st.title("🚦 Mumbai Live Traffic Checker")

# 1️⃣ Add your API key here
API_KEY = st.secrets["tomtom"]["api_key"]


st.markdown("Enter a location to check live traffic conditions.")

# 2️⃣ Input widgets
CITY_LOCATIONS = {
    "South Mumbai": {
        "Colaba": (18.9067, 72.8147),
        "Churchgate": (18.9322, 72.8264),
        "Marine Lines": (18.9430, 72.8272),
        "Mumbai Central": (18.9690, 72.8194),
        "Worli": (19.0176, 72.8162)
    },

    "Central Mumbai": {
        "Dadar": (19.0178, 72.8478),
        "Mahim": (19.0425, 72.8404),
        "Sion": (19.0400, 72.8647),
        "Kurla": (19.0726, 72.8826),
        "Chembur": (19.0623, 72.9005)
    },

    "Western Suburbs": {
        "Bandra West": (19.0607, 72.8362),
        "Bandra East": (19.0596, 72.8466),
        "Santacruz West": (19.0824, 72.8347),
        "Andheri West": (19.1364, 72.8296),
        "Andheri East": (19.1197, 72.8468),
        "Goregaon West": (19.1650, 72.8336),
        "Malad West": (19.1860, 72.8420),
        "Borivali West": (19.2350, 72.8441)
    },

    "Eastern Suburbs": {
        "Powai": (19.1176, 72.9060),
        "Ghatkopar": (19.0856, 72.9080),
        "Vikhroli": (19.1097, 72.9287),
        "Mulund West": (19.1726, 72.9426),
        "Bhandup": (19.1511, 72.9372)
    }
}
# 1️⃣ Select suburb first
suburb = st.selectbox(
    "Select Suburb",
    CITY_LOCATIONS.keys()
)

# 2️⃣ Select city based on suburb
city = st.selectbox(
    "Select Area",
    CITY_LOCATIONS[suburb].keys()
)

# 3️⃣ Get lat & long
lat, lon = CITY_LOCATIONS[suburb][city]


# 3️⃣ Button to trigger API call
if st.button("Check Traffic"):
    url = (
        "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/json"
        f"?point={lat},{lon}&key={API_KEY}"
    )

    # 4️⃣ Call the API
    response = requests.get(url)

    if response.status_code != 200:
        st.error("Error calling TomTom API")
    else:
        data = response.json()

        # 5️⃣ Extract flow data
        flow_data = data["flowSegmentData"]
        current_speed = flow_data["currentSpeed"]
        free_flow_speed = flow_data["freeFlowSpeed"]

        slowdown_percentage = round(
            ((free_flow_speed - current_speed) / free_flow_speed) * 100, 1
        )

        estimated_delay = round((slowdown_percentage / 100) * 30)

        # 6️⃣ Determine traffic condition
        if slowdown_percentage < 10:
            condition = "🟢 Light traffic"
            st.success(
                f"Traffic is {slowdown_percentage}% slower than normal "
                f"(≈ {estimated_delay} min delay)"
            )
        elif slowdown_percentage < 25:
            condition = "🟡 Moderate congestion"
            st.warning(
                f"Traffic is {slowdown_percentage}% slower than normal "
                f"(≈ {estimated_delay} min delay)"
            )
        else:
            condition = "🔴 Heavy congestion"
            st.error(
            f"Traffic is {slowdown_percentage}% slower than normal "
            f"(≈ {estimated_delay} min delay). Consider alternate routes."
        )



        # 7️⃣ Display results
        st.metric("Current Speed (km/h)", current_speed)
        st.metric("Free Flow Speed (km/h)", free_flow_speed)
        st.write(f"**Condition:** {condition}")

        # Congestion bar
        st.progress(min(int(slowdown_percentage), 100))

        # Map
        st.map([{"lat": lat, "lon": lon}])


        with st.expander("What do these numbers mean?"):
            st.markdown("""
        **Current Speed**
        - The average speed of vehicles on this road *right now*. Lower values indicate congestion or slow-moving traffic.

        **Free Flow Speed**
        - The typical speed on the same road when traffic is light. This is not the speed limit, but a normal baseline.

        **Slowdown %**
        - Shows how much slower traffic is compared to normal conditions. Helps quickly assess congestion severity.
        """)
