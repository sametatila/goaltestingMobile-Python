from sqlalchemy import create_engine
from database_models.database_url import DATABASE_URL
import pandas as pd

# Create the database engine
engine = create_engine(DATABASE_URL)

# Get data from iopssablon table
with engine.connect() as connection:
    result = connection.execute("SELECT DISTINCT test_date, school, room, test_session FROM iopssablon")
    data = result.fetchall()
    for row in data:
        # Process each row of data here
        print(f'proctor/{row[0]}/{row[1]}/{row[3]}/{row[2]}')

# # Convert the data to a pandas DataFrame
# df = pd.DataFrame(data, columns=['test_date', 'school', 'room', 'test_session'])

# # Export the DataFrame to a CSV file
# df.to_csv('data.csv', index=False)