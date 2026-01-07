import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_db_engine():

    load_dotenv()

    server = os.getenv('DB_SERVER')
    db = os.getenv('DB_NAME')

    con = f"mssql+pyodbc://{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection"

    engine = create_engine(con)

    return engine

    
        
def get_customers():
    
    engine = get_db_engine()
    
    with engine.connect() as conexion:    
        query = """
                SELECT 
                    BusinessEntityID, 
                    FirstName, 
                    LastName, 
                    CONCAT(FirstName,' ', LastName) as FullName
                FROM Person.Person;
        """
        df = pd.read_sql(query,conexion)
        
        return df
    
if __name__ == "__main__":
    df = get_customers()
    print(df.head())
    

    df_full =  df['FullName'].tolist()
    
    print(df_full)