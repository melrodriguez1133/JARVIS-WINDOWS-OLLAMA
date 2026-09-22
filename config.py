# ============================================================
# CONFIGURACIÓN GENERAL DE JARVIS
# ============================================================

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen3:4b"

OLLAMA_API_KEY = "ollama"


# ============================================================
# VOZ
# ============================================================

WHISPER_MODEL = "base"

WHISPER_DEVICE = "cpu"

WHISPER_COMPUTE_TYPE = "int8"

AUDIO_DEVICE = 1

AUDIO_FILE = "voice_input.wav"

LISTEN_SECONDS = 5


# ============================================================
# CÁMARA
# ============================================================

CAMERA_INDEX = 0


# ============================================================
# MQTT
# ============================================================

MQTT_BROKER = "localhost"

MQTT_PORT = 1883

MQTT_LIGHT_TOPIC = "jarvis/luz"