from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base
from database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the ProctorModel table
class ProctorModel(Base):
    __tablename__ = 'proctors'

    id = Column(Integer, autoincrement=True)
    proctor_cred_id = Column(Integer, primary_key=True)
    user_type = Column(Integer)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_prefix = Column(String(4))
    phone = Column(BigInteger)
    province = Column(String(50))
    district = Column(String(50))
    tc_no = Column(BigInteger)
    bank = Column(String(100))
    iban = Column(String(26))

# Create the table
Base.metadata.create_all(engine)

print("Table created successfully")
