# 🐍 Conversor Py → EXE (Interfaz gráfica con Tkinter)

Una aplicación gráfica desarrollada en Python con Tkinter que permite convertir archivos .py a ejecutables .exe de forma sencilla utilizando PyInstaller.
Incluye opciones de configuración, selección de bibliotecas ocultas, modo de empaquetado y carpeta de destino, todo dentro de una interfaz moderna y minimalista.<br>

<img width="749" height="959" alt="image" src="https://github.com/user-attachments/assets/aa284d5d-cd3c-4aae-a97c-58e386220ec7" />

## 🚀 Características principales
<li>✅ Interfaz gráfica amigable y responsiva (Tkinter).<br>
<li>📂 Permite seleccionar el archivo .py mediante un explorador de archivos.<br>
<li>📁 Elección de carpeta de destino para el ejecutable.<br>
<li>⚙️ Compatibilidad con los modos de PyInstaller:<br>
<li> &emsp; --onefile: genera un único ejecutable.<br>
<li> &emsp; --onefolder: genera una carpeta con el ejecutable y dependencias.<br>
<li>🧩 Posibilidad de agregar bibliotecas ocultas (--hidden-import).<br>
<li>🧵 Ejecución del proceso en un hilo independiente (sin bloquear la interfaz).<br>
<li>📜 Monitoreo en tiempo real del progreso del proceso de compilación.<br>
<li>💬 Área de log en vivo para salida del proceso y errores.<br>

## 🧠 Tecnologías utilizadas (Requisitos)
<li>Python 3<br>
<li>Tkinter (Interfaz gráfica)<br>
<li>PyInstaller (Generación de ejecutables)<br>
<li>Threading (Ejecución en segundo plano)<br>
<li>Subprocess (Ejecución y captura de comandos del sistema)<br>

## 💻 Uso
<li>Haz clic en Buscar ruta para seleccionar el archivo .py que deseas convertir.<br>
<li>Selecciona el modo de compilación (OneFile o OneFolder).<br>
<li>(Opcional) Agrega bibliotecas ocultas si tu script las utiliza.<br>
<li>Define una carpeta de destino para guardar el resultado.<br>
<li>Revisa el comando generado automáticamente.<br>
<li>Pulsa Iniciar comando para ejecutar la conversión.<br>
<li>El progreso se mostrará en tiempo real en el cuadro de texto inferior.<br>

## ⚠️ Notas importantes
<li>En algunos sistemas Windows, es posible que debas ejecutar la aplicación con permisos de administrador para evitar restricciones de escritura en ciertas carpetas.<br>
<li>Si usas rutas con espacios, el programa las manejará automáticamente entre comillas.<br>
<li>El proceso puede tardar algunos minutos según el tamaño del proyecto o las dependencias incluidas.
