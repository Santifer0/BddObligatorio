# Conexión Frontend-Backend

## Resumen
Este proyecto conecta un frontend en React (Vite) con un backend en Python (Flask) que accede a una base de datos MySQL.

## Arquitectura
```
Frontend (React + Vite) -> API REST (Flask) -> Base de Datos (MySQL)
     Puerto 5173              Puerto 5000         Puerto 3306
```

## Configuración

### Backend (Flask)
- **Archivo principal**: `app.py`
- **Puerto**: 5000
- **Dependencias**: Flask, Flask-CORS, mysql-connector-python

### Frontend (React)
- **Directorio**: `Frontend/obligatorioBasesDeDatos/`
- **Puerto**: 5173 (por defecto de Vite)
- **Servicio API**: `src/services/apiService.js`

## Cómo ejecutar

### Opción 1: Ejecutar todo a la vez
```bash
# Ejecutar desde el directorio raíz
start_all.bat
```

### Opción 2: Ejecutar por separado

#### Backend:
```bash
# Desde el directorio raíz
start_backend.bat

# O manualmente:
cd "c:\Users\juanm\OneDrive\Documentos\ucu\Base de datos\BddObligatorio"
"c:/Users/juanm/OneDrive/Documentos/ucu/Base de datos/BddObligatorio/.venv/Scripts/python.exe" app.py
```

#### Frontend:
```bash
# Desde el directorio raíz
start_frontend.bat

# O manualmente:
cd Frontend/obligatorioBasesDeDatos
npm run dev
```

## Endpoints de la API

### POST /api/login
Autentica un usuario en el sistema.

**Body:**
```json
{
  "correo": "usuario@ejemplo.com",
  "contraseña": "password123"
}
```

**Respuesta exitosa:**
```json
{
  "success": true,
  "es_administrador": false,
  "message": "Login exitoso"
}
```

**Respuesta de error:**
```json
{
  "success": false,
  "message": "Credenciales incorrectas"
}
```

### GET /api/test-db
Prueba la conexión con la base de datos.

**Respuesta:**
```json
{
  "message": "Conexión a base de datos exitosa"
}
```

## Uso del servicio API en React

```javascript
import apiService from '../src/services/apiService';

// Ejemplo de login
try {
  const response = await apiService.login(correo, contraseña);
  if (response.success) {
    // Usuario autenticado
    console.log('Es administrador:', response.es_administrador);
  }
} catch (error) {
  console.error('Error en login:', error.message);
}
```

## Próximos pasos

Para agregar más funcionalidades:

1. **En el backend (`app.py`)**: Agrega nuevos endpoints para otras operaciones
2. **En el servicio (`apiService.js`)**: Agrega métodos para llamar a los nuevos endpoints
3. **En los componentes de React**: Usa el servicio para hacer las llamadas

### Ejemplo para agregar operaciones CRUD de máquinas:

**Backend:**
```python
@app.route('/api/maquinas', methods=['GET'])
def get_maquinas():
    # Lógica para obtener máquinas
    pass

@app.route('/api/maquinas', methods=['POST'])
def create_maquina():
    # Lógica para crear máquina
    pass
```

**Frontend:**
```javascript
// En apiService.js
async getMaquinas() {
    return this.request('/maquinas');
}

async createMaquina(maquinaData) {
    return this.request('/maquinas', {
        method: 'POST',
        body: JSON.stringify(maquinaData),
    });
}
```

## Troubleshooting

### Error de CORS
Si ves errores de CORS, verifica que Flask-CORS esté instalado y configurado en `app.py`.

### Error de conexión a base de datos
Verifica las credenciales en `dataBase.py` y que MySQL esté ejecutándose.

### Frontend no puede conectar al backend
Verifica que el backend esté ejecutándose en el puerto 5000 y que la URL en `apiService.js` sea correcta.
