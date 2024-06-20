from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the ProctorHistoryModel table
class ProctorHistoryModel(Base):
    __tablename__ = 'proctors_history'

    id = Column(Integer, autoincrement=True)
    proctor_cred_id = Column(Integer, primary_key=True)
    test_date = Column(Date, nullable=False)
    institution = Column(String(255), nullable=False)
    test_type = Column(Integer, nullable=False)
    test_session = Column(Integer, nullable=False)

# Create the table
Base.metadata.create_all(engine)

print("Table created successfully")
