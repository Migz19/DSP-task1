import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def open_file():
    filepath1 = filedialog.askopenfilename(title="Select File")
    if filepath1:
        process_signal(filepath1)

def process_signal(filepath1):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()

    data1 = [line.split() for line in lines1[3:]]
    data1 = np.array(data1, dtype=float)

    time = np.arange(0, len(data1))

    number1 = data1[:, 0]

    shifted_signal = number1 + constant

    plt.subplot(2, 1, 1)
    plt.plot(time, shifted_signal)
    plt.title('Shifting')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

def set_constant(value):
    global constant
    constant = float(value)

myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Shifting Signal")
myfram.configure(bg="antiquewhite2")

Shifting_label = tk.Label(myfram, text="Shifting", width=20)
Shifting_label.pack(pady=10)

constant_label = tk.Label(myfram, text="Enter Shift Constant:")
constant_label.pack(pady=10)

constant_entry = tk.Entry(myfram)
constant_entry.pack()

constant_button = tk.Button(myfram, text="Set Constant", command=lambda: set_constant(constant_entry.get()))
constant_button.pack()

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white", fg="black", width=15)
mybutton.pack(padx=20, pady=50)

myfram.mainloop()
