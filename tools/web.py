import webbrowser
from urllib.parse import quote


def open_youtube():

    webbrowser.open("https://www.youtube.com")

    return "YouTube fue abierto."


def search_youtube(query: str):

    url = (
        "https://www.youtube.com/results?search_query="
        + quote(query)
    )

    webbrowser.open(url)

    return f"Buscando {query} en YouTube."