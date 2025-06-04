"""
Universal Adapter Backend for Artifact Virtual Chat
Supports OpenAI, Ollama, Gradio, LLM Studio, GGUF (llama.cpp), PyTorch (.pt), and more.
Python 3.8+ required. Flask is used for simplicity.
"""

import os
import json
from flask import Flask, jsonify, request
from typing import List, Dict

app = Flask(__name__)

# Example model registry (extend as needed)
MODEL_REGISTRY = [
    {"display_name": "Gradio", "endpoint": "/gradio/", "type": "gradio"},
    {"display_name": "OpenAI", "endpoint": "/openai/", "type": "openai"},
    {"display_name": "Ollama", "endpoint": "/ollama/", "type": "ollama"},
    {"display_name": "LLM Studio", "endpoint": "/llmstudio/", "type": "llmstudio"},
]

# Scan for GGUF and PT models in a models/ directory
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
GGUF_EXT = '.gguf'
PT_EXT = '.pt'

def scan_local_models() -> List[Dict]:
    models = []
    if not os.path.exists(MODELS_DIR):
        return models
    for fname in os.listdir(MODELS_DIR):
        fpath = os.path.join(MODELS_DIR, fname)
        if fname.endswith(GGUF_EXT):
            models.append({
                "display_name": f"GGUF: {fname}",
                "endpoint": f"/gguf/{fname}",
                "type": "gguf"
            })
        elif fname.endswith(PT_EXT):
            models.append({
                "display_name": f"PyTorch: {fname}",
                "endpoint": f"/pt/{fname}",
                "type": "pt"
            })
    return models

@app.route('/api/models')
def get_models():
    models = MODEL_REGISTRY + scan_local_models()
    return jsonify(models)

# Example universal chat endpoint (stub)
@app.route('/api/chat', methods=['POST'])
def universal_chat():
    data = request.json
    model_type = data.get('model_type')
    prompt = data.get('prompt')
    # Route to the correct backend (stub logic)
    if model_type == 'openai':
        # Call OpenAI API
        return jsonify({"response": "[OpenAI response here]"})
    elif model_type == 'ollama':
        # Call Ollama API
        return jsonify({"response": "[Ollama response here]"})
    elif model_type == 'gguf':
        # Call local GGUF model (llama.cpp server)
        return jsonify({"response": "[GGUF model response here]"})
    elif model_type == 'pt':
        # Call local PyTorch model
        return jsonify({"response": "[PyTorch model response here]"})
    else:
        return jsonify({"response": "[Unknown model type]"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
