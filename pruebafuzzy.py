from rapidfuzz import process, fuzz

nuevos_clientes = ["Juan Perez", "Maria Gonalez", "Carlos Lopéz"]

base_datos = [
    "Juan Antonio Perez", 
    "Maria Elena Gonzalez", 
    "Roberto Diaz", 
    "Caro S. Lo"
]

for nombre in nuevos_clientes:
    
    resultado = process.extractOne(
        query = nombre,
        choices = base_datos,
        scorer = fuzz.WRatio
        
    )
    
    print(f"Buscando a: '{nombre}'")
    print(f"Resultado bruto: {resultado}") 
    print("-" * 30)