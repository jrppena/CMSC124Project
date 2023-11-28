import tkinter as tk
from api import Api

root = tk.Tk()
root.geometry("1500x800")

root.title("Lolcode Interpreter")


top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, padx=10, pady=10)

""" Textboxs"""
editor = tk.Text(top_frame, height=20, width=80)
editor.grid(row=0, column=0, padx=20, pady=10)

lexemes = tk.Text(top_frame, height=20, width=50)
lexemes.grid(row=0, column=1, padx=20, pady=10)

variables = tk.Text(top_frame, height=20, width=20)
variables.grid(row=0, column=2, padx=20, pady=10)

terminal = tk.Text(root, height=20, width=70)
terminal.pack(side=tk.BOTTOM, padx=20, pady=10)


""" Function calls """
api = Api(root, editor,terminal,  lexemes, variables )

terminal.bind("<Return>", api.on_enter_pressed)


ex = tk.Button(root, text="Execute", command=api.execute)
ex.pack( padx=20, pady=10)

file_button = tk.Button(root, text="Open File", command=api.open_file_dialog)
file_button.pack( padx=20, pady=10)



root.mainloop()




