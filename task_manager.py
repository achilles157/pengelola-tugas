import streamlit as st
import pandas as pd

class TaskManager:
    def __init__(self):
         try:
             self.data = pd.read_csv('data_tugas.csv')
         except FileNotFoundError:
             self.data = pd.DataFrame(columns=['Tugas', 'Deskripsi', 'Tanggal Jatuh Tempo', 'Prioritas', 'Status'])
    
    def get_statistics(self):
         total_tasks = len(self.data)
         completed_tasks = len(self.data[self.data['Status'] == 'Selesai'])
         pending_tasks = total_tasks - completed_tasks
         return total_tasks, completed_tasks, pending_tasks
    
    # ini untuk function objek tambah_tugas
    def add_task(self, task):
         self.data.loc[len(self.data)] = task
         self.save_to_csv()

    def delete_task(self, index):
         if 0 <= index < len(self.data):
             self.data = self.data.drop(index).reset_index(drop=True)
             self.save_to_csv()

    def update_status(self, index, status):
         if 0 <= index < len(self.data):
             self.data.at[index, 'Status'] = status
             self.save_to_csv()

    def save_to_csv(self):
         self.data.to_csv('data_tugas.csv', index=False)



