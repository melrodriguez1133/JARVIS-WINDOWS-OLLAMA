def detect_intent(text):

    text = text.lower().strip()

    # ==========================================
    # HORA
    # ==========================================

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

    # ==========================================
    # NOTEPAD
    # ==========================================

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

    # ==========================================
    # ABRIR YOUTUBE
    # ==========================================

    if (
        "abre youtube" in text
        or "abrir youtube" in text
    ):

        return {
            "tool": "open_youtube",
            "arguments": {}
        }

    # ==========================================
    # BUSCAR Y REPRODUCIR YOUTUBE
    # ==========================================

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

            return {
                "tool": "search_and_play_youtube",
                "arguments": {
                    "query": query
                }
            }

    return None