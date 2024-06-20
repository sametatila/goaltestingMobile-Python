from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base
from database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the ProctorCredModel table
class ProctorCredModel(Base):
    __tablename__ = 'proctors_cred'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    reg_date = Column(Date, nullable=False)
    is_activated = Column(Boolean, default=False)

# Create the table
Base.metadata.create_all(engine)

print("Table created successfully")
