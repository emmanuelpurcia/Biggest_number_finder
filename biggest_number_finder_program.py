# A Program that asks the user to input THREE NUMBERS ONLY.
# Then the program itself will determine and print the BIGGEST NUMBER among the three given numbers by the user.

# pseudocode 

# Import the Tkinter Font Art
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("BIGGEST NUMBER FINDER")
window.geometry("750x250")

# Set the color theme
window.configure(bg="lightblue")

# Create a tkinter canvas
canvas = tk.Canvas(window, width=400, height=300, bg="lightblue", highlightthickness=0)
canvas.pack()

# Create a tkinter font for the welcome message and the output
cool_font = ("Comic Sans MS", 12, "bold")

# Create a tkinter label for the welcome message
welcome_label = tk.Label(window, text="WELCOME USER! PLEASE INPUT ANY NUMBER TO THE THREE EMPTY BOXES BELOW!", font=cool_font, fg="black", bg="white")
canvas.create_window(200, 50, window=welcome_label)

# Create tkinter entry boxes for the input numbers
num1_entry = tk.Entry(window, width=5, font=cool_font, bg="white", fg="black")
canvas.create_window(100, 120, window=num1_entry)

num2_entry = tk.Entry(window, width=5, font=cool_font, bg="white", fg="black")
canvas.create_window(200, 120, window=num2_entry)

num3_entry = tk.Entry(window, width=5, font=cool_font, bg="white", fg="black")
canvas.create_window(300, 120, window=num3_entry)

# Create a tkinter function to find the largest number
def find_largest():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    num3 = float(num3_entry.get())

    # Using if-else statement to find the largest number
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    else:
        largest = max(num2, num3)

    # Create a tkinter label for the output
    output_label = tk.Label(window, text=f"THE BIGGEST NUMBER AMONG THE THREE INPUTTED NUMBERS IS {largest:.0f}! 🤘", font=cool_font, fg="black", bg="lightblue")
    canvas.create_window(200, 220, window=output_label)

# Create a tkinter button to find the largest number
find_button = tk.Button(window, text="CLICK HERE TO DETERMINE THE BIGGEST NUMBER", command=find_largest, font=cool_font, bg="black", fg="white")
canvas.create_window(200, 170, window=find_button)

# Run the tkinter window
window.mainloop()