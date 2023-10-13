
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(title="Select File")
    if filepath:
        process_signal(filepath)

def process_signal(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().splitlines()

    signal_type = int(lines[0])
    is_periodic = int(lines[1])
    n_samples_or_freqs = int(lines[2])

    data = [line.split() for line in lines[3:]]
    data = np.array(data, dtype=float)

    if signal_type == 0:
        timediscrete = data[:, 0]
        signal_discrete = data[:, 1]

        time_continuous = np.linspace(0, timediscrete[-1], 1000)

        signal_continuous = np.interp(time_continuous, timediscrete, signal_discrete)

        plt.subplot(2, 1, 1)
        plt.stem(timediscrete, signal_discrete)
        plt.title('Discrete Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

        plt.subplot(2, 1, 2)
        plt.plot(time_continuous, signal_continuous)
        plt.title('Continuous Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

        plt.tight_layout()

        plt.show()



    else:
        print("Invalid signal type specified in the file.")

myfram = tk.Tk()
myfram.geometry("300x300")
myfram.title("choose file")
myfram.configure(bg="grey")

mybutton = tk.Button(myfram, text="Open File", command=open_file,bg="black",fg="white")
mybutton.pack(pady=100)

myfram.mainloop()

