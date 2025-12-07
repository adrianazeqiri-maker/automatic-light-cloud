# automatic_light_control.py
import streamlit as st
import random
import time

st.title("Simulim i Kontrollit të Ndriçimit Automatik")

# Slider për ndriçimin ambient
ndricimi = st.slider("Ndriçimi ambientale (0-100)", 0, 100, 50)

# Vendimmarrja automatike
if ndricimi < 40:
    status_drite = "💡 Drita është E NDIZUR"
else:
    status_drite = "❌ Drita është E FIKUR"

# Shfaq statusin
st.subheader(status_drite)

# Opsional: simulim automatik i ndriçimit
if st.checkbox("Simulo ndryshimin e ndriçimit automatikisht"):
    placeholder = st.empty()
    for _ in range(20):
        ndricimi_random = random.randint(0, 100)
        if ndricimi_random < 40:
            status = "💡 Drita është E NDIZUR"
        else:
            status = "❌ Drita është E FIKUR"
        placeholder.text(f"Ndriçimi: {ndricimi_random} → {status}")
        time.sleep(1)
