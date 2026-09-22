from tools.apps import open_notepad
from tools.web import open_youtube, search_youtube
from tools.system import get_time, run_cmd
from tools.youtube import search_and_play_youtube
from tools.spotify_player import play_spotify
from tools.camera import start_camera


# ============================================================
# ROUTER DE HERRAMIENTAS DE JARVIS
# ============================================================

def execute_tool(
    tool_name,
    arguments=None
):

    arguments = arguments or {}

    print(
        f"\n🔧 Ejecutando herramienta: {tool_name}"
    )


    # ========================================================
    # BLOC DE NOTAS
    # ========================================================

    if tool_name == "open_notepad":

        return open_notepad()


    # ========================================================
    # ABRIR YOUTUBE
    # ========================================================

    elif tool_name == "open_youtube":

        return open_youtube()


    # ========================================================
    # BUSCAR YOUTUBE
    # ========================================================

    elif tool_name == "search_youtube":

        query = arguments.get(
            "query",
            ""
        )

        return search_youtube(
            query
        )


    # ========================================================
    # BUSCAR Y REPRODUCIR YOUTUBE
    # ========================================================

    elif tool_name == "search_and_play_youtube":

        query = arguments.get(
            "query",
            ""
        )

        return search_and_play_youtube(
            query
        )


    # ========================================================
    # HORA
    # ========================================================

    elif tool_name == "get_time":

        return get_time()


    # ========================================================
    # CMD
    # ========================================================

    elif tool_name == "run_cmd":

        command = arguments.get(
            "command",
            ""
        )

        return run_cmd(
            command
        )


    # ========================================================
    # SPOTIFY DESKTOP
    # ========================================================

    elif tool_name == "play_spotify":

        query = arguments.get(
            "query",
            ""
        )

        return play_spotify(
            query
        )


    # ========================================================
    # CÁMARA
    # ========================================================

    elif tool_name == "start_camera":

        return start_camera()


    # ========================================================
    # HERRAMIENTA DESCONOCIDA
    # ========================================================

    else:

        return (
            f"Herramienta desconocida: "
            f"{tool_name}"
        )