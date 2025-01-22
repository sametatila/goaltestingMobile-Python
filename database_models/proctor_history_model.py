from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from database_url import DATABASE_URL
from datetime import date, timedelta

# Create the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define the ProctorHistoryModel table
class ProctorHistoryModel(Base):
    __tablename__ = 'proctors_history'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key with auto increment
    proctor_cred_id = Column(Integer, index=True, nullable=True)  # Index, nullable
    test_date = Column(Date, nullable=True)  # Date, nullable
    institution = Column(String(255), nullable=True)  # Varchar(255), nullable
    test_type = Column(Integer, nullable=True)  # Integer, nullable
    test_session = Column(Integer, nullable=True)  # Integer, nullable

# Create the table
Base.metadata.create_all(engine)

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Define the start date for mock data
# start_date = date(2024, 7, 28)

# # List of institutions and test types for variety
# institutions = ["XYZ College", "ABC University"]
# test_types = [20, 21, 4, 5]

# # Add mock data to the table
# for day in range(30):  # 30 gün boyunca her gün için 2 kayıt
#     current_date = start_date + timedelta(days=day)
#     for session_num in range(1, 3):  # Her gün için 2 oturum
#         proctor = ProctorHistoryModel(
#             proctor_cred_id=2,
#             test_date=current_date,
#             institution=institutions[day % len(institutions)],
#             test_type=test_types[day % len(test_types)],
#             test_session=session_num
#         )
#         session.add(proctor)

# # Commit the changes to the database
# session.commit()

# # Close the session
# session.close()

# print("Mock data successfully inserted into the table.")
