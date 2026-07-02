# Finis Trabaja — Prototipo de Validación

Instrucciones para configurar la base de datos, levantar el backend, ejecutar el frontend y trabajar con el repositorio en Git.

---

## 1. Requisitos previos

Asegúrate de tener instalado:

- **Python** 3.10 o superior
- **Node.js** y **npm**
- **Servidor MySQL** — se recomienda **XAMPP** (incluye MySQL + phpMyAdmin listos para usar)
- **Git**

> **Nota sobre XAMPP:** phpMyAdmin se sirve a través de **Apache**, no de MySQL. Si al entrar a `http://localhost/phpmyadmin` la conexión es rechazada, verifica que **ambos** servicios (Apache y MySQL) estén en estado "Running" en el panel de XAMPP.

---

## 2. Configuración de la base de datos (MySQL)

1. Enciende tu servidor local de MySQL (y Apache, si usas XAMPP y quieres phpMyAdmin).
2. Crea la base de datos ejecutando esta consulta SQL (desde phpMyAdmin, pestaña **SQL**, o por línea de comandos):
   ```sql
   CREATE DATABASE finistrabaja_db;
   ```
3. Revisa las credenciales en `backend/database.py`:
   ```python
   SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/finistrabaja_db"
   ```
   Esta es la configuración por defecto de XAMPP (usuario `root`, **sin contraseña**). Si tu servidor MySQL usa credenciales distintas, actualiza `usuario` y `contraseña` en esa línea.

---

## 3. Levantar el backend (FastAPI)

1. Abre una terminal y entra a la carpeta del backend:
   ```bash
   cd backend
   ```
2. Crea y activa el entorno virtual:

   **Windows:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   > Cada persona debe generar **su propio** entorno virtual localmente. La carpeta `venv/` no se sube al repositorio (está en `.gitignore`), ya que contiene rutas absolutas específicas de cada equipo y no funciona si se comparte entre máquinas distintas.

3. Instala las librerías necesarias:
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql
   ```
4. Puebla la base de datos — **ejecutar solo una vez**, para crear las tablas y datos de prueba:
   ```bash
   python poblarbd.py
   ```
5. Inicia el servidor del backend (déjalo corriendo):
   ```bash
   uvicorn main:app --reload
   ```
   La API estará disponible en `http://localhost:8000`. La documentación interactiva (Swagger) está en `http://localhost:8000/docs`.

---

## 4. Levantar el frontend (Vue 3)

1. Abre una **nueva terminal** (sin cerrar la del backend) y entra a la carpeta del frontend:
   ```bash
   cd frontend
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia el servidor web:
   ```bash
   npm run dev
   ```
   La página estará disponible en `http://localhost:5173`.

---

## 5. Comportamiento esperado del prototipo

Este prototipo fue construido siguiendo un requisito específico del profesor: al seleccionar una oferta desde la **vista de estudiante**, esta se elimina automáticamente de la lista disponible (simulando que ya fue tomada).

Esto significa que, tras interactuar con la página y tomar ofertas, **la vista de estudiante puede aparecer vacía** — no es un error, es el comportamiento esperado una vez que ya no quedan ofertas disponibles para tomar.

**Para volver a ver ofertas disponibles** (por ejemplo, para hacer una nueva demostración o prueba), es necesario restablecer los datos desde la base de datos. Las opciones son:

- Volver a ejecutar el script de datos base:
  ```bash
  python poblar_bd.py
  ```
  *(revisar si el script requiere vaciar antes las tablas relacionadas, o si lo hace automáticamente al ejecutarse)*
- O modificar manualmente los registros correspondientes directamente desde phpMyAdmin, restaurando el estado de las ofertas para que vuelvan a marcarse como disponibles.

---

## 6. Notas para quien clone este repositorio desde cero

- Si tras clonar el repo aparece un error del tipo `Fatal error in launcher` al usar `pip`, significa que quedó una carpeta `venv` antigua sin eliminar correctamente del repositorio — borra `backend/venv` y créala de nuevo con `python -m venv venv`.
- Si aparece `Access denied for user 'root'@'localhost'` al ejecutar `poblar_bd.py`, revisa que la línea de conexión en `backend/database.py` coincida con las credenciales reales de tu servidor MySQL (ver sección 2).

---

## 7. Flujo de trabajo con Git

Para subir cambios al repositorio:

```bash
git add .
git commit -m "Descripción breve del cambio"
git pull
git push
```

> Se recomienda ejecutar siempre `git pull` antes de `git push` para traer los cambios de otros integrantes del equipo y evitar conflictos.

Si es la primera vez que usas Git en tu equipo, configura tu identidad antes del primer commit:
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```
