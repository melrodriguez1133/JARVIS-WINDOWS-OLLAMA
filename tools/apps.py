import subprocess


def open_notepad():

    try:

        subprocess.Popen(["notepad.exe"])

        return "Bloc de notas abierto correctamente."

    except Exception as e:

        return f"No pude abrir el bloc de notas: {e}"