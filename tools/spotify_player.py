import os
import time

from pywinauto import Desktop, keyboard


# ============================================================
# CONFIGURACIÓN
# ============================================================

SPOTIFY_MAX_WAIT = 30
SPOTIFY_STARTUP_WAIT = 5
SEARCH_WAIT = 5


# ============================================================
# BUSCAR VENTANA DE SPOTIFY
# ============================================================

def get_spotify_window():

    try:

        windows = Desktop(
            backend="uia"
        ).windows(
            title_re=".*Spotify.*"
        )

        for window in windows:

            try:

                if window.is_visible():

                    return window

            except Exception:

                continue

    except Exception:

        pass

    return None


# ============================================================
# ABRIR SPOTIFY DESKTOP
# ============================================================

def open_spotify():

    spotify = get_spotify_window()

    if spotify:

        return spotify

    print("🎵 Abriendo Spotify...")

    try:

        os.startfile(
            "spotify:"
        )

    except Exception as error:

        print(
            f"❌ No se pudo abrir Spotify: {error}"
        )

        return None

    # ----------------------------------------
    # ESPERAR A QUE SPOTIFY ABRA
    # ----------------------------------------

    start_time = time.time()

    while time.time() - start_time < SPOTIFY_MAX_WAIT:

        spotify = get_spotify_window()

        if spotify:

            print("✅ Spotify abierto.")

            time.sleep(
                SPOTIFY_STARTUP_WAIT
            )

            return spotify

        time.sleep(1)

    print(
        "❌ No se encontró la ventana de Spotify."
    )

    return None


# ============================================================
# BUSCAR EN SPOTIFY
# ============================================================

def search_spotify(
    spotify,
    query
):

    if not query:

        return (
            "❌ No se indicó qué canción "
            "o artista buscar."
        )

    try:

        print(
            f"🔎 Buscando en Spotify: {query}"
        )

        # ----------------------------------------
        # ACTIVAR SPOTIFY
        # ----------------------------------------

        spotify.set_focus()

        time.sleep(1)

        # ----------------------------------------
        # ABRIR BUSCADOR
        # ----------------------------------------

        keyboard.send_keys(
            "^k"
        )

        time.sleep(1)

        # ----------------------------------------
        # LIMPIAR BÚSQUEDA
        # ----------------------------------------

        keyboard.send_keys(
            "^a"
        )

        # ----------------------------------------
        # ESCRIBIR BÚSQUEDA
        # ----------------------------------------

        keyboard.send_keys(
            query,
            with_spaces=True
        )

        time.sleep(
            SEARCH_WAIT
        )

        # ----------------------------------------
        # ENTER
        #
        # Spotify Desktop utiliza ENTER para
        # seleccionar/reproducir el resultado.
        # ----------------------------------------

        keyboard.send_keys(
            "{ENTER}"
        )

        time.sleep(3)

        return (
            f"🎵 Reproduciendo en Spotify: "
            f"{query}"
        )

    except Exception as error:

        return (
            "❌ Error al controlar Spotify: "
            f"{error}"
        )


# ============================================================
# REPRODUCIR EN SPOTIFY
# ============================================================

def play_spotify(query):

    query = query.strip()

    if not query:

        return (
            "❌ Indica qué canción o artista "
            "quieres reproducir."
        )

    spotify = open_spotify()

    if not spotify:

        return (
            "❌ No pude abrir Spotify Desktop."
        )

    return search_spotify(
        spotify,
        query
    )