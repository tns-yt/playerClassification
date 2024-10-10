from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    print(os.getcwd())
    try:
        image_data = request.form.get('image_data')
        if not image_data:
            return jsonify({"error": "No image data received"}), 400
        
        result = util.classify_image(image_data)
        return jsonify(result)
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'hi'

if __name__ == "__main__":
    # app.run(debug=True)
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)