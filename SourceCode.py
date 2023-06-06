import tkinter as tk # Modul tkinter dan alias tk untuk memudahkan pengguna
from tkinter import filedialog # fungsi filedialog yang di gunakan untuk dialog
pemilihan fle
current_file = None # variabel untuk menyimpan path file yang sedang aktif
def new_file():#fungsi ini di panggil ketika opsi "New " di menu file di pilih dan
untuk menghapus teks dalam widget
global current_file
text.delete('1.0', tk.END)
current_file = None
def open_file():#untuk membuka dialog pemilihan file dan membaca isi file yang
di pilih
global current_file
file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
if file_path:
with open(file_path, 'r') as file:
text.delete('1.0', tk.END)
text.insert(tk.END, file.read())
current_file = file_path # setelah hapus file sebelumnya current file diatur
menjadi path file
def save_file():# untuk menemukan nilai
global current_file
if current_file:
with open(current_file, 'w') as file:
file.write(text.get('1.0', tk.END))
else:
save_file_as()
def save_file_as():# menu ini di panggil jika opsi save as di menu file di pilih
file_path = filedialog.asksaveasfilename(defaultextension='.txt',
filetypes=[('Text Files', '*.txt')])
if file_path:
with open(file_path, 'w') as file:
file.write(text.get('1.0', tk.END))
current_file = file_path
def cut_text():# fungsi ini di panggil ketika opsi cut di menu edit di pilih dan yang
akan memotong teks yang di pilih
text.event_generate('<<Cut>>')
def copy_text():
text.event_generate('<<Copy>>')
def paste_text():
text.event_generate('<<Paste>>')
root = tk.Tk()
root.title("Notepad")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
text = tk.Text(root)
text.pack()
root.mainloop()
