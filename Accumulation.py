import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

# Define the accumulation function
def accumulation(x_values, y_values):
    result_data_y = []
    cumulative_sum = y_values[0]

    for i in range(1, len(x_values)):
        cumulative_sum += y_values[i]
        result_data_y.append(cumulative_sum)


    if len(x_values) > len(result_data_y):
        x_values = x_values[:len(result_data_y)]
    elif len(x_values) < len(result_data_y):
        result_data_y = result_data_y[:len(x_values)]

    return x_values, result_data_y

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

    # Perform accumulation
    x_values, accumulated_data = accumulation(time, number1)
    print(accumulated_data)

    plt.subplot(2, 1, 1)
    plt.plot(x_values, accumulated_data)
    plt.title('Accumulation')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Accumulation Signal")
myfram.configure(bg="antiquewhite2")






mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white", fg="black", width=15)
mybutton.pack(padx=20, pady=50)

myfram.mainloop()
