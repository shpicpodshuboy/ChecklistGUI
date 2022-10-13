from tkinter import *

def add_item():
    label_events_submenu.insert(END, label_content_submenu.get())
    label_content_submenu.delete(0, END)

def del_list():
    select = list(label_events_submenu.curselection())
    select.reverse()
    for i in select:
        label_events_submenu.delete(i)

def save_list():
    f = open('a:/list000.txt', 'w')
    f.writelines("\n".join(label_events_submenu.get(0, END)))
    f.close()

root=Tk()

frame_main_events=Frame(master=root)
frame_events=Frame(master=frame_main_events)
frame_events_submenu=Frame(master=frame_main_events)
frame_main_content=Frame(master=root)
frame_content_submenu=Frame(master=frame_main_content)
frame_content_info=Frame(master=frame_main_content)
frame_content_info.pack(side=BOTTOM)
frame_content_submenu.pack(side=TOP)
frame_events.pack()
frame_events_submenu.pack()
frame_main_events.pack(side=LEFT, fill=BOTH)
frame_main_content.pack(side=LEFT, fill=BOTH)

label_events=Label(master=frame_events,relief=RAISED, text="События",height=2,width=20, bg='grey')
label_events.pack()
label_events_submenu=Listbox(master=frame_events_submenu, width=20)
label_events_submenu.pack(pady=8)
label_content_submenu=Entry(master=frame_content_submenu, width=40)
label_content_submenu.pack(pady=9)
content_info=Text(master=frame_main_content, height=30, width=60)
content_info.pack(padx=5, pady=5)
add_button=Button(master=frame_events_submenu,text='Добавить', command=add_item)
add_button.pack()
del_button=Button(master=frame_events_submenu,text='Удалить', command=del_list)
del_button.pack(pady=6)
save_button=Button(master=frame_events_submenu,text='Сохранить', command=save_list)
save_button.pack(pady=6)

f=open('a:/list000.txt', 'r')

events_list=[]
for line in f:
    events_list.append(line)

for i in events_list:
    label_events_submenu.insert(END, i)

root.title("Планировщик")
root.mainloop()