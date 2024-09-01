from sqlalchemy import create_engine,text, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base
from database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the ProctorHistoryModel table
class SeasonPlanModel(Base):
    __tablename__ = 'seasonplan'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tarih = Column(Integer)
    durum = Column(String(255))
    okul = Column(String(255))
    tca = Column(String(255))
    seans = Column(Float)
    aciklamalar = Column(String(1000))
    gozetmen = Column(Integer)
    pbt_sinif = Column(Integer)
    cbt_sinif = Column(Integer)
    ps1 = Column(Integer)
    ps2 = Column(Integer)
    pspk = Column(Integer)
    js = Column(Integer)
    jspk = Column(Integer)
    itp = Column(Integer)
    muhattap = Column(String(255))
    muhattap_tel = Column(String(255))
    muhattap_eposta = Column(String(255))
    konum = Column(String(255))

# Create the table
Base.metadata.create_all(engine)

print("Table created successfully")
with engine.connect() as connection:
    # Uyku modundaki bağlantıları listeleme
    result = connection.execute(text("SELECT id FROM information_schema.processlist WHERE Command = 'Sleep';"))
    sleep_connections = result.fetchall()

    # Uyku modundaki bağlantıları kapatma
    for conn_id in sleep_connections:
        print(f"Kapatılan bağlantı ID'si: {conn_id[0]}")
        # connection.execute(text(f"KILL {conn_id[0]};"))

# Bağlantıyı kapat
engine.dispose()

