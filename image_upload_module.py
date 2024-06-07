import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename() # 选择并读取文件路径
    root.destroy()  # 关闭主窗口
    return file_path
