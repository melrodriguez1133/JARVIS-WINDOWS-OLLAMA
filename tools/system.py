from datetime import datetime
import subprocess


# ============================================================
# HORA
# ============================================================

def get_time():

    now = datetime.now()

    return (
        f"La hora actual es "
        f"{now.strftime('%H:%M:%S')}"
    )


# ============================================================
# COMANDOS CMD PERMITIDOS
# ============================================================

ALLOWED_COMMANDS = {
    "ipconfig",
    "hostname",
    "whoami",
    "dir",
    "ver",
    "systeminfo",
}


# ============================================================
# EJECUTAR COMANDO EN CMD VISIBLE
# ============================================================

def run_cmd(command):

    if not command:

        return (
            "❌ No se indicó ningún comando."
        )

    # ----------------------------------------
    # LIMPIAR COMANDO
    # ----------------------------------------

    command = command.strip().lower()

    # ----------------------------------------
    # VERIFICAR SI ESTÁ PERMITIDO
    # ----------------------------------------

    if command not in ALLOWED_COMMANDS:

        return (
            "❌ Comando no permitido. "
            "JARVIS solamente puede ejecutar "
            "comandos autorizados."
        )

    try:

        print(
            f"💻 Ejecutando en CMD: {command}"
        )

        # ----------------------------------------
        # ABRIR CMD VISIBLE
        #
        # /K:
        # Ejecuta el comando y mantiene abierta
        # la ventana de CMD.
        # ----------------------------------------

        subprocess.Popen(
            [
                "cmd.exe",
                "/K",
                command
            ]
        )

        return (
            f"💻 Ejecutando '{command}' "
            f"en CMD."
        )

    except Exception as error:

        return (
            "❌ No pude abrir CMD: "
            f"{error}"
        )


# ============================================================
# FIN DEL ARCHIVO
# ============================================================