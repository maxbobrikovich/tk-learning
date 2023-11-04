import tkinter as tk

clicks = 0

# Create a function to be called when the button is clicked
def button_click():
    global clicks
    clicks = clicks + 1
    
    label.config(text=clicks)

# Create the main window
window = tk.Tk()
window.title("Multiplication Window")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Create a button
button = tk.Button(window, text="Hi, there can you click me? ", command=button_click)
button.pack()

# Start the main event loop
window.mainloop()