from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de conexión con PyMySQL para MySQL 8.x [cite: 1233, 1234]
# Reemplaza 'usuario', 'password', 'localhost' y 'finistrabaja_db' con tus credenciales locales.
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/finistrabaja_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para generar las tablas en la base de datos
def init_db():
    from models import Base # Importar la base de tus modelos
    Base.metadata.create_all(bind=engine)