import webbrowser
import yt_dlp


def search_and_play_youtube(query: str):

    if not query:
        return "No recibí qué quieres buscar."

    print(f"🔎 Buscando en YouTube: {query}")

    search = f"ytsearch1:{query}"

    options = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:

            result = ydl.extract_info(
                search,
                download=False
            )

        if not result or not result.get("entries"):
            return "No encontré ningún video."

        video = result["entries"][0]

        title = video.get("title", "Video")
        video_url = video.get("url")

        if not video_url:
            video_id = video.get("id")

            if not video_id:
                return "No pude obtener el enlace del video."

            video_url = (
                f"https://www.youtube.com/watch?v={video_id}"
            )

        print(f"🎬 Primer resultado: {title}")
        print(f"🔗 {video_url}")

        webbrowser.open(video_url)

        return (
            f"Encontré '{title}' "
            "y abrí el primer resultado."
        )

    except Exception as error:

        print(f"❌ Error YouTube: {error}")

        return "No pude buscar el video en YouTube."