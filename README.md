# Webhook Tunnel

A minimal, open-source HTTP webhook tunnel service built with FastAPI.

This project allows you to create temporary webhook URLs that forward incoming HTTP requests to your specified `target_url`. Useful for testing, debugging, or capturing events from third-party services.

---

## Features

- 🔁 Forward any HTTP method (`GET`, `POST`, `PUT`, etc.)
- 🛣️ Supports nested paths: `/hook/{id}/path/to/resource`
- 📦 Request body and headers forwarding
- 🧠 TO DO: Stores all events for later inspection (optional)
- ⚡ Built with FastAPI + async SQLAlchemy

---

## Getting Started

### 🔧 Install Locally (Optional)

```bash
git clone https://github.com/hexkit/webhook-tunnel.git
cd webhook-tunnel
pip install -r requirements.txt
uvicorn src.main:app --reload
```

---

### 🐳 Run with Docker

> Make sure you have Docker installed: https://docs.docker.com/get-docker/

#### 🔹 Build the image:

```bash
docker build -t webhook-tunnel .
```

#### 🔹 Run the container:

```bash
docker run -p 8000:8000 webhook-tunnel
```

Then open:

```
http://localhost:8000/docs
```

---
## Usage

### Create a tunnel

```http
POST /tunnels
Content-Type: application/json

{
  "target_url": "https://your.domain.com/webhook"
}
```

### Forward incoming request

```http
POST /hook/{tunnel_id}/some/path
```

This will forward the request to:

```
{target_url}/some/path
```

with original headers, body, and method.

---

## Example

```bash
curl -X POST http://localhost:8000/hook/abc123/notify -d '{"event": "test"}'
```

---

## Development

- Python 3.10+
- FastAPI
- SQLAlchemy (async)
- httpx

---

## Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

---

## License

MIT License

---

## Credits

Built with ❤️ using FastAPI and a focus on developer experience.
