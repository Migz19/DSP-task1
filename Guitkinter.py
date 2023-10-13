# import math
# from tkinter import *
# import numpy as np
# import matplotlib.pyplot as plt
# from tkinter import messagebox
#
# myfram = Tk()
# myfram.title('main')
# myfram.geometry("600x600")
# myfram.configure(bg="black")
#
# def generatesignal():
#     signaltype = signal_type_entry.get()
#     amplitude = float(Amplitude_entry.get())
#     phaseshift=float(phase_shift_entry.get())
#     analogfrequency = float(Analog_frequancy_Entry.get())
#     samplingfrequency = float(sample_frequancy_entry.get())
#     t = np.linspace(0, 1, num=1000)
#     n = np.arange(0, 10)
#     phaseshift = math.radians(phaseshift)  # Convert to radians
#     if samplingfrequency < (2 * analogfrequency):
#         messagebox.showinfo("Alert","The sampling frequency must be greater than 2 * analog frequency.")
#     else:
#         viewsignal(t, n, phaseshift, signaltype, amplitude, analogfrequency, samplingfrequency)
#
# def viewsignal(t, n, phaseshift, signaltype, amplitude, analogfrequency, samplingfrequency):
#     if signaltype == 'sin':
#         analogsignal = amplitude * np.sin(2 * np.pi * analogfrequency * t + phaseshift)
#         digitalsignal = amplitude * np.sin(2 * np.pi * (analogfrequency * n) / samplingfrequency + phaseshift)
#     else:
#         analogsignal = amplitude * np.cos(2 * np.pi * analogfrequency * t + phaseshift)
#         digitalsignal = amplitude * np.sin(2 * np.pi * (analogfrequency * n) / samplingfrequency + phaseshift)
#
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
#
#     # Plot the analog signal in the first subplot (ax1)
#     ax1.plot(t, analogsignal, label="Analog Signal")
#     ax1.set_title(f"{signaltype.capitalize()} (Analog)")
#     ax1.set_xlabel("Time (s)")
#     ax1.set_ylabel("Amplitude")
#     ax1.grid(True)
#     ax1.legend()
#
#     # Plot the digital signal in the second subplot (ax2)
#     ax2.stem(n, digitalsignal, label="Digital Signal")
#     ax2.set_title(f"{signaltype.capitalize()} (Digital)")
#     ax2.set_xlabel("Time (s)")
#     ax2.set_ylabel("Amplitude")
#     ax2.grid(True)
#     ax2.legend()
#
#     # Adjust the spacing between subplots
#     plt.tight_layout()
#
#     # Show the figure with both subplots
#     plt.show()
#
# lb1 = Label(myfram, text="Enter data of the signal", fg="white", bg="black")
# lb1.pack(pady=30)
#
# lb2 = Label(myfram, text="Signal Type", fg="white", bg="black")
# lb2.pack(side=TOP)
# signal_type_entry = Entry(myfram)
# signal_type_entry.pack(pady=10)
#
# lb3 = Label(myfram, text="Amplitude", fg="white", bg="black")
# lb3.pack(side=TOP)
# Amplitude_entry = Entry(myfram)
# Amplitude_entry.pack(pady=10)
#
# lb4 = Label(myfram, text="Phase Shift (degrees)", fg="white", bg="black")
# lb4.pack(side=TOP)
# phase_shift_entry = Entry(myfram)
# phase_shift_entry.pack(pady=10)
#
# lb5 = Label(myfram, text="Analog Frequency", fg="white", bg="black")
# lb5.pack(side=TOP)
# Analog_frequancy_Entry = Entry(myfram)
# Analog_frequancy_Entry.pack(pady=10)
#
# lb6 = Label(myfram, text="Sampling Frequency", fg="white", bg="black")
# lb6.pack(side=TOP)
# sample_frequancy_entry = Entry(myfram)
# sample_frequancy_entry.pack(pady=10)
#
# mybutton = Button(myfram, text="View Signal", fg="black", bg="yellow", command=generatesignal)
# mybutton.pack()
#
# myfram.mainloop()
import math
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

myfram = Tk()
myfram.title('main')
myfram.geometry("600x600")
myfram.configure(bg="black")


def generatesignal(signaltype, amplitude, phaseshift, analogfrequency, samplingfrequency):
    # t = np.linspace(0, 1, num=1000)  # Increase the number of points for smoother curves
    t=np.arange(0,1,0.001)
    n = np.arange(0, 10)

    if signaltype == 'sin':
        analogsignal = amplitude * np.sin(2 * np.pi * analogfrequency * t + phaseshift)
        digitalsignal = amplitude * np.sin(2 * np.pi * (analogfrequency * n / samplingfrequency) + phaseshift)
    elif signaltype == 'cos':
        analogsignal = amplitude * np.cos(2 * np.pi * analogfrequency * t + phaseshift)
        digitalsignal = amplitude * np.sin(2 * np.pi * (analogfrequency * n / samplingfrequency) + phaseshift)

    return t, analogsignal, digitalsignal, n


def viewsignal():
    signaltype = signal_type_entry.get()
    amplitude = float(Amplitude_entry.get())
    phaseshift = math.radians(float(phase_shift_entry.get()))  # Convert to radians
    analogfrequency = float(Analog_frequancy_Entry.get())
    samplingfrequency = float(sample_frequancy_entry.get())

    if samplingfrequency < (2 * analogfrequency):
        messagebox.showinfo("Alert","The sampling frequency must be greater than 2 * analog frequency.")
    else:
        t, analogsignal, digitalsignal, n = generatesignal(signaltype, amplitude,phaseshift,analogfrequency,samplingfrequency)



    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    ax1.plot(t, analogsignal, label="Analog Signal")
    ax1.set_title(f"{signaltype.capitalize()} (Analog)")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    ax1.legend()

    # Plot the digital signal in the second subplot (ax2)
    ax2.stem(n, digitalsignal, label="Digital Signal")
    ax2.set_title(f"{signaltype.capitalize()} (Digital)")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()

    plt.show()


lb1 = Label(myfram, text="Enter data of the signal", fg="white", bg="black")
lb1.pack(pady=30)

lb2 = Label(myfram, text="Signal Type", fg="white", bg="black")
lb2.pack(side=TOP)
signal_type_entry = Entry(myfram)
signal_type_entry.pack(pady=10)

lb3 = Label(myfram, text="Amplitude", fg="white", bg="black")
lb3.pack(side=TOP)
Amplitude_entry = Entry(myfram)
Amplitude_entry.pack(pady=10)

lb4 = Label(myfram, text="Phase Shift (degrees)", fg="white", bg="black")
lb4.pack(side=TOP)
phase_shift_entry = Entry(myfram)
phase_shift_entry.pack(pady=10)

lb5 = Label(myfram, text="Analog Frequency", fg="white", bg="black")
lb5.pack(side=TOP)
Analog_frequancy_Entry = Entry(myfram)
Analog_frequancy_Entry.pack(pady=10)

lb6 = Label(myfram, text="Sampling Frequency", fg="white", bg="black")
lb6.pack(side=TOP)
sample_frequancy_entry = Entry(myfram)
sample_frequancy_entry.pack(pady=10)

mybutton = Button(myfram, text="View Signal", fg="black", bg="yellow",command=viewsignal)
mybutton.pack()

myfram.mainloop()
