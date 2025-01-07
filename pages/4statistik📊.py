import streamlit as st
from task_manager import TaskManager
import matplotlib.pyplot as plt

task_manager = TaskManager()

def tampilkan_statistik():
    if 'username' not in st.session_state:
        st.error("Anda harus login terlebih dahulu.")
        return

    if not task_manager.data.empty:
        # Bar chart for task priorities
        st.bar_chart(task_manager.data['Prioritas'].value_counts())
        
        # Pie chart for task completion status
        completion_counts = task_manager.data['Status'].value_counts()
        st.write("Status Tugas:")
        
        # Create a figure and axis for the pie chart
        fig, ax = plt.subplots()
        ax.pie(completion_counts, labels=completion_counts.index, autopct='%1.1f%%')
        st.pyplot(fig)
        
        # Line chart for task completion over time
        task_completion = task_manager.data.groupby('Tanggal Jatuh Tempo')['Status'].value_counts().unstack().fillna(0)
        plt.figure(figsize=(10, 5))
        task_completion.plot(kind='line', marker='o', ax=plt.gca())  # Use line plot with markers
        plt.title('Task Completion Over Time')
        plt.xlabel('Tanggal Jatuh Tempo')
        plt.ylabel('Jumlah Tugas')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.legend(title='Status')
        plt.tight_layout()  # Adjust layout to prevent overlap
        st.pyplot(plt.gcf())
        
        total_tasks, completed_tasks, pending_tasks = task_manager.get_statistics()
        
        st.write(f"Total Tugas: {total_tasks}")
        st.write(f"Tugas Selesai: {completed_tasks}")
        st.write(f"Tugas Belum Selesai: {pending_tasks}")
    else:
        st.write("Tidak ada tugas yang tersedia.")

st.header("Statistik Tugas :roller_coaster:")
tampilkan_statistik()
