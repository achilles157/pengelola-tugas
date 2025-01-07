import pandas as pd

class TaskManager:
    def __init__(self):
        self.data = pd.read_csv('data_tugas.csv')

    def add_task(self, task):
        self.data = pd.concat([self.data, pd.DataFrame([task])], ignore_index=True)
        self.data.to_csv('data_tugas.csv', index=False)

    def delete_task(self, index):
        self.data = self.data.drop(index)
        self.data.to_csv('data_tugas.csv', index=False)

    def update_status(self, index, status):
        self.data.at[index, 'Status'] = status
        self.data.to_csv('data_tugas.csv', index=False)

    def get_statistics(self):
        total_tasks = len(self.data)
        completed_tasks = len(self.data[self.data['Status'] == "Selesai"])
        pending_tasks = total_tasks - completed_tasks
        return total_tasks, completed_tasks, pending_tasks
