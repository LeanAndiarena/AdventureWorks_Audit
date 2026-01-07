import pandas as pd
from rapidfuzz import process, fuzz
from src.db import get_customers

def find_duplicates(df_new, df_db):
    
    df_name =  df_db['FullName'].tolist()
    
    list = []
    
    for i, row in df_new.iterrows():
        
        nombre_sucio = row['Nombre_Sucio']
        
        resultado = process.extractOne(
            query= nombre_sucio,
            choices= df_name,
            scorer= fuzz.WRatio
        )
        
        # Desempaquetamos la tupla (Nombre, Score, Indice)
        nombre_encontrado = resultado[0]
        score = resultado[1]
        indice_en_db = resultado[2]       
        
        if score > 85:
            
            # Aquí está el truco: Usamos el índice para buscar el ID original
            # .iloc es para buscar por posición (índice numérico)
            id_real = df_db.iloc[indice_en_db]['BusinessEntityID']
            
            # Guardamos el hallazgo en nuestra lista
            list.append({
                'Nombre_Input': nombre_sucio,
                'Coincidencia_DB': nombre_encontrado,
                'Score': round(score, 2),
                'ID_AdventureWorks': id_real
            })            
    
    # 5. Devolvemos la lista convertida en DataFrame (bonito para leer)
    return pd.DataFrame(list)
    

if __name__ == '__main__':
    print("⏳ Cargando base de datos...")
    df_db = get_customers()
    
    print("⏳ Leyendo archivo de leads...")
    # Ajusté la barra invertida a '/' que es más seguro en Python
    df_new = pd.read_csv('data/leads_nuevos.csv',sep=';')
    
    # 🔍 TRUCO DE DEBUGGING: Imprime esto para ver la verdad
    print("Columnas detectadas:", df_new.columns.tolist())
    
    print("🔍 Buscando duplicados...")
    resultados = find_duplicates(df_new, df_db)
    
    print("\n✅ RESULTADOS ENCONTRADOS:")
    print(resultados)