# llm-proxy--ollama-openai-bridge
llm-proxy | ollama-openai-bridge 


[DE] Ein OpenAI-kompatibler Middleware-Proxy für lokale LLM-Infrastrukturen.

[EN] An OpenAI-compatible middleware proxy for local LLM infrastructures.

⚡ Quick Start / Schnelleinrichtung (venv)

[DE] Um Konflikte mit Ihrem System-Python zu vermeiden, nutzen wir eine isolierte Umgebung:

[EN] To avoid conflicts with your system Python, we use an isolated environment:
Bash

# 1. Create environment / Umgebung erstellen
python3 -m venv venv

# 2. Activate / Aktivieren
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate # Windows

# 3. Install dependencies / Abhängigkeiten installieren
pip install flask requests

# 4. Start / Starten
python llm_proxy.py

📖 Description / Beschreibung

[DE] Dieser Proxy fungiert als Brücke zwischen Anwendungen, die eine OpenAI-API erwarten, und lokalen Backends wie Ollama.

    Modell-Erzwingung: Leitet alle Anfragen auf ein definiertes lokales Modell um.

    Netzwerk-Abstraktion: Das Backend kann auf jedem Server im LAN/VPN laufen.

    Stabilitäts-Delay: Ein kurzer Delay hilft Agent-Systemen (wie Browser-Automation), stabil zu laufen.

[EN] This proxy acts as a bridge between applications expecting an OpenAI API and local backends like Ollama.

    Model Enforcement: Redirects all requests to a defined local model.

    Network Abstraction: The backend can run on any server within your LAN/VPN.

    Stability Delay: A short delay helps agent systems (like browser automation) run more reliably.

    
