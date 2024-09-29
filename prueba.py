import requests

# Datos de entrada para la predicción
data = {
    'Ram': 12,  
    'Memory': 120, 
    'Inches': 16.0,     # Cambia esto según los datos de entrada que necesites
    'Weight': 1.5  # Cambia esto según los datos de entrada que necesites
}

# Realizar la solicitud
response = requests.post('http://127.0.0.1:5000/predict', json=data)
# Imprimir la respuesta
print(response.json())