from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base, Session
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

# Create a sample ProctorModel object
proctor_details = [
    ProctorModel(proctor_cred_id=4,
                 user_type=4,
                 first_name='Thomas',
                 last_name='Anderson',
                 phone_prefix='+90',
                 phone=5455444433,
                 province='Ankara',
                 district='Çankaya',
                 tc_no=11223344551,
                 bank='Garanti BBVA',
                 iban='11111111111111111111111111'),
    ProctorModel(proctor_cred_id=5,
                 user_type=4,
                 first_name='John',
                 last_name='Doe',
                 phone_prefix='+90',
                 phone=1234567890,
                 province='New York',
                 district='Manhattan',
                 tc_no=1234567890,
                 bank='Garanti BBVA',
                 iban='22222222222222222222222222'),
    ProctorModel(proctor_cred_id=9,
                 user_type=4,
                 first_name='Jane',
                 last_name='Smith',
                 phone_prefix='+90',
                 phone=9876543210,
                 province='London',
                 district='Westminster',
                 tc_no=9876543210,
                 bank='Garanti BBVA',
                 iban='33333333333333333333333333'),
    ProctorModel(proctor_cred_id=7,
                 user_type=4,
                 first_name='Max',
                 last_name='Mustermann',
                 phone_prefix='+90',
                 phone=5555555555,
                 province='Berlin',
                 district='Mitte',
                 tc_no=5555555555,
                 bank='Garanti BBVA',
                 iban='44444444444444444444444444'),
    ProctorModel(proctor_cred_id=8,
                 user_type=4,
                 first_name='Maria',
                 last_name='Garcia',
                 phone_prefix='+90',
                 phone=9999999999,
                 province='Madrid',
                 district='Salamanca',
                 tc_no=9999999999,
                 bank='Garanti BBVA',
                 iban='55555555555555555555555555')
]

with Session(engine) as session:
    session.add_all(proctor_details)
    session.commit()