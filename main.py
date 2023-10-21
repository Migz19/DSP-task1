# import tkinter as tk
# import matplotlib.pyplot as plt
# import numpy as np
# from tkinter import filedialog
#
#
# def open_file():
#     filepath = filedialog.askopenfilename(title="Select File")
#     if filepath:
#         process_signal(filepath)
#
#
# def process_signal(filepath,filepath2):
#     with open(filepath, 'r') as file:
#         lines = file.read().splitlines()
#
#
#     data = [line.split() for line in lines[3:]]
#     data = np.array(data, dtype=float)
#
#
#
#     time = np.arange(0, len(data))
#
#     number1 = data[:, 1]
#     number2 = data2[:, 1]
#
#     add=number1+number2
#
#     print(add)
#     plt.subplot(2, 1, 1)
#     plt.plot(time, add)
#     plt.title(' Add')
#     plt.xlabel('Time')
#     plt.ylabel('sum')
#     plt.tight_layout()
#
#     plt.show()
#
# myfram = tk.Tk()
# myfram.geometry("300x300")
# myfram.title("choose file")
# myfram.configure(bg="yellow")
#
# mybutton = tk.Button(myfram, text="Open File", command=open_file,bg="black",fg="white")
# mybutton.pack(pady=100)
#
#
# myfram.mainloop()
#

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def open_file():
    global filepath1
    filepath1 = filedialog.askopenfilename(title="Select File 1")
    if filepath1:
        if 'filepath2' in globals():
            process_signal(filepath1, filepath2)
        else:
            print("Please select the second file.")

def open_file2():
    global filepath2
    filepath2 = filedialog.askopenfilename(title="Select File 2")
    if filepath2:
        if 'filepath1' in globals():
            process_signal(filepath1, filepath2)
        else:
            print("Please select the first file.")

def process_signal(filepath1, filepath2):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()
    with open(filepath2, 'r') as file2:
        lines2 = file2.read().splitlines()

    data1 = [line.split() for line in lines1[3:]]
    data1 = np.array(data1, dtype=float)

    data2 = [line.split() for line in lines2[3:]]
    data2 = np.array(data2, dtype=float)

    if len(data1) != len(data2):
        print("Error: The two files must have the same number of data points.")
        return

    time = np.arange(0, len(data1))

    number1 = data1[:, 1]
    number2 = data2[:, 1]

    add = number1 + number2

    print(add)
    plt.subplot(2, 1, 1)
    plt.plot(time, add)
    plt.title('Sum of Columns')
    plt.xlabel('Time')
    plt.ylabel('Sum')
    plt.tight_layout()
    plt.show()

myfram = tk.Tk()
myfram.geometry("300x300")
myfram.title("Choose Files")
myfram.configure(bg="thistle4")

mybutton = tk.Button(myfram, text="Open File 1", command=open_file, bg="black", fg="white")
mybutton.pack(side="left",padx=40)

mybutton2 = tk.Button(myfram, text="Open File 2", command=open_file2, bg="white", fg="black")
mybutton2.pack(side="right",padx=40)

myfram.mainloop()

