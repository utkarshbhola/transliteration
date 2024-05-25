from ai4bharat.transliteration import XlitEngine
import tkinter as tk
from tkinter import ttk  # For Combobox widget
# Define selected_language and user_input as global variables
selected_language = ""
user_input = ""
user_output=""
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

root.mainloop()

# Now you can access selected_language and user_input outside the function
print("User Input:", user_input)
print("Selected Language:", selected_language)
print("User Output:",user_output)
def ai4():
    global user_output
    if (selected_language == "Hindi"):
        e = XlitEngine("hi")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Konkani Goan"):
        e = XlitEngine("gom")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Gujarati"):
        e = XlitEngine("gu")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Bengali"):
        e = XlitEngine("bn")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Kannada"):
        e = XlitEngine("kn")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Maithili"):
        e = XlitEngine("mai")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Malayalam"):
        e = XlitEngine("ml")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Marathi"):
        e = XlitEngine("mr")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Punjabi"):
        e = XlitEngine("pa")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Sindhi"):
        e = XlitEngine("sd")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Sinhala"):
        e = XlitEngine("si")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Tamil"):
        e = XlitEngine("ta")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Telugu"):
        e = XlitEngine("te")
        out = e.translit_sentence(user_input)
        print(out)

    elif(selected_language == "Urdu"):
        e = XlitEngine("ur")
        out = e.translit_sentence(user_input)
        print(out)


    elif(selected_language == "Oriya"):
        e = XlitEngine("or")
        out = e.translit_sentence(user_input)
        print(out)

print("User Output:",user_output)
output_label = tk.Label(root, text="This is the initial output.")
output_label.pack()

#def process_input():
  # ... your logic to calculate the output text
 # output_text = "The calculated output is: " + str(result)
  #output_label.config(text=output_text)

