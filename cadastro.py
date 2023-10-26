import tkinter as tk

def cadastro():
    name= entry_name.get()
    email= entry_email.get()
    senha = entry_senha.get()

root = tk.Tk()
root.geometry("400x200")
root.eval('tk::PlaceWindow . center')
root.title('Cadastro')

second_win = tk.Toplevel(root)
root.eval(f'tk::PlaceWindow {str(second_win)} center')
label_name = tk.Label(root, text= 'NOME')
entry_name = tk.Entry(root)


label_email = tk.Label(root, text= 'EMAIL')
entry_email = tk.Entry(root)


label_senha = tk.Label(root, text= 'SENHA')
entry_senha = tk.Entry(root, show='*')



btn = tk.Button(root, text = 'Clique aqui', command=cadastro)



#packs
entry_name.pack()
entry_email.pack()
entry_senha.pack()

label_name.pack()
label_email.pack()
label_senha.pack()

btn.pack()

root.mainloop()
