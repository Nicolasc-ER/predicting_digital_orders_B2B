!pip install -r requirements.txt
import mlflow
import pandas as pd
from flask import Flask, request, jsonify

# --- 1. Cargar el Modelo desde MLflow ---

# IDs de tu experimento y de la mejor ejecución (run)
RUN_ID = "af5ed57b2547405a9c26fee31c350ed8"
EXPERIMENT_ID = "384562385199565" # Opcional, pero buena práctica

# Construir la URI del modelo en el formato 'runs:/<RUN_ID>/<ARTIFACT_PATH>'
# El 'artifact_path' es el nombre que le dimos al modelo al guardarlo.
model_uri = f"runs:/{RUN_ID}/sklearn-model"

# Cargar el modelo como una función de Python (PyFunc)
# PyFunc se encarga de todo el preprocesamiento y la predicción.
print("Cargando modelo desde MLflow...")
model = mlflow.pyfunc.load_model(model_uri)
print("Modelo cargado exitosamente.")


# --- 2. Configurar el Servidor Web con Flask ---

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    """
    Función que se ejecuta cuando se recibe una petición POST en el endpoint /predict.
    """
    try:
        # Obtener los datos JSON de la petición
        json_data = request.get_json()
        
        # Convertir los datos a un DataFrame de Pandas
        # Se espera un formato como: {"data": [{"feature1": val1, "feature2": val2}, ...]}
        data_df = pd.DataFrame(json_data['data'])
        
        # Realizar la predicción de probabilidades
        # El modelo pipeline se encarga de todo el preprocesamiento.
        # Usamos predict_proba para obtener la probabilidad, no solo la clase (0 o 1).
        predictions_proba = model.predict_proba(data_df)
        
        # La salida es un array de [prob_clase_0, prob_clase_1].
        # Nos interesa la probabilidad de la clase 1 (predicción de que será digital).
        probability_digital = [p[1] for p in predictions_proba]

        # Devolver las predicciones en formato JSON
        return jsonify({
            "status": "success",
            "predictions": probability_digital
        })

    except Exception as e:
        # Manejo de errores
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# --- 3. Ejecutar la Aplicación ---

if __name__ == '__main__':
    # Inicia el servidor en el puerto 5001, accesible desde cualquier IP.
    app.run(host='0.0.0.0', port=5001)