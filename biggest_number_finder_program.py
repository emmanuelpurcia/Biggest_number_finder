# A Program that asks the user to input THREE NUMBERS ONLY.
# Then the program itself will determine and print the BIGGEST NUMBER among the three given numbers by the user.

# pseudocode 

# Import the Tkinter Font Art
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Coolest Number Finder")
window.geometry("800x300")

# Create a tkinter canvas
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# Create a tkinter font for the welcome message and the output
cool_font = ("Helvetica", 20, "bold")

# Create a tkinter label for the welcome message
welcome_label = tk.Label(window, text="WELCOME TO PYTHON'S BIGGEST NUMBER FINDER!", font=cool_font)
canvas.create_window(200, 50, window=welcome_label)

# Create tkinter entry boxes for the input numbers
# Create a tkinter function to find the largest number
    # Use the if-else statement to find the largest number
    # Create a tkinter label for the output with the largest number
    # Create a tkinter button to close the window
# Create a tkinter button to find the largest number
# Run the tkinter window