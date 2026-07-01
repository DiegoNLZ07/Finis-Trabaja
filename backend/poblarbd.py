# backend/poblar_bd.py
from database import engine, SessionLocal
from models import Base, Empresa, Estudiante, OfertaLaboral, CVV

# 1. Crear las tablas en MySQL
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# 2. Poblar datos "de mentira" (Sin necesidad de registro/login)
# Crear una empresa
empresa_mock = Empresa(
    correo="miguelitoelmejor@miguelito.cl", contrasena_hash="fakehash", rol="empresa",
    rut_empresa="67.676.767-7", razon_social="Vender furros", giro="Tecnología Furriana", estado_validacion="Aprobado"
)
db.add(empresa_mock)

# Crear un estudiante
estudiante_mock = Estudiante(
    correo="murzuag2@uft.edu", contrasena_hash="fakehash", rol="estudiante",
    rut="22.222.222-2", nombre_completo="Matías Urzúa", carrera="Ingeniería Civil Informática", semestre_actual=9
)
db.add(estudiante_mock)
db.commit() # Guardar para obtener los IDs

# Crear el CVV obligatorio para el estudiante
cvv_mock = CVV(estudiante_id=estudiante_mock.id, is_public=True)
db.add(cvv_mock)

# Crear ofertas laborales habilitadas para esa empresa
oferta1 = OfertaLaboral(
    empresa_id=empresa_mock.id, titulo_cargo="Desarrollador Backend de furros", 
    descripcion="Python, FastAPI y MySQL. Buen gusto en furros", estado="Activa"
)
oferta2 = OfertaLaboral(
    empresa_id=empresa_mock.id, titulo_cargo="Desarrollador grafico de furros", 
    descripcion="Vue 3 y consumo de APIs. Furros en 3d ñam", estado="Activa"
)
db.add(oferta1)
db.add(oferta2)

db.commit()
db.close()

print("Base de datos poblada exitosamente con datos de prueba.")