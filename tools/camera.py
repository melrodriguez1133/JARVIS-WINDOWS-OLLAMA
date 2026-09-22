import os
import time

import cv2
import mediapipe as mp


# ============================================================
# CONFIGURACIÓN
# ============================================================

CAMERA_INDEX = 0

MODEL_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    ),
    "models",
    "hand_landmarker.task"
)


# ============================================================
# MEDIAPIPE
# ============================================================

BaseOptions = mp.tasks.BaseOptions

HandLandmarker = mp.tasks.vision.HandLandmarker

HandLandmarkerOptions = (
    mp.tasks.vision.HandLandmarkerOptions
)

RunningMode = mp.tasks.vision.RunningMode


# ============================================================
# RESULTADO GLOBAL
# ============================================================

latest_result = None


# ============================================================
# DETECTAR DEDOS
# ============================================================

def finger_is_open(hand, tip, pip):
    """
    Detecta si un dedo está extendido.

    Para los dedos índice, medio, anular y meñique
    usamos la posición vertical de la punta respecto
    a la articulación PIP.
    """

    tip_point = hand[tip]
    pip_point = hand[pip]

    return tip_point.y < pip_point.y


# ============================================================
# DETECTAR PULGAR
# ============================================================

def thumb_is_open(hand):

    thumb_tip = hand[4]
    thumb_ip = hand[3]

    # El pulgar extendido normalmente se encuentra
    # más alejado de la palma.

    return (
        abs(
            thumb_tip.x - thumb_ip.x
        ) > 0.04
    )


# ============================================================
# DETECTAR GESTO
# ============================================================

def detect_gesture(hand):

    # --------------------------------------------------------
    # DEDOS
    # --------------------------------------------------------

    index_open = finger_is_open(
        hand,
        8,
        6
    )

    middle_open = finger_is_open(
        hand,
        12,
        10
    )

    ring_open = finger_is_open(
        hand,
        16,
        14
    )

    pinky_open = finger_is_open(
        hand,
        20,
        18
    )

    thumb_open = thumb_is_open(
        hand
    )


    # --------------------------------------------------------
    # 👍 ME GUSTA
    # --------------------------------------------------------

    if (
        thumb_open
        and not index_open
        and not middle_open
        and not ring_open
        and not pinky_open
    ):

        return "ME GUSTA"


    # --------------------------------------------------------
    # ✋ MANO ABIERTA
    # --------------------------------------------------------

    if (
        thumb_open
        and index_open
        and middle_open
        and ring_open
        and pinky_open
    ):

        return "MANO ABIERTA"


    # --------------------------------------------------------
    # ✊ PUÑO
    # --------------------------------------------------------

    if (
        not index_open
        and not middle_open
        and not ring_open
        and not pinky_open
        and not thumb_open
    ):

        return "PUÑO"


    # --------------------------------------------------------
    # DESCONOCIDO
    # --------------------------------------------------------

    return "DESCONOCIDO"


# ============================================================
# DIBUJAR MANO
# ============================================================

def draw_hand(frame, hand):

    height, width, _ = frame.shape


    # --------------------------------------------------------
    # PUNTOS
    # --------------------------------------------------------

    for landmark in hand:

        x = int(
            landmark.x * width
        )

        y = int(
            landmark.y * height
        )

        cv2.circle(
            frame,
            (x, y),
            5,
            (0, 255, 0),
            -1
        )


    # --------------------------------------------------------
    # CONEXIONES
    # --------------------------------------------------------

    connections = (
        mp.tasks.vision
        .HandLandmarksConnections
        .HAND_CONNECTIONS
    )


    for connection in connections:

        start = hand[
            connection.start
        ]

        end = hand[
            connection.end
        ]

        start_point = (
            int(start.x * width),
            int(start.y * height)
        )

        end_point = (
            int(end.x * width),
            int(end.y * height)
        )

        cv2.line(
            frame,
            start_point,
            end_point,
            (0, 255, 0),
            2
        )


# ============================================================
# CALLBACK
# ============================================================

def result_callback(
    result,
    output_image,
    timestamp_ms
):

    global latest_result

    latest_result = result


# ============================================================
# CREAR DETECTOR
# ============================================================

def create_detector():

    if not os.path.exists(MODEL_PATH):

        raise FileNotFoundError(
            "No se encontró el modelo:\n"
            f"{MODEL_PATH}"
        )


    options = HandLandmarkerOptions(

        base_options=BaseOptions(
            model_asset_path=MODEL_PATH
        ),

        running_mode=RunningMode.LIVE_STREAM,

        num_hands=1,

        min_hand_detection_confidence=0.5,

        min_hand_presence_confidence=0.5,

        min_tracking_confidence=0.5,

        result_callback=result_callback
    )


    return HandLandmarker.create_from_options(
        options
    )


# ============================================================
# ACCIONES DE JARVIS
# ============================================================

def execute_gesture_action(gesture):

    if gesture == "ME GUSTA":

        print()
        print("👍 ME GUSTA DETECTADO")
        print("🤖 JARVIS: ¡Entendido!")
        print()


    elif gesture == "MANO ABIERTA":

        print(
            "✋ JARVIS detectó una mano abierta."
        )


    elif gesture == "PUÑO":

        print(
            "✊ JARVIS detectó un puño."
        )


# ============================================================
# INICIAR CÁMARA
# ============================================================

def start_camera():

    global latest_result


    print("=" * 60)

    print(
        "       📷 JARVIS - CONTROL POR GESTOS"
    )

    print("=" * 60)

    print()

    print(
        f"🧠 Modelo: {MODEL_PATH}"
    )

    print()


    # --------------------------------------------------------
    # MODELO
    # --------------------------------------------------------

    if not os.path.exists(MODEL_PATH):

        print(
            "❌ No se encontró el modelo."
        )

        return


    # --------------------------------------------------------
    # CÁMARA
    # --------------------------------------------------------

    camera = cv2.VideoCapture(
        CAMERA_INDEX
    )


    if not camera.isOpened():

        print(
            "❌ No se pudo abrir la cámara."
        )

        return


    print(
        "✅ Cámara iniciada."
    )

    print()

    print(
        "✋ Mano abierta"
    )

    print(
        "✊ Puño"
    )

    print(
        "👍 Me gusta"
    )

    print()

    print(
        "🚪 Presiona Q para salir."
    )

    print()


    last_gesture = ""

    last_action_time = 0

    timestamp_ms = 0


    try:

        with create_detector() as detector:

            while True:

                # ------------------------------------------------
                # LEER FRAME
                # ------------------------------------------------

                success, frame = camera.read()


                if not success:

                    print(
                        "❌ Error leyendo cámara."
                    )

                    break


                # ------------------------------------------------
                # ESPEJO
                # ------------------------------------------------

                frame = cv2.flip(
                    frame,
                    1
                )


                # ------------------------------------------------
                # RGB
                # ------------------------------------------------

                rgb_frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )


                # ------------------------------------------------
                # MEDIAPIPE IMAGE
                # ------------------------------------------------

                mp_image = mp.Image(

                    image_format=(
                        mp.ImageFormat.SRGB
                    ),

                    data=rgb_frame
                )


                # ------------------------------------------------
                # TIMESTAMP
                # ------------------------------------------------

                timestamp_ms += 33


                # ------------------------------------------------
                # DETECTAR
                # ------------------------------------------------

                detector.detect_async(
                    mp_image,
                    timestamp_ms
                )


                # ------------------------------------------------
                # RESULTADO
                # ------------------------------------------------

                result = latest_result

                gesture = "BUSCANDO..."


                if (
                    result is not None
                    and result.hand_landmarks
                ):

                    hand = (
                        result.hand_landmarks[0]
                    )


                    # Dibujar

                    draw_hand(
                        frame,
                        hand
                    )


                    # Detectar

                    gesture = detect_gesture(
                        hand
                    )


                    # ------------------------------------------------
                    # ACCIÓN
                    # ------------------------------------------------

                    current_time = time.time()


                    if (
                        gesture != last_gesture
                        and gesture != "DESCONOCIDO"
                        and (
                            current_time
                            - last_action_time
                            > 2
                        )
                    ):

                        print(
                            f"👋 Gesto detectado: "
                            f"{gesture}"
                        )


                        execute_gesture_action(
                            gesture
                        )


                        last_gesture = gesture

                        last_action_time = (
                            current_time
                        )


                # ------------------------------------------------
                # TEXTO EN PANTALLA
                # ------------------------------------------------

                cv2.putText(

                    frame,

                    gesture,

                    (20, 45),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    1,

                    (0, 255, 0),

                    2
                )


                # ------------------------------------------------
                # VENTANA
                # ------------------------------------------------

                cv2.imshow(
                    "JARVIS - Gestos",
                    frame
                )


                # ------------------------------------------------
                # SALIR
                # ------------------------------------------------

                key = (
                    cv2.waitKey(1)
                    & 0xFF
                )


                if key == ord("q"):

                    print()

                    print(
                        "🛑 Cámara detenida."
                    )

                    break


    except KeyboardInterrupt:

        print()

        print(
            "🛑 Cámara detenida."
        )


    except Exception as error:

        print()

        print(
            "❌ Error:"
        )

        print(error)


    finally:

        camera.release()

        cv2.destroyAllWindows()

        print(
            "📷 Cámara cerrada."
        )


# ============================================================
# EJECUTAR
# ============================================================

if __name__ == "__main__":

    start_camera()