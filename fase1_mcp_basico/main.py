from fastapi import FastAPI
from pydantic import BaseModel
from agents import responder, transformer
from db.models import SessionLocal, Task

app = FastAPI()

class TaskInput(BaseModel):
    agent: str
    input: str

@app.post("/run-task")
def run_task(data: TaskInput):
    input_text = data.input
    agent = data.agent.lower()
    
    if agent == "responder":
        output = responder.responder_agent(input_text)
    elif agent == "transformer":
        output = transformer.transformer_agent(input_text)
    else:
        return {"error": "Agente no válido"}

    db = SessionLocal()
    task = Task(input=input_text, output=output, agent=agent)
    db.add(task)
    db.commit()
    db.close()

    return {"output": output}