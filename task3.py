import numpy as np
import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Functions
# ------------------------------
def get_matrices():
    try:
        m1 = np.array([[int(e.get()) for e in row] for row in entries1])
        m2 = np.array([[int(e.get()) for e in row] for row in entries2])
        return m1, m2
    except:
        messagebox.showerror("Error", "Please enter valid numbers")
        return None, None

def show_result(result, title):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{title}:\n{result}")

def add():
    m1, m2 = get_matrices()
    if m1 is not None:
        show_result(m1 + m2, "Addition")

def subtract():
    m1, m2 = get_matrices()
    if m1 is not None:
        show_result(m1 - m2, "Subtraction")

def multiply():
    m1, m2 = get_matrices()
    if m1 is not None:
        try:
            show_result(np.dot(m1, m2), "Multiplication")
        except:
            messagebox.showerror("Error", "Invalid dimensions for multiplication")

def transpose():
    m1, _ = get_matrices()
    if m1 is not None:
        show_result(m1.T, "Transpose (Matrix 1)")

def determinant():
    m1, _ = get_matrices()
    if m1 is not None:
        if m1.shape[0] == m1.shape[1]:
            show_result(np.linalg.det(m1), "Determinant")
        else:
            messagebox.showerror("Error", "Matrix must be square")

# ------------------------------
# GUI Setup
# ------------------------------
root = tk.Tk()
root.title("Matrix Operations Tool")

rows, cols = 2, 2  # you can change size here

entries1 = []
entries2 = []

# Matrix 1
tk.Label(root, text="Matrix 1").grid(row=0, column=0, columnspan=cols)
for i in range(rows):
    row_entries = []
    for j in range(cols):
        e = tk.Entry(root, width=5)
        e.grid(row=i+1, column=j)
        row_entries.append(e)
    entries1.append(row_entries)

# Matrix 2
tk.Label(root, text="Matrix 2").grid(row=0, column=cols+1, columnspan=cols)
for i in range(rows):
    row_entries = []
    for j in range(cols):
        e = tk.Entry(root, width=5)
        e.grid(row=i+1, column=j+cols+1)
        row_entries.append(e)
    entries2.append(row_entries)

# Buttons
tk.Button(root, text="Add", command=add).grid(row=rows+2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=rows+2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=rows+2, column=2)
tk.Button(root, text="Transpose", command=transpose).grid(row=rows+2, column=3)
tk.Button(root, text="Determinant", command=determinant).grid(row=rows+2, column=4)

# Result box
result_text = tk.Text(root, height=8, width=40)
result_text.grid(row=rows+3, column=0, columnspan=cols*2+1)

root.mainloop()