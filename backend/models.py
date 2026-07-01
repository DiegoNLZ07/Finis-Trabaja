from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# 1. Clase Abstracta / Superclase Usuario [cite: 1141, 1557]
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)
    fecha_creacion = Column(Date, default=datetime.utcnow)

    # Configuración para la herencia en SQLAlchemy
    __mapper_args__ = {
        'polymorphic_on': rol,
        'polymorphic_identity': 'usuario'
    }

# 2. Clases que heredan de Usuario [cite: 1141]
class Estudiante(Usuario):
    __tablename__ = 'estudiantes'
    
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    rut = Column(String(12), unique=True, nullable=False)
    nombre_completo = Column(String(150), nullable=False)
    carrera = Column(String(100), nullable=False)
    semestre_actual = Column(Integer, nullable=False)

    # Composición 1:1 con CVV [cite: 1142]
    cvv = relationship("CVV", back_populates="estudiante", uselist=False, cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'estudiante',
    }

class Empresa(Usuario):
    __tablename__ = 'empresas'
    
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    rut_empresa = Column(String(12), unique=True, nullable=False)
    razon_social = Column(String(150), nullable=False)
    giro = Column(String(150), nullable=False)
    estado_validacion = Column(String(50), default="Pendiente") # Inicia en "Pendiente" por defecto [cite: 1277]

    # Relación 1:N con OfertaLaboral [cite: 1143]
    ofertas = relationship("OfertaLaboral", back_populates="empresa", cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'empresa',
    }

class Administrador(Usuario):
    __tablename__ = 'administradores'
    
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    cargo_institucional = Column(String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'administrador',
    }

# 3. Entidad CVV [cite: 1525, 1526, 1527]
class CVV(Base):
    __tablename__ = 'cvvs'
    
    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), unique=True, nullable=False)
    especialidades = Column(String(255))
    pretension_sueldo = Column(Integer)
    disponibilidad_jornada = Column(String(50))
    modalidad_preferida = Column(String(50))
    archivo_cv_url = Column(String(255))
    is_public = Column(Boolean, default=False) # Parámetro de privacidad (toggle) [cite: 1064, 1302]

    estudiante = relationship("Estudiante", back_populates="cvv")
    postulaciones = relationship("Postulacion", back_populates="cvv", cascade="all, delete-orphan")

# 4. Entidad Oferta Laboral [cite: 1538, 1539]
class OfertaLaboral(Base):
    __tablename__ = 'ofertas_laborales'
    
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey('empresas.id'), nullable=False)
    titulo_cargo = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    carreras_dirigidas = Column(String(255))
    rango_sueldo = Column(Integer)
    tipo_jornada = Column(String(50))
    modalidad = Column(String(50))
    ubicacion = Column(String(150))
    estado = Column(String(50), default="Activa")

    empresa = relationship("Empresa", back_populates="ofertas")
    postulaciones = relationship("Postulacion", back_populates="oferta", cascade="all, delete-orphan")

# 5. Entidad Transaccional Postulación (N:M) [cite: 1144]
class Postulacion(Base):
    __tablename__ = 'postulaciones'
    
    id = Column(Integer, primary_key=True, index=True)
    cvv_id = Column(Integer, ForeignKey('cvvs.id'), nullable=False)
    oferta_id = Column(Integer, ForeignKey('ofertas_laborales.id'), nullable=False)
    fecha_postulacion = Column(Date, default=datetime.utcnow)
    carta_presentacion = Column(Text)
    estado_postulacion = Column(String(50), default="Enviada") # Estado inicial "Enviada" [cite: 1380]

    cvv = relationship("CVV", back_populates="postulaciones")
    oferta = relationship("OfertaLaboral", back_populates="postulaciones")