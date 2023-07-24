from langchain import OpenAI
import pandas as pd
from langchain.agents import create_csv_agent
import tkinter as tk
from PIL import Image, ImageTk
import re


results = []


maps={
    "H1":"Hone",
    "W2":"Wtwo",
    "W1":"Wone",
    "L1":"Lone",
    "h2":"htwo",
    "P1":"Pone",
    "P2":"Ptwo",
    "M1":"Mone",
    "N1":"None",
    "N2":"Ntwo",
    "N3":"Ntheree",
    "S1":"Sone",
    "S2":"Stwo",
    "S3":"Stheree",
    "S4":"Sfour",
    "C0":"Czero",
    "Mr0":"Mrzero",
    "Mp0":"Mpzero",
    "My0":"Myzero",
    "Rail":"Rail(g/m)",    
    "Block":"Block(g)",
    "opsiyonel":"Company = ENDO, Category, W, Pone, H değerleri eşit ve L değeri en yakın ürünler ",
    "muadil":"Company = ENDO, Category, W, Pone, H değerleri eşit ve L değeri en yakın ürünler ",
    "model":"Model Name"
}

csv_path = '/Users/sakastudio/python/endo-6.csv'
chat_gpt_api_key = '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'
chat_gpt_api_key2 = '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'
type_of_arifical_intelligence_model = 'text-davinci-003'

startPrompt = ""

df = pd.read_csv(csv_path)

def clearText():
    text_box.delete(1.0,tk.END)

def modify_sentence(input):
    sayilar = re.findall(r'\b\d+(?:,\d+)?\b', input)
    for sayi in sayilar:
        if ',' in sayi and '.' not in sayi:
            input = re.sub(rf'\b{sayi}\b', f"{float(sayi):.1f}", input)
    # OUR CSV FILE ALL VALUES ARE FLOAT TYPE SO WE ADDED THIS FUNC.
    return input


def process_input():
    try:
        input_text = prompt_entry.get()
        

        convertedText = replace_prompts(input_text,maps,True)
        floatText = modify_sentence(convertedText)
        result = agent.run(startPrompt + floatText)

        results.append("Output : "+result)
        convertedOutput = replace_prompts(result,maps,False)
        text_box.insert(tk.END,"Output: " + convertedOutput + "\n")
    except :
        print("ERROR HAS BEEN OCCOURED")
        text_box.insert(tk.END,"Output " + "Please Fix Your Request or Try Again,")


def show_info_popup():
    # Yeni Toplevel pencere oluşturma
    popup_window = tk.Toplevel(window)
    popup_window.title("GUIDE | KULLANIM")

    # Mesajı göstermek için bir etiket (label) oluşturma
    message_label = tk.Label(popup_window, text="ENDO AI \n   \n\n\n-- TÜRKÇE -- \nArayacağınız değerleri \n H1, W1, L2 şeklinde yazınız \n Örnek : H1 değeri 15 olan ürünü bana bul.\n Endo AI yapay zeka ile ürün sorgulamaları yapmak için geliştirildi. \n Bu bot ile gündelik sohbet edemezsiniz. \n ENDO ürünlerini sorgulamak için özel üretildi.\n\n\n -- ENGLISH -- \nThe values which you gonna search \n type like H1, W1, L2. \n Example : H1 Find me model which H1 equals 15. \n\n Endo AI developed for query products with artifical intelligence.\n You can not daily chat with this bot.\n It is developed for help you in query ENDO Products.\n\n\n - Saka Studio")
    message_label.pack(padx=20, pady=10)

    # Popup penceresini merkezlemek için
    popup_window.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))


def replace_prompts(text,maps,state):
    if state == True:
        for key, value in maps.items():
            text = text.replace(key,value)
    elif state == False:
        for key, value in maps.items():
            text=text.replace(value,key)
    return text

window = tk.Tk()
window.title("ENDO DATA SERVICE")
window.geometry("1000x500")
window.resizable(False,False)

button = tk.Button(window, text="?", command=show_info_popup)
button.place(x=750,y=200)

image =Image.open('/Users/sakastudio/python/endologo.png')
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


agent = create_csv_agent(OpenAI(openai_api_key=chat_gpt_api_key2,temperature= 0,
                         model_name=type_of_arifical_intelligence_model), 
                         csv_path,
                         max_rows = 10,
                         verbose=True)

chunk_size = 150
chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

window.mainloop()