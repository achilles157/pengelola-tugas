import streamlit as st
from task_manager import TaskManager
import pandas as pd
import datetime as dt
import calendar

task_manager = TaskManager()

def tampilkan_kalender():
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
                    tasks_today = task_manager.data[task_manager.data['Tanggal Jatuh Tempo'] == date_str]
                    if not tasks_today.empty:
                        cols[i].markdown(f"**{day}**")
                        for _, task in tasks_today.iterrows():
                            cols[i].markdown(f"- {task['Tugas']} ({task['Prioritas']})")
                    else:
                        cols[i].write(f"{day}")

tampilkan_kalender()
