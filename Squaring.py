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

    number1 = data1[:, 1]

    squaring = number1 *number1

    print(squaring)
    plt.subplot(2, 1, 1)
    plt.plot(time, squaring)
    plt.title('Squaring')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Squaring Signal")
myfram.configure(bg="aquamarine4")

squaring_label = tk.Label(myfram, text="Squaring", width=20)
squaring_label.pack(pady=10)

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white",
                     fg="black", width=15)
mybutton.pack(padx=20, pady=50)

myfram.mainloop()
