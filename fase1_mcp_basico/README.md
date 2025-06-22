# Fase 1 – MCP Básico con Cliente Explícito

Este directorio contiene la **Prueba de Concepto (PoC)** de la **Fase 1** de la Infraestructura MCP. Aquí aprenderás a montar un servidor MCP mínimo con FastAPI y dos agentes simples, usando un cliente explícito de OpenAI.

---

## 📁 Estructura del directorio

```plaintext
fase1_mcp_basico/
├── main.py               # Servidor MCP (FastAPI)
├── agents/
│   ├── responder.py      # Agente que usa cliente explícito de OpenAI para chat completions
│   └── transformer.py    # Agente que aplica una transformación al texto
├── db/
│   └── models.py         # Definición de la tabla Task en SQLite
├── .env                  # Variables de entorno (OPENAI_API_KEY)
└── requirements.txt      # Dependencias del proyecto
```

---

## 🔎 Componentes clave

- **Cliente explícito de OpenAI**: configurado en `agents/responder.py` para centralizar clave, timeout y opciones.
- **Agente Responder**: genera respuestas con GPT-4 utilizando `client.chat.completions.create`.
- **Agente Transformer**: invierte la cadena de texto recibida.
- **Servidor FastAPI**: expone `/run-task`, recibe `agent` e `input`, delega al agente y guarda el resultado en SQLite.
- **SQLite**: base de datos ligera (`tasks.db`) para registrar cada tarea (input, output, agente).

---

## 🛠️ Requisitos

```bash
python3 -m venv mcp-env           # (opcional pero recomendado)
source mcp-env/bin/activate
pip install -r requirements.txt
```

**requirements.txt**:

```text
fastapi
uvicorn
openai
python-dotenv
pydantic
sqlalchemy
```

---

## 🔐 Configurar la API Key de OpenAI

1. Crea un archivo `.env` en este directorio con:
   ```ini
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
2. Añade `.env` a tu `.gitignore` para no subir tu clave.

El cliente de OpenAI en `agents/responder.py` carga esta variable automáticamente con `python-dotenv`.

---

## ▶️ Ejecutar la PoC

```bash
uvicorn main:app --reload
```

Accede a `http://localhost:8000/docs` para probar el endpoint **POST /run-task**.

---

> Con esta configuración, tienes un MCP básico listo para evolucionar en las siguientes fases.
