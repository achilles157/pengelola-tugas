import streamlit as st
from task_manager import TaskManager

task_manager = TaskManager()

def kelola_tugas():
    if not task_manager.data.empty:
        st.subheader("Kelola Tugas :seedling:")
        
        # Search functionality
        search_query = st.text_input("Cari Tugas:")
        
        # Filtering options
        filter_option = st.selectbox("Filter berdasarkan status:", ["Semua", "Selesai", "Belum Selesai"])
        
        if filter_option == "Selesai":
            filtered_data = task_manager.data[task_manager.data['Status'] == "Selesai"]
        elif filter_option == "Belum Selesai":
            filtered_data = task_manager.data[task_manager.data['Status'] == "Belum Selesai"]
        else:
            filtered_data = task_manager.data
        
        # Apply search filter
        if search_query:
            filtered_data = filtered_data[filtered_data['Tugas'].str.contains(search_query, case=False)]
        
        # Sorting options
        sort_option = st.selectbox("Urutkan berdasarkan:", ["Prioritas", "Tanggal Jatuh Tempo"])
        
        if sort_option == "Prioritas":
            filtered_data = filtered_data.sort_values(by='Prioritas')
        elif sort_option == "Tanggal Jatuh Tempo":
            filtered_data = filtered_data.sort_values(by='Tanggal Jatuh Tempo')

        for i, task in enumerate(filtered_data['Tugas']):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"{i + 1}. {task} - Status: {filtered_data.at[i, 'Status']}")
                
            with col2:
                if st.button("Selesai", key=f"selesai_{i}"):
                    task_manager.update_status(i, "Selesai")
                    st.success(f"Tugas '{task}' telah ditandai selesai!")
                    
            with col3:
                if st.button("Hapus", key=f"hapus_{i}"):
                    if st.confirm("Apakah Anda yakin ingin menghapus tugas ini?"):
                        task_manager.delete_task(i)
                        st.success(f"Tugas '{task}' telah dihapus!")
    else:
        st.write("Tidak ada tugas yang tersedia.")

kelola_tugas()
