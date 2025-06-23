from flask import Flask, request, jsonify
import cv2
import numpy as np
import joblib
from PIL import Image
import io
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Enables CORS for all routes

# ✅ Load your trained model
model = joblib.load("anemia_rf_model.pkl")




# ✅ Helper function to extract RGB percentages
def extract_rgb_percentages(image):
    image = cv2.resize(image, (128, 128))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    total_pixels = image.shape[0] * image.shape[1]
    red_count = np.sum(image[:, :, 0]) / 255
    green_count = np.sum(image[:, :, 1]) / 255
    blue_count = np.sum(image[:, :, 2]) / 255
    red_pct = (red_count / total_pixels)
    green_pct = (green_count / total_pixels)
    blue_pct = (blue_count / total_pixels)
    return red_pct, green_pct, blue_pct

@app.route("/predict-image", methods=["POST", "OPTIONS"])
def predict_image():
    if request.method == "OPTIONS":
        return '', 204  # Preflight response

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image_stream = file.read()
    pil_image = Image.open(io.BytesIO(image_stream)).convert("RGB")
    image = np.array(pil_image)

    red, green, blue = extract_rgb_percentages(image)
    hb = 10.5  # Dummy Hb value for now

    # Feature vector
    features = np.array([[red * 100, green * 100, blue * 100, hb]])
    
    prediction = model.predict(features)
    proba = model.predict_proba(features)[0]  # Class probabilities
    confidence = round(max(proba) * 100, 2)

    label = "anemic" if prediction[0] == 1 else "not anemic"

    return jsonify({
        "result": {
            "label": label,
            "timestamp": datetime.datetime.now().isoformat(),
            "hemoglobin": hb,
            "confidence": confidence
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
