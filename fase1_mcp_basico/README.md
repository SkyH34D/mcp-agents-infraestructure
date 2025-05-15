# Infraestructura MCP - PoC (Prueba de Concepto)

Este repositorio contiene una prueba de concepto (PoC) para una arquitectura MCP (Multi-agent Control Plane) básica,
orientada a visualizar cómo se orquestan agentes de IA usando Python y FastAPI.

## Componentes

- **Agente Responder**: Usa un modelo LLM (como GPT-4) para responder preguntas.
- **Agente Transformer**: Transforma el texto (por ejemplo, invierte el contenido).
- **Servidor MCP (FastAPI)**: Punto central que recibe tareas, selecciona el agente y guarda resultados.
- **Base de Datos (SQLite)**: Guarda los logs de las tareas procesadas.

## Requisitos

```bash
pip install fastapi uvicorn openai pydantic sqlalchemy
```

## Uso

1. Ejecuta `uvicorn main:app --reload`
2. Accede a `http://localhost:8000/docs` para probar los endpoints

## Ejemplo de solicitud

```json
POST /run-task
{
  "agent": "responder",
  "input": "¿Qué es un agente en IA?"
}
```

---
Autor: Cristian "SkyH34D" Franco