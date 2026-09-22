import sounddevice as sd
import speech_recognition as sr


# ============================================================
# CONFIGURACIÓN DE AUDIO
# ============================================================

SAMPLE_RATE = 16000
CHANNELS = 1
LISTEN_SECONDS = 5


# ============================================================
# SPEECH TO TEXT
# ============================================================

def listen():

    print("🎤 Escuchando...")

    recognizer = sr.Recognizer()

    try:

        # --------------------------------
        # GRABAR AUDIO
        # --------------------------------

        audio_data = sd.rec(
            int(SAMPLE_RATE * LISTEN_SECONDS),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16"
        )

        sd.wait()

        # --------------------------------
        # CONVERTIR A AUDIO RAW
        # --------------------------------

        audio_bytes = audio_data.tobytes()

        audio = sr.AudioData(
            audio_bytes,
            SAMPLE_RATE,
            2
        )

        print("🧠 Procesando voz...")

        # --------------------------------
        # SPEECH TO TEXT
        # --------------------------------

        text = recognizer.recognize_google(
            audio,
            language="es-ES"
        )

        print(f"📝 Tú dijiste: {text}")

        return text

    except sr.UnknownValueError:

        print(
            "❌ No pude entender lo que dijiste."
        )

        return ""

    except sr.RequestError as error:

        print(
            f"❌ Error del servicio de reconocimiento: {error}"
        )

        return ""

    except Exception as error:

        print(
            f"❌ Error del micrófono: {error}"
        )

        return ""