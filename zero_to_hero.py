from langchain import OpenAI
import pandas as pd
from langchain.agents import create_csv_agent
import tkinter as tk
from PIL import Image, ImageTk

results = []

csv_path = 'YOUR CSV PATH'
chat_gpt_api_key = 'YOUR API KEY'

type_of_arifical_intelligence_model = 'text-davinci-003'
#you can change openAI model name. Davinci 003 is too powerfull and the most expensive one. 
#I suggest you to use Davinci 002 for more basic requests.
startPrompt = ""

df = pd.read_csv(csv_path)

def clearText():
    text_box.delete(1.0,tk.END)

def process_input():
    try:
        input_text = prompt_entry.get()
        result = agent.run(input_text)

        results.append("Output : "+result)
        text_box.insert(tk.END,"Output: " + result + "\n")
    except :
        print("ERROR HAS BEEN OCCOURED")
        text_box.insert(tk.END,"Output " + "Please Fix Your Request or Try Again,")

def show_info_popup():
    # Create new toplevel window.
    popup_window = tk.Toplevel(window)
    popup_window.title("GUIDE | KULLANIM")

    # Crate label for show message.
    message_label = tk.Label(popup_window, text="POP UP")
    message_label.pack(padx=20, pady=10)

    # for center your popup window.
    popup_window.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))

window = tk.Tk()
window.title("TITLE")
window.geometry("1000x500")
window.resizable(False,False)
#With this func you can not resize your window.

button = tk.Button(window, text="?", command=show_info_popup)
button.place(x=750,y=200)

image =Image.open('MY LOGO PATH')
image = image.resize((150,50))
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(window,image=image_tk)
image_label.pack()

prompt_entry = tk.Entry(window,width=50)
prompt_entry.place(x=250,y=200,width=500)

text_box = tk.Text(window , width=30,height=20)
text_box.place(x=200,y=280,height=170,width=600)

clear_button = tk.Button(window,text="CLEAR",command=clearText)
clear_button.place(x=460,y=420)

process_button = tk.Button(window,text="GENERATE",command=process_input)
process_button.place(x=450,y=240)

agent = create_csv_agent(OpenAI(openai_api_key=chat_gpt_api_key,temperature= 0,
                         model_name=type_of_arifical_intelligence_model), 
                         csv_path,
                         max_rows = 10,
                         verbose=True)

window.mainloop()
