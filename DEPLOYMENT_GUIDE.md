# 🚀 TRANX - API de Detección de Transacciones Bancarias Fraudulentas

## ✅ ESTADO: API ACTIVA Y FUNCIONANDO

**URL LOCAL:** `http://localhost:8000`

---

## 📊 CÓMO FUNCIONA

### 1. **Interfaz Web (GET /)**
Accede a la página principal para subir imágenes interactivamente.

**URL:** `http://localhost:8000/`

**Pasos:**
1. Abre el navegador
2. Dirígete a `http://localhost:8000/`
3. Haz click en "Seleccionar archivo"
4. Elige una imagen (JPG, PNG, etc.)
5. Haz click en "Analizar Fraude"
6. Verás los patrones detectados y la imagen procesada

---

### 2. **API REST (POST /api/analyze/)**
Endpoint para análisis programático de fraude.

**URL:** `http://localhost:8000/api/analyze/`  
**Método:** `POST`  
**Content-Type:** `multipart/form-data`

#### Parámetros:
- `image` (requerido): Archivo de imagen

#### Respuesta (200 OK):
```json
{
    "fraud_patterns_detected": 0,
    "image": "iVBORw0KGgoAAAANSUhEUgAAA...[base64]...",
    "message": "Se detectaron 0 patrones sospechosos en la transacción"
}
```

---

## 💻 EJEMPLOS DE USO

### **Opción 1: Interfaz Web**
```
1. Abre: http://localhost:8000/
2. Sube una imagen
3. Haz click en "Analizar Fraude"
```

### **Opción 2: cURL (Terminal)**
```bash
curl -X POST -F "image=@tu_imagen.jpg" http://localhost:8000/api/analyze/
```

### **Opción 3: Python**
```python
import requests
import json

with open('tu_imagen.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/analyze/',
        files={'image': f}
    )

resultado = response.json()
print(f"Patrones detectados: {resultado['fraud_patterns_detected']}")
print(f"Mensaje: {resultado['message']}")
```

### **Opción 4: JavaScript/Fetch**
```javascript
const formData = new FormData();
formData.append('image', document.getElementById('fileInput').files[0]);

fetch('http://localhost:8000/api/analyze/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    console.log('Patrones detectados:', data.fraud_patterns_detected);
    console.log('Mensaje:', data.message);
    console.log('Imagen:', data.image);
});
```

### **Opción 5: Postman / Insomnia**
1. Método: `POST`
2. URL: `http://localhost:8000/api/analyze/`
3. Body → form-data
4. Clave: `image` | Valor: (selecciona archivo de imagen)
5. Click en "Send"

---

## 🔧 CONFIGURACIÓN Y MANTENIMIENTO

### Verificar que el servidor está corriendo:
```bash
curl -I http://localhost:8000/
```

### Ver los logs en tiempo real:
```bash
tail -f /tmp/api.log
```

### Detener el servidor:
```bash
pkill -f "python manage.py runserver"
```

### Reiniciar el servidor:
```bash
cd /home/sonia/Descargas/TRANX_FraudDetection
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### Ejecutar pruebas:
```bash
python manage.py test
```

---

## 📁 ESTRUCTURA DEL PROYECTO

```
TRANX_FraudDetection/
├── manage.py                 # Gestor de Django
├── db.sqlite3                # Base de datos
├── requirements.txt          # Dependencias
├── tranx/                    # Proyecto Django
│   ├── __init__.py
│   ├── settings.py           # Configuración
│   ├── urls.py               # Rutas principales
│   └── wsgi.py               # Interfaz WSGI
├── api/                      # App de la API
│   ├── views.py              # Endpoint /api/analyze/
│   ├── urls.py               # Rutas de API
│   └── ...
├── templates/
│   └── index.html            # Interfaz web
└── static/
    └── uploads/              # Carpeta para subidas
```

---

## 🔑 ENDPOINTS DISPONIBLES

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Página principal (interfaz web) |
| POST | `/api/analyze/` | Analizar fraude bancario |
| GET | `/admin/` | Panel de administración Django |

---

## 📊 RESPUESTA DE LA API

La API devuelve siempre un JSON con la siguiente estructura:

```json
{
    "fraud_patterns_detected": <número>,
    "image": "<base64>",
    "message": "<descripción>"
}
```

- **fraud_patterns_detected**: Número de patrones sospechosos encontrados
- **image**: Imagen procesada en formato base64 PNG
- **message**: Mensaje descriptivo del análisis

---

## ⚙️ CONFIGURACIÓN ACTUAL

- **DEBUG:** True (desarrollo)
- **DATABASE:** SQLite3
- **ALLOWED_HOSTS:** ['localhost', '127.0.0.1', '*']
- **STATIC FILES:** Servidos por Django
- **MEDIA FILES:** En `static/uploads/`

---

## 🔐 SEGURIDAD (Para Producción)

Antes de desplegar a producción:

1. Cambiar `SECRET_KEY` en `tranx/settings.py`
2. Establecer `DEBUG = False`
3. Configurar `ALLOWED_HOSTS` con tus dominios
4. Usar HTTPS
5. Instalar certificados SSL
6. Usar Gunicorn/Waitress en lugar de runserver

---

## 📦 DEPENDENCIAS INSTALADAS

- Django 5.2.9
- Django REST Framework 3.16.1
- OpenCV 4.12.0.88
- NumPy 2.2.6
- MediaPipe 0.10.14
- Gunicorn
- WhiteNoise

---

## ✅ PRUEBAS REALIZADAS

✓ Servidor corriendo en http://localhost:8000  
✓ Página principal cargando correctamente  
✓ Endpoint /api/analyze/ respondiendo (200 OK)  
✓ Procesamiento de imágenes funcionando  
✓ Respuesta JSON correcta con base64  

---

## 🆘 SOLUCIÓN DE PROBLEMAS

**Problema:** Puerto 8000 ya en uso
```bash
lsof -i :8000
kill -9 <PID>
```

**Problema:** Módulo no encontrado
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Problema:** Migrations
```bash
python manage.py migrate
```

---

## 📞 SOPORTE

Para problemas, verificar:
1. Logs: `/tmp/api.log`
2. Server check: `python manage.py check`
3. Imports: `python -c "from tranx.wsgi import application"`

---

**Última actualización:** 2025-12-15  
**Estado:** ✅ FUNCIONAL Y LISTO PARA USAR

