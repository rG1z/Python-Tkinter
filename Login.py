import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x150")
root.title('Drugs')
root.resizable(False, False)


login = tk.StringVar() # login su stringais
passw = tk.StringVar()

def login_click():
    # Gauti info kai paspaudzia login
    msg = f'You entered login name: {login.get()} and password: {passw.get()}'
    showinfo(title="Information", message = msg)

signin = ttk.Frame(root)
signin.pack(padx= 10, pady= 10, fill = "x", expand=True)

login_label = ttk.Label(signin, text="Username: ")
login_label.pack(fill = "x", expand=True) # Susikurti labeli, aprasyma

login_entry = ttk.Entry(signin, textvariable=login) #Susikurti laukeli, kur bus galima irasyti
login_entry.pack(fill = "x", expand=True)
login_entry.focus()

passw_label = ttk.Label(signin, text="Password: ")
passw_label.pack(fill = "x", expand=True) # Susikurti labeli, aprasyma (slaptazodziui)

passw_entry = ttk.Entry(signin, textvariable=passw, show="*") #Susikurti laukeli, kur bus galima irasyti (slaptz)
passw_entry.pack(fill = "x", expand=True)

login_button = ttk.Button(signin, text="Login", command=login_click) #Mygtukas login paspausti
login_button.pack(fill="x", expand=True, pady=10)



root.mainloop()