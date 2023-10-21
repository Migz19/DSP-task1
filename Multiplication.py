import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def open_file():
    filepath1 = filedialog.askopenfilename(title="Select File 1")
    if filepath1:

            process_signal(filepath1, constant)


def process_signal(filepath1, constant):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()


    data1 = [line.split() for line in lines1[3:]]
    data1 = np.array(data1, dtype=float)





    time = np.arange(0, len(data1))

    number1 = data1[:, 1]

    multiplied_signal = constant * (number1)

    print(multiplied_signal)
    plt.subplot(2, 1, 1)
    plt.plot(time, multiplied_signal)
    plt.title('Multiplied Signal')
    plt.xlabel('Time')
    plt.ylabel('Multiplication')
    plt.tight_layout()
    plt.show()

def set_constant(value):
    global constant
    constant = float(value)

myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Choose Files and Constant")
myfram.configure(bg="green")

constant_label = tk.Label(myfram, text="Enter Constant Value:")
constant_label.pack(pady=10)

constant_entry = tk.Entry(myfram)
constant_entry.pack()

constant_button = tk.Button(myfram, text="Set Constant", command=lambda: set_constant(constant_entry.get()))
constant_button.pack(pady=10)

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="black", fg="white",width=17)
mybutton.pack(padx=20,pady=50,)



myfram.mainloop()
