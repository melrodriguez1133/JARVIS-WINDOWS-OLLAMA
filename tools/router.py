from tools.apps import open_notepad
from tools.web import open_youtube, search_youtube
from tools.system import get_time
from tools.youtube import search_and_play_youtube
from tools.spotify_player import play_spotify


def execute_tool(tool_name, arguments=None):

    arguments = arguments or {}

    print(
        f"\n🔧 Ejecutando herramienta: {tool_name}"
    )

    # --------------------------------
    # BLOC DE NOTAS
    # --------------------------------

    if tool_name == "open_notepad":

        return open_notepad()

    # --------------------------------
    # ABRIR YOUTUBE
    # --------------------------------

    elif tool_name == "open_youtube":

        return open_youtube()

    # --------------------------------
    # BUSCAR YOUTUBE
    # --------------------------------

    elif tool_name == "search_youtube":

        query = arguments.get(
            "query",
            ""
        )

        return search_youtube(query)

    # --------------------------------
    # BUSCAR Y REPRODUCIR YOUTUBE
    # --------------------------------

    elif tool_name == "search_and_play_youtube":

        query = arguments.get(
            "query",
            ""
        )

        return search_and_play_youtube(query)

    # --------------------------------
    # HORA
    # --------------------------------

    elif tool_name == "get_time":

        return get_time()

    # --------------------------------
    # SPOTIFY DESKTOP
    # --------------------------------

    elif tool_name == "play_spotify":

        query = arguments.get(
            "query",
            ""
        )

        return play_spotify(query)

    # --------------------------------
    # HERRAMIENTA DESCONOCIDA
    # --------------------------------

    else:

        return (
            f"Herramienta desconocida: "
            f"{tool_name}"
        )