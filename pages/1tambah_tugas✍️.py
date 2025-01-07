import streamlit as st
from task_manager import TaskManager
from datetime import datetime

task_manager = TaskManager()

def tambah_tugas():
    with st.form("form_tugas"):
        nama_tugas = st.text_input("Nama Tugas")
        deskripsi = st.text_area("Deskripsi Tugas")
        tanggal_jatuh_tempo = st.date_input("Tanggal Jatuh Tempo", min_value=datetime.today())
        prioritas = st.selectbox("Prioritas", ["Rendah", "Sedang", "Tinggi"])
        status = st.selectbox("Status", ["Belum Selesai", "Selesai"])
        
        submitted = st.form_submit_button("Submit")
        reset = st.form_submit_button("Reset")

        if reset:
            st.session_state.clear()  # Clear the session state to reset the form

        if submitted:
            if not nama_tugas:
                st.error("Nama Tugas tidak boleh kosong!")
            else:
                new_task = {
                    'Tugas': nama_tugas,
                    'Deskripsi': deskripsi,
                    'Tanggal Jatuh Tempo': tanggal_jatuh_tempo,
                    'Prioritas': prioritas,
                    'Status': status
                }
                task_manager.add_task(new_task)
                st.success("Anda telah menambahkan tugas baru:")
                st.write(new_task)

st.header("Tambah Tugas :star:")
tambah_tugas()
