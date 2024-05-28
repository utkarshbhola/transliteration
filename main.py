from ai4bharat.transliteration import XlitEngine
import tkinter as tk
from tkinter import ttk  # For Combobox widget


# Define selected_language and user_input as global variables
selected_language = ""
user_input = ""
user_output = ""

def process_input():
    global selected_language, user_input, user_output

    """
    Processes the user input and selected language.

    This function retrieves the text from the input area and the selected language
    from the dropdown, performs transliteration, and updates the output area with them.
    """

    user_input = text_area.get("1.0", "end-1c")
    selected_language = language_var.get()

    # Perform transliteration
    ai4()

    # Update the output text area
    output_text.config(state="normal")  # Enable editing the output area
    output_text.delete("1.0", "end")  # Clear previous output
    output_text.insert("1.0", f"Input: {user_input}\nSelected Language: {selected_language}\nOutput: {user_output}")
    output_text.config(state="disabled")  # Disable editing the output area

def ai4():
    global user_output
    if selected_language == "Hindi":
        e = XlitEngine("hi")
    elif selected_language == "Konkani Goan":
        e = XlitEngine("gom")
    elif selected_language == "Gujarati":
        e = XlitEngine("gu")
    elif selected_language == "Bengali":
        e = XlitEngine("bn")
    elif selected_language == "Kannada":
        e = XlitEngine("kn")
    elif selected_language == "Maithili":
        e = XlitEngine("mai")
    elif selected_language == "Malayalam":
        e = XlitEngine("ml")
    elif selected_language == "Marathi":
        e = XlitEngine("mr")
    elif selected_language == "Punjabi":
        e = XlitEngine("pa")
    elif selected_language == "Sindhi":
        e = XlitEngine("sd")
    elif selected_language == "Sinhala":
        e = XlitEngine("si")
    elif selected_language == "Tamil":
        e = XlitEngine("ta")
    elif selected_language == "Telugu":
        e = XlitEngine("te")
    elif selected_language == "Urdu":
        e = XlitEngine("ur")
    elif selected_language == "Oriya":
        e = XlitEngine("or")
    else:
        user_output = "Unsupported language"
        return

    user_output = e.translit_sentence(user_input)

# Create the main window
root = tk.Tk()
root.title("Input Box")

# Create input area
text_area = tk.Text(root, height=5, width=50)
text_area.pack(pady=10)

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

# Start the main event loop
root.mainloop()
