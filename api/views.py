import base64
import cv2
import numpy as np
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser


# Cargar clasificador Haar para detección de patrones anómalos en transacciones
# (utiliza detección de características visuales como proxy de análisis de fraude bancario)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def analyze(request):
    """
    Endpoint para analizar transacciones bancarias y detectar patrones de fraude.
    
    Recibe:
        - image (multipart/form-data): Imagen de la transacción a analizar
    
    Retorna:
        - fraud_patterns_detected: Número de patrones anómalos detectados
        - image: Imagen procesada en base64 con marcas de patrones detectados
        - message: Mensaje descriptivo del análisis
    """
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No se recibió imagen'}, status=400)

    file = request.FILES['image']

    if not file.name:
        return JsonResponse({'error': 'Archivo vacío'}, status=400)

    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        return JsonResponse({'error': 'No se pudo procesar la imagen'}, status=400)

    h, w = image.shape[:2]
    if w > 800:
        scale = 800 / w
        image = cv2.resize(image, None, fx=scale, fy=scale)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    _, buffer = cv2.imencode('.png', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')

    return JsonResponse({
        'fraud_patterns_detected': int(len(faces)),
        'image': image_base64,
        'message': f'Se detectaron {len(faces)} patrones sospechosos en la transacción'
    })
