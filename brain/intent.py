# ============================================================
# DETECCIÓN DE INTENCIONES DE JARVIS
# ============================================================


def detect_intent(text):

    text = text.lower().strip()


    # ========================================================
    # HORA
    # ========================================================

    if (
        "qué hora" in text
        or "que hora" in text
        or "hora actual" in text
        or "dime la hora" in text
    ):

        return {
            "tool": "get_time",
            "arguments": {}
        }


    # ========================================================
    # NOTEPAD
    # ========================================================

    if (
        "abre el bloc" in text
        or "abrir el bloc" in text
        or "abre bloc" in text
        or "notepad" in text
    ):

        return {
            "tool": "open_notepad",
            "arguments": {}
        }


    # ========================================================
    # ABRIR YOUTUBE
    # ========================================================

    if (
        "abre youtube" in text
        or "abrir youtube" in text
    ):

        return {
            "tool": "open_youtube",
            "arguments": {}
        }


    # ========================================================
    # BUSCAR Y REPRODUCIR YOUTUBE
    # ========================================================

    youtube_phrases = [
        "busca en youtube",
        "buscar en youtube",
        "busca youtube",
        "buscar youtube"
    ]


    for phrase in youtube_phrases:

        if phrase in text:

            query = text.replace(
                phrase,
                ""
            ).strip()


            if query:

                return {
                    "tool": "search_and_play_youtube",
                    "arguments": {
                        "query": query
                    }
                }


    # ========================================================
    # SPOTIFY
    # ========================================================

    spotify_phrases = [
        "reproduce en spotify",
        "reproducir en spotify",
        "pon en spotify",
        "poner en spotify",
        "busca en spotify",
        "buscar en spotify",
        "reproduce spotify",
        "reproducir spotify",
        "pon spotify",
        "poner spotify",
        "busca spotify",
        "buscar spotify"
    ]


    for phrase in spotify_phrases:

        if phrase in text:

            query = text.replace(
                phrase,
                ""
            ).strip()


            if query:

                return {
                    "tool": "play_spotify",
                    "arguments": {
                        "query": query
                    }
                }


    # ========================================================
    # SPOTIFY
    # FORMATO: "REPRODUCE ... EN SPOTIFY"
    # ========================================================

    if "spotify" in text:

        spotify_query = text.replace(
            "spotify",
            ""
        ).strip()


        spotify_query = (
            spotify_query
            .replace("reproduce", "")
            .replace("reproducir", "")
            .replace("pon", "")
            .replace("poner", "")
            .replace("busca", "")
            .replace("buscar", "")
            .strip()
        )


        if spotify_query:

            return {
                "tool": "play_spotify",
                "arguments": {
                    "query": spotify_query
                }
            }


    # ========================================================
    # CÁMARA
    # ========================================================

    if (
        "abre la cámara" in text
        or "abre cámara" in text
        or "abrir la cámara" in text
        or "abrir cámara" in text
        or "activa la cámara" in text
        or "activa cámara" in text
        or "activar la cámara" in text
        or "activar cámara" in text
        or "enciende la cámara" in text
        or "enciende cámara" in text
    ):

        return {
            "tool": "start_camera",
            "arguments": {}
        }


    # ========================================================
    # CMD / WINDOWS
    # ========================================================

    cmd_commands = {

        # ----------------------------------------------------
        # IPCONFIG
        # ----------------------------------------------------

        "ipconfig": [
            "ipconfig",
            "ip config",
            "ip-config",

            "ejecuta ipconfig",
            "ejecuta ip config",

            "ejecutar ipconfig",
            "ejecutar ip config",

            "corre ipconfig",
            "corre ip config",

            "muestra ipconfig",
            "muestra ip config",

            "muestra mi ip",
            "muéstrame mi ip",
            "muestrame mi ip",

            "ver mi ip",

            "cuál es mi ip",
            "cual es mi ip"
        ],


        # ----------------------------------------------------
        # HOSTNAME
        # ----------------------------------------------------

        "hostname": [
            "hostname",

            "nombre del equipo",

            "nombre de mi computadora",

            "nombre de mi pc"
        ],


        # ----------------------------------------------------
        # WHOAMI
        # ----------------------------------------------------

        "whoami": [
            "whoami",

            "qué usuario soy",

            "que usuario soy",

            "mi usuario de windows",

            "usuario de windows"
        ],


        # ----------------------------------------------------
        # DIR
        # ----------------------------------------------------

        "dir": [
            "dir",

            "muestra los archivos",

            "muestra los archivos de la carpeta",

            "lista los archivos",

            "ver archivos"
        ],


        # ----------------------------------------------------
        # VER WINDOWS
        # ----------------------------------------------------

        "ver": [
            "ver windows",

            "versión de windows",

            "version de windows"
        ],


        # ----------------------------------------------------
        # SYSTEMINFO
        # ----------------------------------------------------

        "systeminfo": [
            "systeminfo",

            "información del sistema",

            "informacion del sistema",

            "información de mi pc",

            "informacion de mi pc"
        ]
    }


    # ========================================================
    # BUSCAR COMANDO
    # ========================================================

    for command, phrases in cmd_commands.items():

        for phrase in phrases:

            if phrase in text:

                return {
                    "tool": "run_cmd",
                    "arguments": {
                        "command": command
                    }
                }


    # ========================================================
    # NO SE DETECTÓ NINGUNA INTENCIÓN
    # ========================================================

    return None