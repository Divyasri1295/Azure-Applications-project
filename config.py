import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Secret key for session encryption
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage details
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    # ---------- ✅ Updated Section Starts Here ----------
    # Instead of hardcoding SQL credentials, read full connection string from Azure
    connection_string = os.environ.get("AZURE_SQL_CONNECTIONSTRING")

    if connection_string:
        # URL-encode and format for SQLAlchemy
        params = urllib.parse.quote_plus(connection_string)
        SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    else:
        # Fallback if running locally (optional)
        SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
        SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
        SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
        SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'

        SQLALCHEMY_DATABASE_URI = ('mssql+pyodbc://'+ SQL_USER_NAME+ ':'+ SQL_PASSWORD+ '@'+ SQL_SERVER+ ':1433/'+ SQL_DATABASE+ '?driver=ODBC+Driver+17+for+SQL+Server')

     SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ---------- ✅ Updated Section Ends Here ----------

    ### Info for Microsoft Authentication ###
     CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or "ENTER_CLIENT_SECRET_HERE"
     CLIENT_ID = os.environ.get("CLIENT_ID") or "ENTER_CLIENT_ID_HERE"

    # Multi-tenant endpoint (works for Udacity project)
     AUTHORITY = "https://login.microsoftonline.com/common"

    # Must match the redirect URI registered in Azure App
     REDIRECT_PATH = "/getAToken"

    # Minimal permission scope
     SCOPE = ["User.Read"]

    # Store session info locally (token cache)
     SESSION_TYPE = "filesystem"
