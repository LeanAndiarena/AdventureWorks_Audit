import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

def get_db_engine():
    try:
        load_dotenv()
        
            
        server = os.getenv('DB_SERVER')
        db = os.getenv('DB_NAME')

        con = f"mssql+pyodbc://{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection"

        engine = create_engine(con)

        logging.info(f"Conexión exitosa a la base de datos {db}")
        return engine

    except Exception as e:
        logging.error(f"❌ Error crítico en db.py: {e}")
         
        
def get_customers():
    
    try:
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
            
            logging.info(f"Query realizada con exito y dataframe creado")
            return df
        
    except Exception as e:
        
        logging.error(f"❌ Error crítico en db.py: {e}")
        return pd.DataFrame() # Devolvemos un DF vacío para que no rompa el siguiente paso
     
     
if __name__ == "__main__":
    df = get_customers()
    print(df.head())
    

    df_full =  df['FullName'].tolist()
    
    print(df_full)