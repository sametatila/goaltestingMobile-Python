from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base, Session
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

# Create 5 users
users = [
    ProctorCredModel(email='b', password='b', reg_date='2024-01-01', is_activated=True),
#     ProctorCredModel(email='d', password='d', reg_date='2020-01-02', is_activated=True),
#     ProctorCredModel(email='e', password='e', reg_date='2021-01-03', is_activated=True),
#     ProctorCredModel(email='f', password='f', reg_date='2022-01-04', is_activated=True),
#     ProctorCredModel(email='g', password='g', reg_date='2023-01-05', is_activated=True)
]

# Add the users to the session and commit the changes
with Session(engine) as session:
    session.add_all(users)
    session.commit()

print("Users created successfully")
