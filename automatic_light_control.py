import streamlit as st
import random
import time
import pandas as pd
import altair as alt

st.set_page_config(page_title="Kontroll Ndriçimi Automatik", page_icon="💡")
st.title("Simulim i Kontrollit të Ndriçimit Automatik me Line Chart")

# Slider për ndriçimin ambient
ndricimi = st.slider("Ndriçimi ambiental (0-100)", 0, 100, 50)

# Vendimmarrja automatike
if ndricimi < 40:
    status_drite = "💡 Drita është E NDEZUR"
else:
    status_drite = "❌ Drita është E FIKUR"

st.subheader(status_drite)

# Krijo DataFrame për grafikun fillestar
df = pd.DataFrame({"Ndriçimi": [ndricimi], "Koha": [0], "Status": [status_drite]})

# Shfaq grafik linjë fillestar
line_chart = alt.Chart(df).mark_line(point=True).encode(
    x='Koha',
    y='Ndriçimi',
    color='Status'
)
chart_placeholder = st.altair_chart(line_chart, use_container_width=True)

# Opsional: simulim automatik i ndriçimit
if st.checkbox("Simulo ndryshimin e ndriçimit automatikisht"):
    for t in range(1, 21):
        ndricimi_random = random.randint(0, 100)
        if ndricimi_random < 40:
            status = "💡 Drita është E NDEZUR"
        else:
            status = "❌ Drita është E FIKUR"
        df = pd.concat([df, pd.DataFrame({"Ndriçimi": [ndricimi_random], "Koha": [t], "Status": [status]})], ignore_index=True)
        chart = alt.Chart(df).mark_line(point=True).encode(
            x='Koha',
            y='Ndriçimi',
            color='Status'
        )
        chart_placeholder.altair_chart(chart, use_container_width=True)
        time.sleep(1)

