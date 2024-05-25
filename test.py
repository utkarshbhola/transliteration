import tkinter as tk
from tkinter import ttk  # For Combobox widget
# Define selected_language and user_input as global variables
selected_language = ""
user_input = ""
def process_input():
  global selected_language, user_input
  """
  Processes the user input and selected language.

  This function retrieves the text from the input area and the selected language
  from the dropdown and prints them to the console for demonstration purposes.
  You can replace this logic with your desired actions based on the input and language.
  """

  user_input = text_area.get("1.0", "end-1c")
  selected_language = language_var.get()

  print("Input:", user_input)
  print("Selected Language:", selected_language)

  # Add your code to process the input and language here

# Create the main window
root = tk.Tk()
root.title("Input Box")

# Create input area
text_area = tk.Text(root, height=5, width=50)
text_area.pack(pady=10)

# Create label for output
output_label = tk.Label(root, text="Output:")
output_label.pack()

# Create output text area (initially empty)
output_text = tk.Text(root, height=5, width=50, state="disabled")
output_text.pack()

# Create dropdown for language selection
languages = ["English", "Hindi", "Sanskrit", "Oriya", "Konkani Goan", "Gujarati", "Bengali", "Kannada", "Maithili", "Malayalam", "Marathi", "Punjabi", "Sindhi", "Sinhala", "Tamil", "Telugu", "Urdu"]
language_var = tk.StringVar(root)
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=languages)
language_dropdown.pack()

# Create a button to trigger processing
process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack(pady=10)
import tkinter as tk

# Create the main window (root)
root = tk.Tk()
root.title("Translator")

# Create the output label before mainloop
output_label = tk.Label(root, text="This is the initial output.")
output_label.pack()

root.mainloop()
