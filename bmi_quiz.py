import tkinter as tk

root = tk.Tk()
root.title("BMI Quiz")

# root variables
window_width = 770
window_height = 375
x = (root.winfo_screenwidth() // 2) - (window_width // 2)
y = (root.winfo_screenheight() // 2) - (window_height // 2)

style = ('Calibri', 14, 'normal')
heading_style = ('Calibri', 20, 'bold')
bmi_heading_style = ('Calibri', 18, 'bold', 'underline'),

input_background_color = "#353b48"
input_text_color = "#ecf0f1"

bmi_background_color = "#353b48"
bmi_text_color = "#ecf0f1"

result: str
input_frame = tk.Frame(root, bg=input_background_color)
bmi_frame = tk.Frame(root, bg=input_background_color)


def calculate_bmi():
    global result
    if (weight_entry.get() == "" or height_entry.get() == ""):
        result = "Enter both weight and height!"
        set_result_label(result)
    else:
        if (weight_entry.get().isnumeric() and height_entry.get().isnumeric()):
            bmi = int(weight_entry.get()) / ((int(height_entry.get()) / 100) ** 2)
            bmi = round(bmi, 2)
            body_type = get_body_type(bmi)
            result = f"Your BMI is {bmi}. You are {body_type}"
            set_result_label(result)
        else:
            result = "Enter a valid number!"
            set_result_label(result)

def get_body_type(bmi):
    if bmi <= 16:
        return "Severely Underweight"
    elif bmi > 16 and bmi <= 18.4:
        return "Underweight"
    elif bmi > 18.4 and bmi <= 24.9:
        return "Normal"
    elif bmi > 24.9 and bmi <= 29.9:
        return "Overweight"
    elif bmi > 29.9 and bmi <= 34.9:
        return "Moderately Obese"
    elif bmi > 34.9 and bmi <= 39.9:
        return "Severely Obese"
    elif bmi > 39.9:
        return "Morbidly Obese"

def set_root_and_frames():
    # root settings
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)
    root.config(background="#2f3640", padx=10, pady=10)

    # input frame
    input_frame.pack(side='left', fill='y')

    # bmi frame
    bmi_frame.pack(side='right', fill='y')

# Global Widgets
heading_label = tk.Label(input_frame, text="Py Tkinter - Adult BMI Calculator", fg="#FFFDFD", bg="#B64B38", font=heading_style, width=27)
weight_label = tk.Label(input_frame, text="Enter Your Weight (kg): ", fg=input_text_color, bg=input_background_color, font=style)
weight_entry = tk.Entry(input_frame, font=style, borderwidth=0)
height_label = tk.Label(input_frame, text="Enter Your Height (cm): ", fg=input_text_color, bg=input_background_color, font=style)
height_entry = tk.Entry(input_frame, font=style, borderwidth=0)
calculate_button = tk.Button(input_frame, text="Calculate!", command=calculate_bmi, font=style, width=40, fg=input_text_color, bg=input_background_color, borderwidth=2, relief="groove")
result_label = tk.Label(input_frame, text="", font=style, fg=input_text_color, bg=input_background_color)

def set_inputs():
    heading_label.grid(row=0, column=0, columnspan=2,padx=10, pady=(30,10))
    weight_label.grid(row=1, column=0, padx=10, pady=10)
    weight_entry.grid(row=1, column=1, padx=10, pady=10)
    height_label.grid(row=2, column=0, padx=10, pady=10)
    height_entry.grid(row=2, column=1, padx=10, pady=10)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=25)

def set_result_label(_text):
    global result_label
    result_label.config(text=_text)

def set_bmi_frame():
    bmi_label = tk.Label(bmi_frame, text="BMI", font=bmi_heading_style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation1 = tk.Label(bmi_frame, text="< 16.0", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation2 = tk.Label(bmi_frame, text="16.0 - 18.4", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation3 = tk.Label(bmi_frame, text="18.5 - 24.9", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation4 = tk.Label(bmi_frame, text="25.0 - 29.9", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation5 = tk.Label(bmi_frame, text="30.0 - 34.9", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation6 = tk.Label(bmi_frame, text="35.0 - 39.9", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_situation7 = tk.Label(bmi_frame, text="> 40.0", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label.grid(row=0, column=0, padx=10, pady=8)
    bmi_label_situation1.grid(row=1, column=0, padx=10, pady=8)
    bmi_label_situation2.grid(row=2, column=0, padx=10, pady=8)
    bmi_label_situation3.grid(row=3, column=0, padx=10, pady=8)
    bmi_label_situation4.grid(row=4, column=0, padx=10, pady=8)
    bmi_label_situation5.grid(row=5, column=0, padx=10, pady=8)
    bmi_label_situation6.grid(row=6, column=0, padx=10, pady=8)
    bmi_label_situation7.grid(row=7, column=0, padx=10, pady=8)

    category_label = tk.Label(bmi_frame, text="Category", font=bmi_heading_style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category1 = tk.Label(bmi_frame, text="Severely Underweight", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category2 = tk.Label(bmi_frame, text="Underweight", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category3 = tk.Label(bmi_frame, text="Normal", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category4 = tk.Label(bmi_frame, text="Overweight", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category5 = tk.Label(bmi_frame, text="Moderately Obese", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category6 = tk.Label(bmi_frame, text="Severely Obese", font=style, bg=bmi_background_color, fg=bmi_text_color)
    bmi_label_category7 = tk.Label(bmi_frame, text="Morbidly Obese", font=style, bg=bmi_background_color, fg=bmi_text_color)
    category_label.grid(row=0, column=1, padx=10, pady=8)
    bmi_label_category1.grid(row=1, column=1, padx=10, pady=8)
    bmi_label_category2.grid(row=2, column=1, padx=10, pady=8)
    bmi_label_category3.grid(row=3, column=1, padx=10, pady=8)
    bmi_label_category4.grid(row=4, column=1, padx=10, pady=8)
    bmi_label_category5.grid(row=5, column=1, padx=10, pady=8)
    bmi_label_category6.grid(row=6, column=1, padx=10, pady=8)
    bmi_label_category7.grid(row=7, column=1, padx=10, pady=8)
set_bmi_frame()
set_root_and_frames()
set_inputs()

root.mainloop()