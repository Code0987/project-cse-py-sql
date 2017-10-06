import os

SECRET_KEY = "secret"
# sql://dbUser:dbPassword@dbServer:dbPort/dbName
DB_URI = os.environ.get("DATABASE_URI", "postgres://project:project@localhost:5432/project")
