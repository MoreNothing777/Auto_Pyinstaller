# 🐍 Conversor Py → EXE (Interfaz gráfica con Tkinter)

Una aplicación gráfica desarrollada en Python con Tkinter que permite convertir archivos .py a ejecutables .exe de forma sencilla utilizando PyInstaller.
Incluye opciones de configuración, selección de bibliotecas ocultas, modo de empaquetado y carpeta de destino, todo dentro de una interfaz moderna y minimalista.

<img width="749" height="959" alt="image" src="https://github.com/user-attachments/assets/aa284d5d-cd3c-4aae-a97c-58e386220ec7" />

-------------------
# 🚀 Características principales

· ✅ Interfaz gráfica amigable y responsiva (Tkinter).
· 📂 Permite seleccionar el archivo .py mediante un explorador de archivos.
· 📁 Elección de carpeta de destino para el ejecutable.
· ⚙️ Compatibilidad con los modos de PyInstaller:
  · --onefile: genera un único ejecutable.
  · --onefolder: genera una carpeta con el ejecutable y dependencias.
· 🧩 Posibilidad de agregar bibliotecas ocultas (--hidden-import).
· 🧵 Ejecución del proceso en un hilo independiente (sin bloquear la interfaz).
· 📜 Monitoreo en tiempo real del progreso del proceso de compilación.
· 💬 Área de log en vivo para salida del proceso y errores.

--------------
# 🧠 Tecnologías utilizadas (Requisitos)

· Python 3
· Tkinter (Interfaz gráfica)
· PyInstaller (Generación de ejecutables)
· Threading (Ejecución en segundo plano)
· Subprocess (Ejecución y captura de comandos del sistema)

-------------

# 💻 Uso

**En la interfaz:**

· Haz clic en Buscar ruta para seleccionar el archivo .py que deseas convertir.
· Selecciona el modo de compilación (OneFile o OneFolder).
· (Opcional) Agrega bibliotecas ocultas si tu script las utiliza.
· Define una carpeta de destino para guardar el resultado.
· Revisa el comando generado automáticamente.
· Pulsa Iniciar comando para ejecutar la conversión.
· El progreso se mostrará en tiempo real en el cuadro de texto inferior.

--------------
# ⚠️ Notas importantes

· En algunos sistemas Windows, es posible que debas ejecutar la aplicación con permisos de administrador para evitar restricciones de escritura en ciertas carpetas.
· Si usas rutas con espacios, el programa las manejará automáticamente entre comillas.
· El proceso puede tardar algunos minutos según el tamaño del proyecto o las dependencias incluidas.
