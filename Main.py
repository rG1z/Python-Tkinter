import tkinter as tk
from tkinter import ttk


class Class(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()
        self.remove()

    # paspaudimo mygtukai ir laukeliai ivedimui
    def initialize_user_interface(self):
        self.parent.title("Drugs")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")
        self.drug_label = ttk.Label(self.parent, text="Drug name:")
        self.drug_entry = ttk.Entry(self.parent)
        self.drug_label.grid(row=0, column=0, ipadx=120)
        self.drug_entry.grid(row=0, column=0)
        self.drug_entry.delete(0, tk.END)
        self.quantity_label = ttk.Label(self.parent, text="Quantity:")
        self.quantity_entry = ttk.Entry(self.parent)
        self.quantity_label.grid(row=1, column=0, ipadx=120)
        self.quantity_entry.grid(row=1, column=0)
        self.bought_label = ttk.Label(self.parent, text="When bought:")
        self.bought_entry = ttk.Entry(self.parent)
        self.bought_label.grid(row=2, column=0, ipadx=120)
        self.bought_entry.grid(row=2, column=0)
        self.enough_label = ttk.Label(self.parent, text="Enough till:")
        self.enough_entry = ttk.Entry(self.parent)
        self.enough_label.grid(row=3, column=0, ipadx=120)
        self.enough_entry.grid(row=3, column=0)
        self.submit_button = ttk.Button(self.parent, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=5, column=0, padx=100)
        self.exit_button = ttk.Button(self.parent, text="Exit", command=self.parent.quit)
        self.exit_button.grid(row=0, column=3)
        self.del_btn = ttk.Button(self.parent, text="Delete", command=self.remove)
        self.del_btn.grid(row=6, column=0)


        # treeview lentele
        self.tree = ttk.Treeview(self.parent, columns=('Drug name', 'Quantity', 'When bought', 'Enough till'))
        self.tree.heading('#1', text='Drug name')
        self.tree.heading('#2', text='Quantity')
        self.tree.heading('#3', text='When bought')
        self.tree.heading('#4', text='Enough till')
        self.tree.column('#1', stretch=True)
        self.tree.column('#2', stretch=True)
        self.tree.column('#3', stretch=True)
        self.tree.column('#4', stretch=True)
        self.tree.grid(row=8, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Kad eitu i apacia skaiciai su Nr.
        self.i = 1


    def insert_data(self):
        self.treeview.insert("", 'end', text="Nr."+str(self.i), values=(self.drug_entry.get(),
                            self.quantity_entry.get(),
                            self.bought_entry.get(),
                            self.enough_entry.get()))
        self.treeview.focus()
        self.drug_entry.delete(0, "end") # Ištrinti laukelius kai suveda duomenis ir paspaudzia insert
        self.quantity_entry.delete(0, "end")
        self.bought_entry.delete(0, "end")
        self.enough_entry.delete(0, "end")

        # Kad pridetu eiles numeri po +1
        self.i = self.i + 1

        # Funkcija, kad ištrinti lentele eilute pasirinkta
    def remove(self):
        selected_items = self.tree.selection()
        for lists in selected_items:
            self.tree.delete(lists)



def main():
    root = tk.Tk()
    d = Class(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# drugs2 = tk.StringVar()
# mesage = ttk.Entry(root, textvariable=drugs2)
# mesage.pack(padx= 10, pady= 10, anchor='w', expand= True)
# ttk.Button(root, text= "Click Here", command=mesage).pack(pady= 20)
# mesage.get()
#
#
# columns = ("drug_name", "drug_quantity", "bought", "till")
# tree = ttk.Treeview(root, columns=columns, show="headings")
#
# tree.heading('drug_name', text="Drug Name")
# tree.heading('drug_quantity', text="Drug Quantity")
# tree.heading('bought', text="When Bought")
# tree.heading('till', text="Enough Till")
#
#
# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         showinfo(title="information", message=','.join(record))
#
# tree.bind('<<TreeviewSelect>>', item_selected)
# tree.pack(padx= 10, pady= 10, fill = "x", expand=True)
#
#
# root.mainloop()
#
#
# #
# # # vardas_pavarde = input("Įveskite savo vardą ir pavardę: ")
# # # print(f'{vardas_pavarde}' " naudojami vaistai:")


