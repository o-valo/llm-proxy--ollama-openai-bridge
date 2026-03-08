import os
import time
import requests
from flask import Flask, request, Response, jsonify

VERSION = "1.2.9-stable"
app = Flask(__name__)

# --- CONFIGURATION / KONFIGURATION ---

# [EN] Backend URL (e.g., Ollama). Can be a network IP (10.x.x.x) or 127.0.0.1.
# [DE] URL zum Backend (z.B. Ollama). Kann eine Netzwerk-IP oder localhost sein.
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://10.0.0.1:11434")

# [EN] Model Configuration: Set your preferred model here. 
# [DE] Modell-Konfiguration: Tragen Sie hier Ihr bevorzugtes Modell ein. 
# Recommendation/Empfehlung: Qwen 3.5
SELECTED_MODEL = os.getenv("MODEL_NAME", "qwen3.5:9b-q8_0")

# Proxy Port
PORT = int(os.getenv("PROXY_PORT", 11435))

@app.route('/v1/chat/completions', methods=['POST'])
@app.route('/chat/completions', methods=['POST'])
def proxy_completions():
    try:
        data = request.get_json()
        data["model"] = SELECTED_MODEL
        
        # Stability Delay for Agents / Stabilitäts-Pause
        time.sleep(0.5)
        
        print(f"[{VERSION}] Routing request to {SELECTED_MODEL} via {OLLAMA_URL}...")

        is_streaming = data.get("stream", False)

        resp = requests.post(
            f"{OLLAMA_URL}/v1/chat/completions",
            json=data,
            timeout=180,
            headers={"Content-Type": "application/json"},
            stream=is_streaming
        )

        if is_streaming:
            return Response(
                resp.iter_content(chunk_size=1024), 
                content_type=resp.headers.get('Content-Type', 'text/event-stream')
            )
        
        return Response(resp.content, resp.status_code, dict(resp.headers))

    except Exception as e:
        print(f"[{VERSION}] Error/Fehler: {str(e)}")
        return jsonify({"error": str(e), "v": VERSION}), 500

@app.route('/v1/models', methods=['GET'])
def list_models():
    return jsonify({
        "object": "list",
        "data": [{
            "id": SELECTED_MODEL,
            "object": "model",
            "created": int(time.time()),
            "owned_by": "llm-proxy"
        }]
    })

if __name__ == '__main__':
    print(f"--- LLM Proxy | Ollama-Bridge {VERSION} active ---")
    print(f"Target/Ziel: {OLLAMA_URL}")
    print(f"Model/Modell: {SELECTED_MODEL}")
    app.run(host='0.0.0.0', port=PORT)

# EOF
