# 🐍 Conversor Py → EXE (Interfaz gráfica con Tkinter)

Una aplicación gráfica desarrollada en Python con Tkinter que permite convertir archivos .py a ejecutables .exe de forma sencilla utilizando PyInstaller.
Incluye opciones de configuración, selección de bibliotecas ocultas, modo de empaquetado y carpeta de destino, todo dentro de una interfaz moderna y minimalista.<br>

<img width="749" height="959" alt="image" src="https://github.com/user-attachments/assets/aa284d5d-cd3c-4aae-a97c-58e386220ec7" />

-------------------

# 🚀 Características principales

· ✅ Interfaz gráfica amigable y responsiva (Tkinter).<br>
· 📂 Permite seleccionar el archivo .py mediante un explorador de archivos.<br>
· 📁 Elección de carpeta de destino para el ejecutable.<br>
· ⚙️ Compatibilidad con los modos de PyInstaller:<br>
  · --onefile: genera un único ejecutable.<br>
  · --onefolder: genera una carpeta con el ejecutable y dependencias.<br>
· 🧩 Posibilidad de agregar bibliotecas ocultas (--hidden-import).<br>
· 🧵 Ejecución del proceso en un hilo independiente (sin bloquear la interfaz).<br>
· 📜 Monitoreo en tiempo real del progreso del proceso de compilación.<br>
· 💬 Área de log en vivo para salida del proceso y errores.<br>

--------------

# 🧠 Tecnologías utilizadas (Requisitos)
<br>
· Python 3<br>
· Tkinter (Interfaz gráfica)<br>
· PyInstaller (Generación de ejecutables)<br>
· Threading (Ejecución en segundo plano)<br>
· Subprocess (Ejecución y captura de comandos del sistema)<br>

-------------

# 💻 Uso

**En la interfaz:**

· Haz clic en Buscar ruta para seleccionar el archivo .py que deseas convertir.<br>
· Selecciona el modo de compilación (OneFile o OneFolder).<br>
· (Opcional) Agrega bibliotecas ocultas si tu script las utiliza.<br>
· Define una carpeta de destino para guardar el resultado.<br>
· Revisa el comando generado automáticamente.<br>
· Pulsa Iniciar comando para ejecutar la conversión.<br>
· El progreso se mostrará en tiempo real en el cuadro de texto inferior.<br>

--------------

# ⚠️ Notas importantes

· En algunos sistemas Windows, es posible que debas ejecutar la aplicación con permisos de administrador para evitar restricciones de escritura en ciertas carpetas.<br>
· Si usas rutas con espacios, el programa las manejará automáticamente entre comillas.<br>
· El proceso puede tardar algunos minutos según el tamaño del proyecto o las dependencias incluidas.<br>
