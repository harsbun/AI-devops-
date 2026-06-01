# AI DevOps Assistant

An AI-powered REST API that generates DevOps artifacts—Dockerfiles, Kubernetes manifests, and Terraform configurations—from natural-language prompts.

Built with [FastAPI](https://fastapi.tiangolo.com/) and the [Groq API](https://console.groq.com/) (Llama 3.3 70B).

## Features

| Endpoint       | Description                                      |
|----------------|--------------------------------------------------|
| `GET /`        | Health check                                     |
| `GET /docker`  | Generate a Dockerfile from a prompt              |
| `GET /k8s`     | Generate Kubernetes YAML from a prompt           |
| `GET /terraform` | Generate Terraform code from a prompt          |

## AI Tools Used in Development

This project was designed and built with help from multiple AI assistants:

| Tool | Role |
|------|------|
| **OpenAI Codex** | Code generation, scaffolding, and API structure |
| **Claude (Anthropic)** | Architecture review, prompt design, and refactoring |
| **Google Gemini AI** | Documentation, alternative implementations, and testing ideas |
| **Cursor** | IDE-integrated development and iteration |

## APIs & Integrations

| API / SDK | Purpose |
|-----------|---------|
| **Groq API** | Runtime LLM inference (`llama-3.3-70b-versatile`) for `/docker`, `/k8s`, and `/terraform` |
| **Google Generative AI** | Gemini SDK available for extended AI workflows (`google-generativeai`) |
| **FastAPI** | Web framework and OpenAPI docs |
| **python-dotenv** | Secure loading of API keys from environment variables |

## Prerequisites

- Python 3.12+
- [Groq API key](https://console.groq.com/keys)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/harsbun/AI-devops-.git
   cd AI-devops-
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install groq
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Optional (for Gemini integrations):

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

   API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Usage Examples

**Generate a Dockerfile**

```bash
curl "http://127.0.0.1:8000/docker?prompt=Python%20Flask%20app%20on%20port%205000"
```

**Generate Kubernetes YAML**

```bash
curl "http://127.0.0.1:8000/k8s?prompt=Deploy%20nginx%20with%202%20replicas"
```

**Generate Terraform**

```bash
curl "http://127.0.0.1:8000/terraform?prompt=AWS%20EC2%20instance%20with%20security%20group"
```

## Project Structure

```
AI-devops-/
├── main.py           # FastAPI app and DevOps endpoints
├── test.py           # Groq API connectivity test
├── requirements.txt  # Python dependencies
├── .env              # API keys (not committed)
└── README.md
```

## Security

- Never commit `.env` or API keys to version control.
- Rotate keys if they are exposed.

## License

MIT

## Author

[harsbun](https://github.com/harsbun)
