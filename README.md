# API de Detección de Transacciones Bancarias Fraudulentas

Sistema Django REST Framework para detectar patrones sospechosos en imágenes de transacciones bancarias mediante análisis de características visuales.

## Descripción

Esta API analiza imágenes de transacciones bancarias para identificar patrones anómalos que podrían indicar fraude. Utiliza técnicas de procesamiento de imágenes (OpenCV y clasificadores Haar Cascade) para detectar características sospechosas.

## Requisitos

- Python 3.8+
- Django 5.2+
- Django REST Framework 3.16+
- OpenCV 4.12+
- NumPy 2.2+
- MediaPipe 0.10+

## Instalación

1. **Crear entorno virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

4. **Arrancar servidor de desarrollo:**
```bash
python manage.py runserver 0.0.0.0:8000
```

El servidor estará disponible en `http://localhost:8000`

## Uso de la API

### Endpoint: `POST /api/analyze/`

Analiza una imagen para detectar patrones de fraude bancario.

**Parámetros:**
- `image` (multipart/form-data, requerido): Archivo de imagen (PNG, JPG, etc.)

**Ejemplo con cURL:**
```bash
curl -X POST -F "image=@transaccion.jpg" http://localhost:8000/api/analyze/
```

**Respuesta exitosa (200 OK):**
```json
{
    "fraud_patterns_detected": 5,
    "image": "iVBORw0KGgoAAAANSUhEUgAAA...[base64 data]...==",
    "message": "Se detectaron 5 patrones sospechosos en la transacción"
}
```

**Respuesta de error:**
```json
{
    "error": "No se recibió imagen"
}
```

## Interfaz Web

Accede a `http://localhost:8000` para usar la interfaz web interactiva.

## Estructura del Proyecto

```
V_EMOTIONIA_CORREGIDO/
├── manage.py                      # Script de gestión Django
├── requirements.txt               # Dependencias Python
├── README.md                      # Este archivo
├── db.sqlite3                     # Base de datos SQLite (generada)
├── vemotionia/                    # Proyecto Django principal
│   ├── __init__.py
│   ├── settings.py               # Configuración Django
│   ├── urls.py                   # Rutas principales
│   └── wsgi.py                   # Interfaz WSGI
├── api/                           # App de la API
│   ├── __init__.py
│   ├── apps.py                   # Configuración de la app
│   ├── views.py                  # Vistas/endpoints
│   ├── urls.py                   # Rutas de la API
│   └── models.py                 # Modelos (sin usar actualmente)
├── templates/
│   └── index.html                # Interfaz web
└── static/
    └── uploads/                  # Carpeta para subidas (generada)
```

## Configuración para Producción

1. **Cambiar la clave secreta en `vemotionia/settings.py`:**
```python
SECRET_KEY = 'tu-clave-secreta-aqui'
```

2. **Desactivar modo debug:**
```python
DEBUG = False
```

3. **Configurar hosts permitidos:**
```python
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']
```

4. **Usar servidor WSGI/ASGI apropiado (Gunicorn, Waitress, etc.)**

## Tecnologías Utilizadas

- **Django 5.2**: Framework web
- **Django REST Framework**: API REST
- **OpenCV**: Procesamiento de imágenes
- **NumPy**: Operaciones numéricas
- **MediaPipe**: Detección de características

## Notas

- El sistema utiliza clasificadores Haar Cascade preentrenados para detectar patrones visuales.
- Las imágenes se procesan en memoria, no se guardan en disco por defecto.
- La detección es basada en análisis de características visuales como proxy del análisis de fraude.

## Licencia

Uso interno solamente.
