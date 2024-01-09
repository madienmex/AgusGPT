from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from loopimg import gen_image
from loopchat import run_conversation
from config import config
import os

app = Flask(__name__)

# Allow all origins for all routes (not recommended for production)
#CORS(app)

# If you want to be more specific, you can allow only certain origins for all routes:
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500"]}}, supports_credentials=True)

# Or even more granular, allowing certain origins for specific routes:
# CORS(app, resources={r"/initialize": {"origins": ["http://127.0.0.1:5500"]}})


# Global variable to store messages
messages = []
#config.set_api_key(None)

@app.route('/initialize', methods=['POST'])
# Header authorization attributes from CORS
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def initialize():
    api_key = request.json.get('api_key')
    if api_key is not None:
        config.set_api_key(api_key)
        return jsonify({"status": "initialized", "message": "API key set successfully"})
    else:
        return jsonify({"status": "failed", "message": "API key not found"}) 

@app.route('/selfstart', methods=['POST'])
# Header authorization attributes from CORS
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def selfstart():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is not None:
        config.set_api_key(api_key)
        return jsonify({"status": "initialized", "message": "API key set successfully"})
    else:
        return jsonify({"status": "failed", "message": "API key not found"})    
    

@app.route('/chat', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'application/json'])
def chat():
    if not config.get_api_key():
        return jsonify({"error": "API key not initialized"}), 401  # Unauthorized
    global messages
    data = request.get_json()
    input = data.get('input',0)
    if input.lower() in ['quit', 'exit', 'bye']:
        response = "Chat ended. Goodbye!"
        messages = []  # Reset messages
    else:
        response, messages = run_conversation(input, messages)
    return jsonify({"response": response, "history": messages})

@app.route('/img', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'application/json'])
def img():
    if not config.get_api_key():
        return jsonify({"error": "API key not initialized"}), 401  # Unauthorized
    data = request.get_json()
    input = data.get('input',0)
    if input.lower() in ['quit', 'exit', 'bye']:
        response = "<p>Image not found</p>"
    else:
        response = gen_image(input)
        response = f"<img src='{response}' alt='Generated Image'>"
    
    return make_response(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)