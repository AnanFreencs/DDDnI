from flask import Flask, jsonify
import random  # Untuk mensimulasikan pembacaan sensor

app = Flask(__name__)

@app.route('/get-sensor-data', methods=['GET'])
def get_sensor_data():
    # Simulasi data dari sensor MAX30102
    sensor_data = {
        "glukosa": random.uniform(70, 150),  # Kadar glukosa darah (mg/dl)
        "heart_rate": random.randint(60, 100),  # Detak jantung per menit
        "spo2": random.uniform(95, 100)  # Saturasi oksigen
    }
    return jsonify(sensor_data)

@app.route('/predict-diabetes', methods=['POST'])
def predict_diabetes():
    # Simulasi deteksi diabetes berdasarkan input
    data = request.get_json()
    glukosa = data['glukosa']
    heart_rate = data['heart_rate']
    spo2 = data['spo2']
    usia = data['usia']
    
    # Implementasi model ML (misalnya, model sederhana dengan threshold)
    if glukosa > 120:
        result = "Positif Diabetes"
        suggestion = "Disarankan untuk berkonsultasi dengan dokter."
    else:
        result = "Negatif Diabetes"
        suggestion = "Kadar gula darah Anda normal. Tetap jaga pola hidup sehat."
    
    return jsonify({"result": result, "suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
