import streamlit as st
from datetime import datetime
import json
import os

def pengaturan():
    # Load existing preferences if they exist
    preferences_file = "preferences.json"
    if os.path.exists(preferences_file):
        with open(preferences_file, "r") as f:
            preferences = json.load(f)
    else:
        preferences = {}

    # Pengaturan tema tampilan
    theme_option = st.selectbox("Pilih Tema Tampilan:", ["Default", "Gelap"], index=0 if preferences.get("theme") != "Gelap" else 1)
    
    if theme_option == "Gelap":
        st.markdown(
            """
               <style>
            .stApp {
                background-color: black;
                color: white;
            }
            .stText, .stMarkdown, .stHeader, .stSubheader {
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # Pengaturan notifikasi
    notification_enabled = st.checkbox("Aktifkan Notifikasi", value=preferences.get("notifications", False))
    
    if notification_enabled:
        notification_time = st.time_input("Waktu Notifikasi", datetime.now().time())
    
    # Simpan preferensi pengguna
    if st.button("Simpan Preferensi"):
        preferences["theme"] = theme_option
        preferences["notifications"] = notification_enabled
        if notification_enabled:
            preferences["notification_time"] = notification_time.strftime("%H:%M")
        else:
            preferences.pop("notification_time", None)
        
        with open(preferences_file, "w") as f:
            json.dump(preferences, f)
        
        st.success("Preferensi telah disimpan!")

    # Display current preferences
    st.write("Preferensi saat ini:")
    st.write(preferences)

st.header("Pengaturan Aplikasi :hammer_and_wrench:")
pengaturan()
