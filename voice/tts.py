import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


def get_voices():

    voices = engine.getProperty("voices")

    print("\n" + "=" * 45)
    print("        🔊 VOCES DISPONIBLES")
    print("=" * 45)

    for i, voice in enumerate(voices):

        print(f"[{i}] {voice.name}")

    print("=" * 45)

    return voices


def select_voice():

    voices = get_voices()

    if not voices:

        print("❌ No se encontraron voces.")

        return

    while True:

        try:

            option = input(
                "\nSelecciona una voz: "
            ).strip()

            index = int(option)

            if 0 <= index < len(voices):

                engine.setProperty(
                    "voice",
                    voices[index].id
                )

                print(
                    f"\n✅ Voz seleccionada: "
                    f"{voices[index].name}"
                )

                speak(
                    f"Hola, soy JARVIS. "
                    f"Has seleccionado la voz "
                    f"{voices[index].name}."
                )

                break

            print("❌ Número de voz inválido.")

        except ValueError:

            print(
                "❌ Introduce solamente el número."
            )


def speak(text):

    if not text:

        return

    print(f"🔊 JARVIS: {text}")

    engine.say(text)

    engine.runAndWait()