import tkinter as tk
window = tk.Tk()



# schijf hier tussen je code

global is_on
is_on = True
window.configure(bg='yellow')


def switch():
    global is_on
    if is_on:
        print("lamp is uit")
        window.configure(bg='black')
        button.configure(text="uit")
        is_on = False
    else:
        print("lamp is aan")
        window.configure(bg='yellow')
        button.configure(text="aan")
        is_on = True

# schijf hier tussen je code
button = tk.Button(text="aan", bg="white", fg="black", command=switch,pady = 50, padx = 100,)
button.pack(pady = 300, padx = 600,)
window.mainloop()