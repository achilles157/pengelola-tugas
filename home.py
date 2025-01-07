import streamlit as st
from task_manager import TaskManager
from datetime import datetime
import pandas as pd

# Set konfigurasi halaman
st.set_page_config(page_title="Aplikasi Pengelola Tugas", page_icon="📝")

# Judul aplikasi
st.title("Pengelola Tugas Sederhana")

# Dark mode toggle
dark_mode = st.checkbox("Aktifkan Mode Gelap")

if dark_mode:
    st.markdown("""
        <style>
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        h1 {
            color: #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f5;
            color: black;
        }
        h1 {
            color: #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)

# Menampilkan gambar header
st.image('header_image.jpg', width=800)  # Pastikan path gambar benar

# Menambahkan penjelasan aplikasi
st.write("""
    Aplikasi ini dirancang untuk membantu Anda mengelola tugas-tugas Anda dengan lebih efisien.
    Anda dapat melihat daftar tugas yang harus diselesaikan, termasuk deskripsi, tanggal jatuh tempo, 
    prioritas, dan status masing-masing tugas.
""")

task_manager = TaskManager()

# Ensure 'Tanggal Jatuh Tempo' is in datetime format
task_manager.data['Tanggal Jatuh Tempo'] = pd.to_datetime(task_manager.data['Tanggal Jatuh Tempo'], errors='coerce')

# Convert other columns to appropriate types if necessary
task_manager.data['Tugas'] = task_manager.data['Tugas'].astype(str)
task_manager.data['Deskripsi'] = task_manager.data['Deskripsi'].astype(str)
task_manager.data['Prioritas'] = task_manager.data['Prioritas'].astype(str)
task_manager.data['Status'] = task_manager.data['Status'].astype(str)

# Filter out tasks with invalid due dates
valid_tasks = task_manager.data[task_manager.data['Tanggal Jatuh Tempo'].notna()]

# Check for upcoming due tasks
upcoming_tasks = valid_tasks[
    (valid_tasks['Tanggal Jatuh Tempo'] - pd.to_datetime(datetime.now().date())).dt.days <= 3
]

if not upcoming_tasks.empty:
    st.warning("Anda memiliki tugas yang akan jatuh tempo dalam 3 hari ke depan:")
    for _, task in upcoming_tasks.iterrows():
        st.write(f"- {task['Tugas']} (Jatuh Tempo: {task['Tanggal Jatuh Tempo']})")

st.subheader("Daftar Tugas :clipboard:")
st.dataframe((task_manager.data))

# Inisialisasi session state untuk menyimpan data tugas
if "tasks" not in st.session_state:
    st.session_state.tasks = []
