import streamlit as st
from task_manager import TaskManager
import pandas as pd
import datetime as dt
import calendar

task_manager = TaskManager()

def tampilkan_kalender():
    if 'username' not in st.session_state:
        st.error("Anda harus login terlebih dahulu.")
        return

    if not task_manager.data.empty:
        st.subheader("Kalender Tugas :hourglass_flowing_sand:")
        
        # Mengonversi kolom tanggal jatuh tempo ke datetime
        task_manager.data['Tanggal Jatuh Tempo'] = pd.to_datetime(task_manager.data['Tanggal Jatuh Tempo'], errors='coerce')
        
        # Menghapus baris dengan tanggal jatuh tempo yang tidak valid
        task_manager.data = task_manager.data.dropna(subset=['Tanggal Jatuh Tempo'])
        
        # Create a calendar
        year = dt.datetime.now().year
        month = dt.datetime.now().month
        cal = calendar.monthcalendar(year, month)

        for week in cal:
            cols = st.columns(7)
            for i, day in enumerate(week):
                if day == 0:
                    cols[i].write("")
                else:
                    date_str = f"{year}-{month:02d}-{day:02d}"
                    tasks_today = task_manager.data[task_manager.data['Tanggal Jatuh Tempo'].dt.date == dt.date(year, month, day)]
                    
                    # Display the day number
                    if dt.date(year, month, day) < dt.datetime.now().date():
                        cols[i].markdown(f"<span style='color:gray;'>{day}</span>", unsafe_allow_html=True)  # Past dates in gray
                    else:
                        cols[i].markdown(f"**{day}**")  # Current and future dates

                    if not tasks_today.empty:
                        # Display task names with color coding
                        for _, task in tasks_today.iterrows():
                            color = "green" if task['Status'] == "Selesai" else "red"
                            cols[i].markdown(f"<span style='color:{color};'>• {task['Tugas']}</span>", unsafe_allow_html=True)
                    else:
                        cols[i].write("")  # Empty cell for days with no tasks

tampilkan_kalender()
