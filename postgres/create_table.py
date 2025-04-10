from sqlalchemy import create_engine
from Model import Base, Salaries  # Import your Base and Salaries class

# Define your database connection parameters
host = 'localhost'
database = 'mydatabase'
user = 'myuser'
password = 'mypassword'
port = '5434'

# Create a connection string
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

Base.metadata.drop_all(engine)  # Drop the table if it exists
# Create the table in the database
Base.metadata.create_all(engine)

print("Table 'salaries' has been created successfully!")