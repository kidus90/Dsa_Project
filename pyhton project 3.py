import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.front = None
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.front is None

    def search(self, value):
        current = self.front
        while current is not None:
            if current.value == value:
                print("Value found: True")
                return True
            if current.next is None:
                break
            current = current.next
        print("Value not found: False")
        return False

    def get(self, value):
        if self.search(value):
            self.remove_node(value)
        self.put(value)

    def put(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        self.size += 1

        if self.size > self.capacity:
            current_node = self.front
            previous_node = None
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next

            if previous_node:
                previous_node.next = None
            else:
                self.front = None
            self.size -= 1

    def remove_node(self, value):
        prev = None
        current_node = self.front

        if current_node is None:
            return

        if current_node.value == value:
            self.front = current_node.next
            self.size -= 1
            return

        while current_node is not None and current_node.value != value:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        self.size -= 1

    def display(self):
        f = self.front
        print("LRU Cache starts here")
        print("_______________________")
        while f is not None:
            print(f.value)
            f = f.next
        print("_______________________\n")

def add_word():
    if lru_cache is None:
        messagebox.showerror("Error", "Please set the capacity first.")
        return
    word = entry.get()
    lru_cache.get(word)
    lru_cache.display()
    update_table()

def set_capacity():
    global lru_cache
    try:
        cap = int(capacity_entry.get())
        lru_cache = LRUCache(cap)
        capacity_entry.config(state='disabled')
        set_capacity_button.config(state='disabled')
        create_table(cap)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid capacity")

def reset():
    global lru_cache
    lru_cache = None
    capacity_entry.config(state='normal')
    capacity_entry.delete(0, tk.END)
    set_capacity_button.config(state='normal')
    for i in table.get_children():
        table.delete(i)

def create_table(capacity):
    global table
    table = ttk.Treeview(UI_frame, columns=["0"], show='headings', height=capacity)
    table.heading("0", text="LRU Cache")
    table.column("0", width=100)
    table.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

def update_table():
    global table
    for i in table.get_children():
        table.delete(i)
    values = []
    current = lru_cache.front
    while current is not None:
        values.append(current.value)
        current = current.next
    for value in values:
        table.insert('', 'end', values=[value])

root = tk.Tk()
root.title('LRU Cache')
root.maxsize(1000, 900)

UI_frame = tk.Frame(root, width=600, height=200, bg='light grey')
UI_frame.pack(padx=10, pady=10)

tk.Label(UI_frame, text="Please enter a word: ", bg='light grey').grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(UI_frame)
entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(UI_frame, text="Please enter capacity: ", bg='light grey').grid(row=1, column=0, padx=10, pady=5)
capacity_entry = tk.Entry(UI_frame)
capacity_entry.grid(row=1, column=1, padx=10, pady=5)

set_capacity_button = tk.Button(UI_frame, text="Set Capacity", command=set_capacity)
set_capacity_button.grid(row=1, column=2, padx=10, pady=5)

tk.Button(UI_frame, text="Add Word", command=add_word).grid(row=0, column=2, padx=10, pady=5)

reset_button = tk.Button(UI_frame, text="Reset", command=reset)
reset_button.grid(row=3, column=2, padx=10, pady=5)

lru_cache = None

if __name__ == "__main__":
    root.mainloop()
