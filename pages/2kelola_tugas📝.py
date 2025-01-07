import streamlit as st
from task_manager import TaskManager

task_manager = TaskManager()

def kelola_tugas():
    if 'username' not in st.session_state:
        st.error("Anda harus login terlebih dahulu.")
        return

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
        
        # Check if any tasks were found
        if filtered_data.empty:
            st.warning("Tugas tidak ditemukan.")
        else:
            # Sorting options
            sort_option = st.selectbox("Urutkan berdasarkan:", ["Prioritas", "Tanggal Jatuh Tempo"])
            
            if sort_option == "Prioritas":
                filtered_data = filtered_data.sort_values(by='Prioritas')
            elif sort_option == "Tanggal Jatuh Tempo":
                filtered_data = filtered_data.sort_values(by='Tanggal Jatuh Tempo')

            for i, task in enumerate(filtered_data['Tugas']):
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                
                with col1:
                    st.write(f"{i + 1}. **{task}** -  Status: {filtered_data.at[i, 'Status']}")
                    st.write(f"   **Deskripsi:** {filtered_data.at[i, 'Deskripsi']}")
                    
                with col2:
                    if st.button("Selesai", key=f"selesai_{i}"):
                        task_manager.update_status(filtered_data.index[i], "Selesai")
                        st.success(f"Tugas '{task}' telah ditandai selesai!")
                        
                with col3:
                    if st.button("Tandai Belum Selesai", key=f"belum_selesai_{i}"):
                        task_manager.update_status(filtered_data.index[i], "Belum Selesai")
                        st.success(f"Tugas '{task}' telah ditandai belum selesai!")
                        
                with col4:
                    if st.button("Hapus", key=f"hapus_{i}"):
                        task_manager.delete_task(filtered_data.index[i])  # Use the index of the filtered data
                        st.success(f"Tugas '{task}' telah dihapus!")
    else:
        st.write("Tidak ada tugas yang tersedia.")

kelola_tugas()
