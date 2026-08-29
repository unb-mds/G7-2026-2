from fastapi import FastAPI

from app.routers import avaliacoes

app = FastAPI(title="G7 - Avaliação de Disciplinas")

app.include_router(avaliacoes.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
