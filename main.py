from brain.ollama import ask_ollama
from brain.prompt import SYSTEM_PROMPT
from brain.intent import detect_intent
from sandbox.executor import execute_safely

from voice.stt import listen
from voice.tts import speak, select_voice


# ============================================================
# JARVIS - APLICACIÓN PRINCIPAL
# ============================================================

def main():

    print("=" * 50)
    print("          🤖 JARVIS ASISTENTE IA")
    print("=" * 50)
    print()

    # ========================================================
    # CONFIGURAR VOZ
    # ========================================================

    select_voice()

    print()
    print("=" * 50)
    print("🎤 ENTER = hablar")
    print("⌨️  Escribe = texto")
    print("🚪 Escribe 'salir' para terminar")
    print("=" * 50)
    print()

    # ========================================================
    # BUCLE PRINCIPAL
    # ========================================================

    while True:

        try:

            user_input = input(
                "🎤 ENTER = voz | escribe = texto\n"
                "Tú: "
            )

        except KeyboardInterrupt:

            print()
            print("👋 JARVIS finalizado.")
            break

        voice_mode = False

        # ====================================================
        # MODO VOZ
        # ====================================================

        if user_input.strip() == "":

            voice_mode = True

            user_input = listen()

        # ====================================================
        # SIN ENTRADA
        # ====================================================

        if not user_input:

            print(
                "⚠️ No recibí ninguna entrada."
            )

            print()

            continue

        user_input = user_input.strip()

        # ====================================================
        # MOSTRAR ENTRADA
        # ====================================================

        print()
        print("-" * 50)
        print(f"📝 Entrada: {user_input}")
        print("-" * 50)
        print()

        # ====================================================
        # SALIR
        # ====================================================

        if user_input.lower() == "salir":

            response = (
                "Hasta luego. "
                "Fue un placer ayudarte."
            )

            print(
                f"🤖 JARVIS: {response}"
            )

            print()

            if voice_mode:

                speak(response)

            break

        # ====================================================
        # DETECTAR INTENCIÓN
        # ====================================================

        try:

            intent = detect_intent(
                user_input
            )

        except Exception as error:

            print(
                f"❌ Error detectando intención: {error}"
            )

            intent = None

        # ====================================================
        # EJECUTAR HERRAMIENTA
        # ====================================================

        if intent:

            tool_name = intent.get(
                "tool"
            )

            arguments = intent.get(
                "arguments",
                {}
            )

            print(
                f"🧠 Herramienta detectada: "
                f"{tool_name}"
            )

            print(
                f"📦 Argumentos: {arguments}"
            )

            print()

            try:

                result = execute_safely(
                    tool_name,
                    arguments
                )

            except Exception as error:

                result = (
                    "Ocurrió un error al ejecutar "
                    f"la herramienta: {error}"
                )

            print()
            print("🤖 JARVIS:")
            print(result)
            print()

            if voice_mode:

                speak(result)

            continue

        # ====================================================
        # PREGUNTA NORMAL → QWEN
        # ====================================================

        prompt = f"""
{SYSTEM_PROMPT}

Usuario:
{user_input}

Responde de manera clara, natural y fácil de entender.

No menciones herramientas internas, código,
intenciones ni procesos técnicos.

JARVIS:
"""

        try:

            response = ask_ollama(
                prompt
            )

        except Exception as error:

            response = (
                "Lo siento, ocurrió un error "
                f"al consultar el modelo: {error}"
            )

        # ====================================================
        # MOSTRAR RESPUESTA
        # ====================================================

        print()
        print("🤖 JARVIS:")
        print(response)
        print()

        # ====================================================
        # RESPUESTA POR VOZ
        # ====================================================

        if voice_mode:

            speak(response)


# ============================================================
# EJECUTAR JARVIS
# ============================================================

if __name__ == "__main__":

    main()