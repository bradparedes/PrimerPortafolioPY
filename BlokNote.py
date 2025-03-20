import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Colores")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("No  se pudo guardar el Archivo!")
        finally:
            file.close()

def open_file():
    file = askopenfilename(initialfile="untitled.txt",
                                    defaultextension=".txt",
                                    file=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("No puede leer el Archivo!")
    finally:
        file.close()


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("Acerca del Bloc de Notas",
             """Bloc de Notas es un editor de texto incluido en los sistemas operativos.
                                Su funcionalidad es muy simple. Algunas características propias son:
                                Inserción de hora y fecha actual pulsando F5, en formato "HH:MM DD/MM/AA".
                                    - Inserción de hora y fecha actual si el documento comienza por ".LOG"
                                     - Ajuste de líneas. 
                                     -Posibilidad de exportar a cualquier formato de texto plano.
                            """)

def quit():
    window.destroy()

window = Tk()
window.title("Bloc de Notas")
file = None

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width /2) - (window_width /2))
y = int((screen_height /2) - (window_height /2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N + E + S +W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Cortar", command=cut)
edit_menu.add_command(label="Copiar", command=copy)
edit_menu.add_command(label="Pegar",command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayuda", menu=help_menu)
help_menu.add_command(label="Acerca de", command=about)

window.mainloop()