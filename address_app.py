from tkinter import *


window = Tk()
window.title("My Address Book")
window.geometry("900x700")
window.configure(bg="#81D4E3")
window.iconbitmap("icon.ico")

frame1 = Frame(window, bg="#81D4E3")
frame2 = Frame(window, bg="#81D4E3")
frame3 = Frame(window, bg="#81D4E3")


ii = []
nf = str()
nl = str()

def delete():
    global ii, nf, nl

    txt_to_del = contact_label['text']# <---String
    f = open('contacts.txt','r+')
    s = f.read()                    # <---String
    if txt_to_del in s:
        new_text = s.replace(txt_to_del, "")
        nf = (new_text)
        f.truncate(0)
        f.close()
        with open('contacts.txt','a') as f:
            f.write(nf)

    text_list = txt_to_del.split("\n")
    line = str(text_list[0] + "\n")
    f2 = open('names.txt','r+')
    n = f2.read()
    if line in n:
        new_namelist = n.replace(line, "")
        nl = (new_namelist)
        f2.truncate(0)
        f2.close()
        with open('names.txt','a') as nn:
            nn.write(nl)
    contact_label.config(text="Your Contact")
    b_delete.grid_remove()
    sort()
    
        
def sort():
    global ii
    ii.clear()
    get_list = listbox.get(0, END)  #creates a TUPLE
    
    with open('names.txt','r') as names:
        for items in sorted(names):
            ii.append(items)

    listbox.delete(0, END)
    for item in ii:
        listbox.insert(END, item[10:-2])


def show_contact(event):
    global ii
    f = open('contacts.txt', 'r').readlines() # This is a list
    
    chosen_contact = listbox.curselection()[0]
    seltext = listbox.get(chosen_contact) # seltext is a string
    
    try:
        for lines in f:
            if seltext in lines:
                i = f.index(lines)
                contact_label.config(text=f[i] + f[i+1] + f[i+2] + f[i+3] +f[i+4])
    except IndexError:
        pass
    
    b_delete.grid()
def save():

    
    new_name = text_name.get()
    new_phone = text_phone.get()
    new_email = text_email.get()
    new_address = text_address.get()
    new_notes = text_notes.get()
    add_contact = open("contacts.txt", "a")
    add_name = open("names.txt", "a")
    if new_name != "":
        add_contact.write("Full name: " + new_name + ",\nPhone Number: " + new_phone +\
                      ",\nE-mail: " + new_email + ",\nAddress: " + new_address +\
                      "\nNotes: "+ new_notes + "\n")
        add_name.write("Full name: " + new_name + ",\n")
    add_contact.close()
    
    e_name.delete(0, 'end')
    e_phone.delete(0, 'end')
    e_email.delete(0, 'end')
    e_address.delete(0, 'end')
    e_notes.delete(0, 'end')
    

    f = open('contacts.txt', 'r').readlines()
    d = f[-5]
    listbox.insert('end', d[10:-2])

    
scrollbar = Scrollbar(frame2, orient='vertical', width=20)
listbox = Listbox(frame2, bd=5, height=20, width=20, bg="#ebf5fb", font=("Courier", 12), \
                  yscrollcommand=scrollbar.set, highlightbackground="#5d6d7e")


scrollbar.config(command=listbox.yview)
scrollbar.pack(side='right', fill='both')

    
text_name = StringVar()
text_phone = StringVar()
text_email = StringVar()
text_address = StringVar()
text_notes = StringVar()


name = Label(frame1, text="Full Name:", bg="#81D4E3", font=("Courier", 16)).grid(row=0, column=0, sticky=E)
phone = Label(frame1, text="Phone nr:", bg="#81D4E3", font=("Courier", 16)).grid(row=2, column=0, sticky=E)
email = Label(frame1, text="Email:", bg="#81D4E3", font=("Courier", 16)).grid(row=3, column=0, sticky=E)
address = Label(frame1, text="Address:", bg="#81D4E3", font=("Courier", 16)).grid(row=4, column=0, sticky=E)
notes = Label(frame1, text="Notes:", bg="#81D4E3", font=("Courier", 16)).grid(row=5, column=0, sticky=E)

e_name = Entry(frame1, borderwidth=5, font=("Courier", 12), textvariable=text_name)
e_phone = Entry(frame1, borderwidth=5, font=("Courier", 12), textvariable=text_phone)
e_email = Entry(frame1, borderwidth=5, font=("Courier", 12), textvariable=text_email)
e_address = Entry(frame1, borderwidth=5, font=("Courier", 12), textvariable=text_address)
e_notes = Entry(frame1, borderwidth=5, font=("Courier", 12), textvariable=text_notes)

e_name.grid(row=0, column=1, ipadx=60, ipady=8)
e_phone.grid(row=2, column=1, ipadx=60, ipady=8)
e_email.grid(row=3, column=1, ipadx=60, ipady=8)
e_address.grid(row=4, column=1, ipadx=60, ipady=8)
e_notes.grid(row=5, column=1, ipadx=60, ipady=8)

with open('names.txt', 'r') as name_list:
    for items in sorted(name_list):
        ii.append(items)

for i in ii:
    listbox.insert('end', i[10:-2])


listbox.bind("<<ListboxSelect>>", show_contact)

listbox.pack(side='top', fill='both', expand=2)

contact_label = Label(frame3, text="Your Contact", bg="#81D4E3", font=("Courier", 16))
contact_label.grid(column=0, row=0)

b1 = Button(frame1, text="Add contact", bg="#C9EBEA", padx=20, pady=10, \
            font=("Courier", 14), bd=5, activebackground="#8EBB49", command=save)
b1.grid(row=6, column=1, pady=10)

b_sort = Button(frame2, text="Sort", bg="#C9EBEA", padx=10, pady=5,\
                font=("Courier", 12), bd=4, activebackground="#8EBB49", command=sort)
b_sort.pack(side="bottom")

b_delete = Button(frame3, text="Delete", bg="#C9EBEA", padx=10, pady=5,\
                  font=("Courier", 12), bd=4, activebackground="#8EBB49", command=delete)


frame1.grid(column=0, row=0, padx=50)
frame2.grid(column=1, row=0, pady=5)
frame3.grid(column=0, row=1, columnspan=2)

window.mainloop()
