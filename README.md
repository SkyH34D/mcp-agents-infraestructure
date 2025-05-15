# 🧠 Infraestructura MCP con Agentes Inteligentes – De Cero a Experto

Este repositorio es una guía práctica y progresiva para construir una **infraestructura de agentes autónomos** orquestada mediante una arquitectura **MCP**.

A lo largo de varias fases, se diseñarán, construirán y escalarán sistemas multiagente con **Python, FastAPI, LLMs y otras herramientas**.

---

## 📘 Índice de Fases

1. [🔹 Fase 1 – MCP Básico](./fase1_mcp_basico/)
2. [🔹 Fase 2 – Agentes Orquestados](./fase2_agentes_orquestados/)
3. 🔜 Fase 3 – MCP Avanzado *(próximamente)*
4. 🔜 Fase 4 – Multiagente Aplicado *(próximamente)*

---

## 🚀 Objetivos del proyecto

- Comprender los fundamentos de los agentes y su orquestación
- Desarrollar agentes especializados y reutilizables
- Diseñar un servidor MCP que coordine tareas entre agentes
- Integrar memoria, herramientas externas y razonamiento
- Desplegar una arquitectura realista de agentes colaborativos

---

## 🧩 Estructura del proyecto

### [`fase1_mcp_basico/`](./fase1_mcp_basico/)
- MCP mínimo con FastAPI
- Agentes simples (`responder` y `transformer`)
- Registro de tareas en SQLite

### [`fase2_agentes_orquestados/`](./fase2_agentes_orquestados/)
- Agentes especializados en tareas (scraping, análisis, respuesta)
- Orquestación centralizada
- Comunicación básica entre agentes (A2A)
- Integración con APIs externas

---

## 🛠️ Requisitos técnicos

- Python 3.9+
- FastAPI, Uvicorn
- OpenAI API key (o similar)
- SQLAlchemy, SQLite
- [Otros requisitos específicos por fase se detallan en cada carpeta]

---

## 📚 ¿Quién debería usar este repositorio?

Este proyecto está diseñado para:

- Estudiantes y autodidactas de IA generativa
- Profesionales que quieran aprender arquitectura de agentes
- Desarrolladores que busquen construir flujos inteligentes con LLMs
- Personas que deseen experimentar con control MCP y agentes distribuidos

---

## ⚙️ Cómo empezar

```bash
cd fase1_mcp_basico
pip install -r requirements.txt
uvicorn main:app --reload
```

Visita [http://localhost:8000/docs](http://localhost:8000/docs) para probar la API interactiva.

---

## 📄 Licencia

MIT License. Eres libre de usar, modificar y extender este proyecto para tus propios fines.

---

## ✍️ Autor


**Cristian "SkyH34D" Franco**  
Offensive Security | Pentester | Red Team | IA Enthusiast | Agents & MCP Servers | CEH v13
