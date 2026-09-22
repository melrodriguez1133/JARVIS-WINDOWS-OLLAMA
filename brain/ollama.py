import requests

from config import OLLAMA_URL, MODEL


# ============================================================
# CONEXIÓN CON OLLAMA
# ============================================================

def ask_ollama(
    prompt: str,
    model: str = MODEL
) -> str:

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            ""
        ).strip()

    except requests.exceptions.ConnectionError:

        return (
            "No puedo conectarme con Ollama. "
            "Verifica que Ollama esté ejecutándose."
        )

    except requests.exceptions.Timeout:

        return (
            "El modelo está tardando demasiado "
            "en responder."
        )

    except Exception as e:

        return (
            f"Ocurrió un error: {e}"
        )