import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os

# Файл для хранения истории
DATA_FILE = "tasks.json"

# Предопределенный список задач с типами
PREDEFINED_TASKS = [
    {"task": "Прочитать статью", "type": "Учеба"},
    {"task": "Сделать зарядку", "type": "Спорт"},
    {"task": "Поработать над проектом", "type": "Работа"},
    {"task": "Выпить воды", "type": "Здоровье"},
    {"task": "Изучить новую тему", "type": "Учеба"},
    {"task": "Пробежка", "type": "Спорт"},
]

class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор задач")
        self.root.geometry("400x500")

        self.history = []
        self.load_data()

        # Интерфейс
        self.label = tk.Label(root, text="Нажмите кнопку, чтобы получить задачу", font=("Arial", 12))
        self.label.pack(pady=10)

        self.btn_gen = tk.Button(root, text="Сгенерировать задачу", command=self.generate_task, bg="#4CAF50", fg="white")
        self.btn_gen.pack(pady=5)

        # Фильтрация
        filter_frame = tk.Frame(root)
        filter_frame.pack(pady=10)
        tk.Label(filter_frame, text="Фильтр:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar(value="Все")
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=["Все", "Учеба", "Спорт", "Работа", "Здоровье"])
        self.filter_combo.pack(side=tk.LEFT)
        self.filter_combo.bind("<<ComboboxSelected>>", self.update_history_list)

        # Список истории
        self.history_listbox = tk.Listbox(root, width=50, height=15)
        self.history_listbox.pack(pady=10)
        
        self.update_history_list()

    def generate_task(self):
        task = random.choice(PREDEFINED_TASKS)
        self.history.append(task)
        self.save_data()
        self.update_history_list()
        self.label.config(text=f"Задача: {task['task']} ({task['type']})")

    def update_history_list(self, event=None):
        self.history_listbox.delete(0, tk.END)
        filter_type = self.filter_var.get()
        
        for item in reversed(self.history):
            if filter_type == "Все" or item['type'] == filter_type:
                self.history_listbox.insert(tk.END, f"{item['type']}: {item['task']}")

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.history = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGeneratorApp(root)
    root.mainloop()
