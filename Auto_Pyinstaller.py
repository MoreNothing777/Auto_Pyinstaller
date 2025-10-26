import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import subprocess

def buscar_ruta():
    ruta = filedialog.askopenfilename(title="Selecciona el archivo", filetypes=[("Archivos python", "*.py"), ("Todos los archivos", "*.*")])

    if ruta:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta)
        actualizar_comando()
    
def elminar_ruta():
    entrada_ruta.delete(0, tk.END)
    actualizar_comando()

def cambio_modo():
    actualizar_comando()

def elegir_carpeta_destino():
    global carpeta_destino
    carpeta = filedialog.askdirectory(title="Selecciona carpeta de destino")

    if carpeta:
        carpeta_destino = carpeta
        actualizar_comando()
    
def actualizar_comando(*args):
    try:
        ruta = entrada_ruta.get().strip()
        modo_actual = modo.get()
        biblios = entrada_biblio.get("1.0", tk.END).strip().split()

        comando = ["pyinstaller"]

        if modo_actual:
            comando.append(modo_actual)

        if biblios:
            for b in biblios:
                comando.append(f"--hidden-import {b}")

        if ruta:
            comando.append(f'"{ruta}"')

        comando.append(f'--distpath "{carpeta_destino}"')

        cuadro_comando.config(state="normal")
        cuadro_comando.delete("1.0", tk.END)
        cuadro_comando.insert(tk.END, " ".join(comando))
        cuadro_comando.config(state="disabled")

    except Exception:
        return None

def iniciar_comando():
    comando = cuadro_comando.get("1.0", tk.END).strip()

    if not comando:
        return
    
    cuadro_proceso.config(state="normal")
    cuadro_proceso.delete("1.0", tk.END)
    cuadro_proceso.insert(tk.END, "Proceso iniciado\n")
    cuadro_proceso.config(state="disabled")

    hilo = threading.Thread(target=ejecutar_y_mostrar, args=(comando,))
    hilo.start()

def ejecutar_y_mostrar(comando):
    try:
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, bufsize=1)

        for linea in proceso.stdout:
            ventana.after(0, agregar_linea_proceso, linea.strip())

        proceso.wait()
        ventana.after(0, agregar_linea_proceso, "\n>>> Proceso finalizado.\n")

    except Exception as e:
        ventana.after(0, agregar_linea_proceso, f"\nERROR:\n{e}")

def agregar_linea_proceso(linea):
    cuadro_proceso.config(state="normal")
    cuadro_proceso.insert(tk.END, linea + "\n")
    cuadro_proceso.see(tk.END)
    cuadro_proceso.config(state="disabled")

ventana = tk.Tk()
ventana.title("Conversor py -> exe")
ventana.geometry("750x930+0+0")
ventana.config(bg="#1e1e1e")

# estilos
estilo_titulo = {"bg": "#1e1e1e", "fg": "grey", "font": ("Consolas", 26)}
estilo_boton = {"bg": "#444", "fg": "#fff", "activebackground": "#555", "font": ("Consolas", 10), "width": 18}
estilo_label = {"bg": "#1e1e1e", "fg": "white", "font": ("Consolas", 11)}
estilo_entry = {"bg": "#2a2a2a", "fg": "white", "font": ("Consolas", 9)}
estilo_check = {"bg": "#808080", "fg": "black", "font": ("Consolas", 11)}
estilo_boton_comando = {"bg": "#444", "fg": "#fff", "activebackground": "#555", "font": ("Consolas", 10), "width": 100}

# interfaz
tk.Label(text="Conversor py/exe", **estilo_titulo).grid(row=0, column=0, columnspan=3)

tk.Label(text="Ruta del archivo:", **estilo_label).grid(row=1, column=0, sticky="e")

entrada_ruta = tk.Entry(width=75, **estilo_entry)
entrada_ruta.grid(row=1, column=1, columnspan=2, padx=30, pady=30)
entrada_ruta.bind("<KeyRelease>", actualizar_comando)

tk.Button(text= "Buscar ruta", command=buscar_ruta, **estilo_boton).grid(row=3,column=1)
tk.Button(text= "Borrar ruta", command=elminar_ruta, **estilo_boton).grid(row=3,column=2)

modo = tk.StringVar(value = "--onefolder")

op1 = tk.Radiobutton(text = "  OneFile", variable=modo, value="--onefile", **estilo_check, command=cambio_modo)
op1.grid(row=5, column=0, padx=30)
op2 = tk.Radiobutton(text = "OneFolder", variable=modo, value="--onefolder", **estilo_check, command=cambio_modo)
op2.grid(row=6, column=0, padx=30, pady=(20,0), sticky="n")

tk.Label(text="Bibliotecas (Separadas por comas):", **estilo_label).grid(row=4, column=1, columnspan=2, pady=(30,10))
entrada_biblio = tk.Text(**estilo_entry, width=75, height=5)
entrada_biblio.grid(row=5, column=1, columnspan=2, rowspan=2, sticky="n")
entrada_biblio.bind("<KeyRelease>", actualizar_comando)

tk.Button(text="Carpeta destino", command=elegir_carpeta_destino, **estilo_boton).grid(row=6, column=0, pady=(10,0), sticky="es")

tk.Label(text="Comando generado", **estilo_label).grid(row=6, column=1, columnspan=2, pady=(65, 5),padx=20, sticky="e")
cuadro_comando = tk.Text(ventana, height=3, width=100, bg="#2a2a2a", fg="lime", font=("Consolas", 10))
cuadro_comando.grid(row=7, column=0, columnspan=3, padx=20, pady=(10,0))
cuadro_comando.config(state="disabled")

cuadro_proceso = tk.Text(ventana, height=30, width=100, bg="#2a2a2a", fg="lime", font=("Consolas", 10))
cuadro_proceso.grid(row=9, column=0, columnspan=3, pady=10)
cuadro_proceso.config(state="disabled")

tk.Button(ventana, **estilo_boton_comando, command=iniciar_comando, text= "Iniciar comando").grid(row=10, columnspan=3, )

ventana.mainloop()
