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

# Filter out tasks with invalid due dates
valid_tasks = task_manager.data[task_manager.data['Tanggal Jatuh Tempo'].notna()]

# Check for tasks due tomorrow
tomorrow = datetime.now().date() + pd.Timedelta(days=1)
upcoming_tasks = valid_tasks[
    valid_tasks['Tanggal Jatuh Tempo'].dt.date == tomorrow
]

if not upcoming_tasks.empty:
    st.warning("Anda memiliki tugas yang harus diselesaikan besok:")
    for _, task in upcoming_tasks.iterrows():
        st.write(f"- {task['Tugas']} (Jatuh Tempo: {task['Tanggal Jatuh Tempo']})")

st.subheader("Daftar Tugas :clipboard:")
st.dataframe((task_manager.data))

# Inisialisasi session state untuk menyimpan data tugas
if "tasks" not in st.session_state:
    st.session_state.tasks = []
