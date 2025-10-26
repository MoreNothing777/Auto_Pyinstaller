# 🐍 Conversor Py → EXE (Interfaz gráfica con Tkinter)

Una aplicación gráfica desarrollada en Python con Tkinter que permite convertir archivos .py a ejecutables .exe de forma sencilla utilizando PyInstaller.
Incluye opciones de configuración, selección de bibliotecas ocultas, modo de empaquetado y carpeta de destino, todo dentro de una interfaz moderna y minimalista.

<img width="749" height="959" alt="image" src="https://github.com/user-attachments/assets/aa284d5d-cd3c-4aae-a97c-58e386220ec7" />

## 🚀 Características principales
<li>✅ Interfaz gráfica amigable y responsiva (Tkinter).
<li>📂 Permite seleccionar el archivo .py mediante un explorador de archivos.
<li>📁 Elección de carpeta de destino para el ejecutable.
<li>⚙️ Compatibilidad con los modos de PyInstaller:
<li> &emsp; --onefile: genera un único ejecutable.
<li> &emsp; --onefolder: genera una carpeta con el ejecutable y dependencias.
<li>🧩 Posibilidad de agregar bibliotecas ocultas (--hidden-import).
<li>🧵 Ejecución del proceso en un hilo independiente (sin bloquear la interfaz).
<li>📜 Monitoreo en tiempo real del progreso del proceso de compilación.
<li>💬 Área de log en vivo para salida del proceso y errores.

## 🧠 Tecnologías utilizadas (Requisitos)
<li>Python 3
<li>Tkinter (Interfaz gráfica)
<li>PyInstaller (Generación de ejecutables)
<li>Threading (Ejecución en segundo plano)
<li>Subprocess (Ejecución y captura de comandos del sistema)

## 💻 Uso
<li>Haz clic en Buscar ruta para seleccionar el archivo .py que deseas convertir.
<li>Selecciona el modo de compilación (OneFile o OneFolder).
<li>(Opcional) Agrega bibliotecas ocultas si tu script las utiliza.
<li>Define una carpeta de destino para guardar el resultado.
<li>Revisa el comando generado automáticamente.
<li>Pulsa Iniciar comando para ejecutar la conversión.
<li>El progreso se mostrará en tiempo real en el cuadro de texto inferior.

## ⚠️ Notas importantes
<li>En algunos sistemas Windows, es posible que debas ejecutar la aplicación con permisos de administrador para evitar restricciones de escritura en ciertas carpetas.
<li>Si usas rutas con espacios, el programa las manejará automáticamente entre comillas.
<li>El proceso puede tardar algunos minutos según el tamaño del proyecto o las dependencias incluidas.
