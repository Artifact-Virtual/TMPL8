# TMPL8 UI (Universal LLM Adapter)

A universal, device-friendly chat interface for any LLM backend: OpenAI, Ollama, Gradio, LLM Studio, GGUF (llama.cpp), PyTorch (.pt), and more. This project aims to simplify interaction with large language models (LLMs) by providing a unified interface that is easy to use, extend, and deploy.

---

## Features

- **Modern, Responsive HTML UI**  
    Works seamlessly across desktop, tablet, and mobile devices.
    
- **Dynamic Model Selector**  
    Automatically discovers and lists available local and remote models.
    
- **Universal Backend Adapter**  
    Built with Flask, enabling easy integration with various LLM backends.
    
- **Plug-and-Play**  
    Simply drop your GGUF or `.pt` models into the `models/` folder to get started.
    
- **No Vendor Lock-In**  
    Compatible with any LLM backend, and extensible to support custom backends.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-orange)
![HTML](https://img.shields.io/badge/HTML-Responsive-red)

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask (`pip install flask`)
- Supported LLM models (e.g., GGUF, PyTorch `.pt`)

---

## Quick Start

Follow these steps to set up and run TMPL8 UI:

### 1. **Install Python Dependencies**
Run the following command to install Flask:
```powershell
pip install flask
```

### 2. **(Optional) Add Local Models**
Place your `.gguf` or `.pt` models in the `models/` directory. Create the directory if it does not exist.

### 3. **Run the Backend**
Start the Flask backend by running:
```powershell
python universal_adapter_backend.py
```

### 4. **Open the Chat UI**
Open `chat.html` in your browser, or serve it using any static file server.

---

## File Structure

The project is organized as follows:

```
templates/
├── chat.html                  # Main chat UI (device-friendly)
├── universal_adapter_backend.py # Flask backend for model registry and chat
├── README.md                  # Documentation file
models/
        ├── your-model.gguf        # GGUF models (llama.cpp, etc.)
        └── your-model.pt          # PyTorch models
```

---

## Extending the Project

### Adding New Backends
To integrate a new LLM backend:
1. Open `universal_adapter_backend.py`.
2. Add a new adapter function to handle the backend's API or model format.
3. Ensure the new backend is registered in the `/api/models` endpoint.

### Frontend Auto-Population
The frontend dynamically fetches available models from the `/api/models` endpoint. No additional configuration is required for the UI to display new models.

---

## Contributing

We welcome contributions to improve TMPL8 UI. To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Support

For issues, questions, or feature requests, please open an issue in the repository or contact the maintainers directly.

---

## Acknowledgments

Special thanks to the open-source community for providing tools and resources that make projects like this possible.

---
