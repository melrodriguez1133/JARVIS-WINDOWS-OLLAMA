from tools.router import execute_tool


# ============================================================
# HERRAMIENTAS PERMITIDAS
# ============================================================

ALLOWED_TOOLS = {
    "open_notepad",
    "open_youtube",
    "search_youtube",
    "search_and_play_youtube",
    "get_time",
    "play_spotify",
}


# ============================================================
# EJECUTOR SEGURO
# ============================================================

def execute_safely(tool_name, arguments=None):

    if tool_name not in ALLOWED_TOOLS:

        return (
            "Acción bloqueada. "
            "La herramienta no está permitida."
        )

    return execute_tool(
        tool_name,
        arguments
    )