# backend/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal
from models import OfertaLaboral, Postulacion, CVV

app = FastAPI()

# Configuración CORS para que el frontend (Vue/HTML) pueda consumir la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FUNCIONALIDAD A: Empresa visualiza sus ofertas habilitadas
@app.get("/empresas/{empresa_id}/ofertas")
def ver_ofertas_empresa(empresa_id: int, db: Session = Depends(get_db)):
    return db.query(OfertaLaboral).filter(OfertaLaboral.empresa_id == empresa_id).all()

# FUNCIONALIDAD B1: Estudiante visualiza ofertas (que NO ha tomado aún)
@app.get("/estudiantes/{estudiante_id}/ofertas")
def ver_ofertas_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    cvv = db.query(CVV).filter(CVV.estudiante_id == estudiante_id).first()
    
    # Buscar a qué ofertas ya postuló el estudiante
    postulaciones = db.query(Postulacion.oferta_id).filter(Postulacion.cvv_id == cvv.id).all()
    ids_postuladas = [p[0] for p in postulaciones]
    
    # Retornar solo las activas que NO estén en la lista de postuladas
    query = db.query(OfertaLaboral).filter(OfertaLaboral.estado == "Activa")
    if ids_postuladas:
        query = query.filter(OfertaLaboral.id.notin_(ids_postuladas))
        
    return query.all()

# FUNCIONALIDAD B2: Estudiante toma una oferta
@app.post("/estudiantes/{estudiante_id}/postular/{oferta_id}")
def postular_oferta(estudiante_id: int, oferta_id: int, db: Session = Depends(get_db)):
    cvv = db.query(CVV).filter(CVV.estudiante_id == estudiante_id).first()
    
    nueva_postulacion = Postulacion(
        cvv_id=cvv.id, 
        oferta_id=oferta_id, 
        estado_postulacion="Enviada"
    )
    db.add(nueva_postulacion)
    db.commit()
    return {"mensaje": "Postulación realizada con éxito"}