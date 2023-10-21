import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog


def open_file():
    filepath1 = filedialog.askopenfilename(title="Select File")
    if filepath1:
        process_signal(filepath1)


def normalize_signal(signal, normalization_type):
    if normalization_type == "0_to_1":
        min_val = np.min(signal)
        max_val = np.max(signal)
        normalized_signal = (signal - min_val) / (max_val - min_val)
    elif normalization_type == "-1_to_1":
        max_abs_val = np.max(np.abs(signal))
        normalized_signal = (signal / max_abs_val) * 2 - 1
    return normalized_signal


def process_signal(filepath1):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()

    data1 = [line.split() for line in lines1[3:]]
    data1 = np.array(data1, dtype=float)

    time = np.arange(0, len(data1))
    number1 = data1[:, 1]

    normalization_choice = normalization_var.get()

    normalized_signal = normalize_signal(number1, normalization_choice)
    print(normalized_signal)
    plt.subplot(2, 1, 1)
    plt.plot(time, normalized_signal)
    plt.title('Normalized Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


myfram = tk.Tk()
myfram.geometry("400x400")
myfram.title("Normalization of Signal")
myfram.configure(bg="khaki3")

constant_label = tk.Label(myfram, text="Choose Normalization Type:")
constant_label.pack(pady=10)

normalization_var = tk.StringVar(value="0_to_1")
tk.Radiobutton(myfram, text="0 to 1", variable=normalization_var,value="0_to_1").pack()
tk.Radiobutton(myfram, text="-1 to 1", variable=normalization_var,value="-1_to_1").pack(pady=20)

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white",
                     fg="black", width=15)
mybutton.pack(padx=20, pady=50)

myfram.mainloop()