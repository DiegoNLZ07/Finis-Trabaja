====================================================================
FINIS TRABAJA - PROTOTIPO DE VALIDACIÓN (INSTRUCCIONES DEL PROYECTO)
====================================================================

Este archivo contiene los pasos exactos para configurar la base de datos, levantar el backend, ejecutar el frontend y subir los cambios a GitHub.

--------------------------------------------------------------------
1. REQUISITOS PREVIOS
--------------------------------------------------------------------
Asegúrate de tener instalado:
- Python (3.10 o superior)
- Node.js y npm
- Servidor MySQL (XAMPP, Workbench, DBeaver, etc.)
- Git

--------------------------------------------------------------------
2. CONFIGURACIÓN DE LA BASE DE DATOS (MySQL)
--------------------------------------------------------------------
1. Enciende tu servidor local de MySQL.
2. Crea la base de datos ejecutando esta consulta SQL:
   CREATE DATABASE finistrabaja_db;
3. Si usas credenciales distintas a root (sin contraseña), actualiza el archivo "backend/database.py" en la línea:
   SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:contraseña@127.0.0.1:3306/finistrabaja_db"

--------------------------------------------------------------------
3. LEVANTAR EL BACKEND (FastAPI)
--------------------------------------------------------------------
1. Abre una terminal y entra a la carpeta del backend:
   cd backend

2. Crea y activa el entorno virtual:
   En Windows: python -m venv venv -> luego ejecuta: venv\Scripts\activate
   En Mac/Linux: python -m venv venv -> luego ejecuta: source venv/bin/activate

3. Instala las librerías necesarias:
   pip install fastapi uvicorn sqlalchemy pymysql

4. Poblar la base de datos (Ejecuta esto SOLO UNA VEZ para crear las tablas y datos base):
   python poblar_bd.py

5. Inicia el servidor del backend (déjalo corriendo):
   uvicorn main:app --reload
   (La API estará disponible en http://localhost:8000)

--------------------------------------------------------------------
4. LEVANTAR EL FRONTEND (Vue 3)
--------------------------------------------------------------------
1. Abre una NUEVA terminal (sin cerrar la del backend) y entra a la carpeta del frontend:
   cd frontend

2. Instala las dependencias:
   npm install

3. Inicia el servidor web:
   npm run dev
   (La página estará disponible en http://localhost:5173)
