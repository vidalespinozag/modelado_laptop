from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el modelo
model = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del request
    data = request.get_json(force=True)
    
    # Convertir a DataFrame
    input_data = pd.DataFrame(data, index=[0])
    
    # Realizar la predicción
    prediction = model.predict(input_data)
    
    # Devolver la predicción como JSON
    return jsonify(price=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)