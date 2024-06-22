import pandas as pd
from sqlalchemy import create_engine
from database_models.database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Get data from iopssablon table
with engine.connect() as connection:
    result = connection.execute("SELECT DISTINCT test_date, school, room, test_session FROM iopssablon")
    data = result.fetchall()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['test_date', 'school', 'room', 'test_session'])

# Export the DataFrame to a CSV file
df.to_csv('data.csv', index=False)