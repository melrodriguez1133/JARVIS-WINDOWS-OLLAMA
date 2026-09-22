import subprocess


# ============================================================
# APLICACIONES DE WINDOWS
# ============================================================

def open_notepad():

    try:

        subprocess.Popen(
            ["notepad.exe"]
        )

        return (
            "Bloc de notas abierto correctamente."
        )

    except Exception as error:

        return (
            "No pude abrir el bloc de notas: "
            f"{error}"
        )


# ============================================================
# CALCULADORA
# ============================================================

def open_calculator():

    try:

        subprocess.Popen(
            ["calc.exe"]
        )

        return (
            "Calculadora abierta correctamente."
        )

    except Exception as error:

        return (
            "No pude abrir la calculadora: "
            f"{error}"
        )


# ============================================================
# EXPLORADOR DE ARCHIVOS
# ============================================================

def open_explorer():

    try:

        subprocess.Popen(
            ["explorer.exe"]
        )

        return (
            "Explorador de archivos abierto correctamente."
        )

    except Exception as error:

        return (
            "No pude abrir el explorador de archivos: "
            f"{error}"
        )


# ============================================================
# CMD
# ============================================================

def open_cmd():

    try:

        subprocess.Popen(
            ["cmd.exe"]
        )

        return (
            "Símbolo del sistema abierto correctamente."
        )

    except Exception as error:

        return (
            "No pude abrir el símbolo del sistema: "
            f"{error}"
        )