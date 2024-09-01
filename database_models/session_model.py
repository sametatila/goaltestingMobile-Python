from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the SessionDetailsModel table
class SessionDetailsModel(Base):
    __tablename__ = 'session_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, unique=True, nullable=False, autoincrement=True, default=100000)
    test_date = Column(Date, nullable=False)
    institution = Column(String(255), nullable=False)
    session_by_tca = Column(Integer)
    session_created = Column(Boolean)

    # Relationship to SessionPartModel
    session_parts = relationship("SessionPartModel", back_populates="session_details")

# Define the SessionPartModel table
class SessionPartModel(Base):
    __tablename__ = 'session_parts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('session_details.session_id'), nullable=False)
    session_by_proctor_id = Column(Integer)
    test_date = Column(Date)
    institution = Column(String(255))
    test_type = Column(Integer)
    test_session = Column(Integer)
    test_classroom = Column(String(50))
    test_time = Column(String(20))
    session_parts_total = Column(Integer)
    session_ready = Column(Boolean)
    session_start = Column(Boolean)
    session_part_index = Column(Integer)
    session_part = Column(String(33))
    session_part_time_bool = Column(Boolean)
    session_part_time = Column(Integer)
    session_break = Column(Boolean)
    session_end = Column(Boolean)

    # Relationship to SessionDetailsModel
    session_details = relationship("SessionDetailsModel", back_populates="session_parts")

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample query data to SessionDetailsModel
session_details = SessionDetailsModel(session_id=100005,test_date='2022-01-02', institution='Sample Institution', session_by_tca=1)
session.add(session_details)
session.commit()

print("Tables created successfully and sample query data added")
