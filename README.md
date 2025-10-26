# 🐍 Conversor Py → EXE (Interfaz gráfica con Tkinter)

Una aplicación gráfica desarrollada en Python con Tkinter que permite convertir archivos .py a ejecutables .exe de forma sencilla utilizando PyInstaller.
Incluye opciones de configuración, selección de bibliotecas ocultas, modo de empaquetado y carpeta de destino, todo dentro de una interfaz moderna y minimalista.<br>

<img width="749" height="959" alt="image" src="https://github.com/user-attachments/assets/aa284d5d-cd3c-4aae-a97c-58e386220ec7" />

## 🚀 Características principales
<li>✅ Interfaz gráfica amigable y responsiva (Tkinter).<\li><br>
<li>📂 Permite seleccionar el archivo .py mediante un explorador de archivos.<\li><br>
<li>📁 Elección de carpeta de destino para el ejecutable.<\li><br>
<li>⚙️ Compatibilidad con los modos de PyInstaller:<\li><br>
&emsp;<li> --onefile: genera un único ejecutable.<\li><br>
&emsp;<li> --onefolder: genera una carpeta con el ejecutable y dependencias.<\li><br>
<li>🧩 Posibilidad de agregar bibliotecas ocultas (--hidden-import).<\li><br>
<li>🧵 Ejecución del proceso en un hilo independiente (sin bloquear la interfaz).<\li><br>
<li>📜 Monitoreo en tiempo real del progreso del proceso de compilación.<\li><br>
<li>💬 Área de log en vivo para salida del proceso y errores.<\li><br>

## 🧠 Tecnologías utilizadas (Requisitos)
<li>Python 3<\li><br>
<li>Tkinter (Interfaz gráfica)<\li><br>
<li>PyInstaller (Generación de ejecutables)<\li><br>
<li>Threading (Ejecución en segundo plano)<\li><br>
<li>Subprocess (Ejecución y captura de comandos del sistema)<\li><br>

## 💻 Uso
<li>Haz clic en Buscar ruta para seleccionar el archivo .py que deseas convertir.<\li><br>
<li>Selecciona el modo de compilación (OneFile o OneFolder).<\li><br>
<li>(Opcional) Agrega bibliotecas ocultas si tu script las utiliza.<\li><br>
<li>Define una carpeta de destino para guardar el resultado.<\li><br>
<li>Revisa el comando generado automáticamente.<\li><br>
<li>Pulsa Iniciar comando para ejecutar la conversión.<\li><br>
<li>El progreso se mostrará en tiempo real en el cuadro de texto inferior.<\li><br>

## ⚠️ Notas importantes
<li>En algunos sistemas Windows, es posible que debas ejecutar la aplicación con permisos de administrador para evitar restricciones de escritura en ciertas carpetas.<\li><br>
<li>Si usas rutas con espacios, el programa las manejará automáticamente entre comillas.<\li><br>
<li>El proceso puede tardar algunos minutos según el tamaño del proyecto o las dependencias incluidas.<\li>
