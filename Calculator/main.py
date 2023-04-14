import tkinter as tk

def label_frames():
    global entry_label_frame, buttons_label_frame
    entry_label_frame = tk.LabelFrame(root, borderwidth=0)
    buttons_label_frame = tk.LabelFrame(root, borderwidth=0)

    entry_label_frame.grid(row=0, column=0, padx=65, pady=40)
    buttons_label_frame.grid(row=1, column=0, padx=10)

    entry_widget()
    buttons_widgets()

def entry_widget():
    calc_entry = tk.Entry(entry_label_frame, width=20, font=('Arial', 18))
    calc_entry.grid(row=0, column=0)

def buttons_widgets():
    for i in range(5):
        for j in range(4):
            button = tk.Button(buttons_label_frame, width=7, background='orange', foreground='#000', font=('roboto', 10, 'bold'), borderwidth=1)
            if i == 0:
                button.config(text=str(j+1))
                if j == 3:
                    button.config(text='+')
            elif i == 1:
                button.config(text=str(j+4))
                if j == 3:
                    button.config(text='-')
            elif i == 2:
                button.config(text=str(j+7))
                if j == 3:
                    button.config(text='x')
            elif i == 3:
                button.config(text='0')
                if j == 1:
                    button.config(text='C')
                elif j == 2:
                    button.config(text='=')
                elif j == 3:
                    button.config(text='/')
            elif i == 4:
                button.config(state='disabled')
                if j == 0:
                    button.config(text='.', state='normal')
                

                    
            button.grid(row=i, column=j)


if __name__=='__main__':
    root = tk.Tk()
    root.title('DFI Calculator')
    root.geometry('400x300')
    root.resizable(0, 0)
    root.iconbitmap('fortress.ico')
    root.config(background='#262727')


    label_frames()

    root.mainloop()