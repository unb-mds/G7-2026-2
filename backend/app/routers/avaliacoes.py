from fastapi import APIRouter

from app.schemas.avaliacao import AvaliacaoRead

router = APIRouter(prefix="/avaliacoes", tags=["avaliacoes"])


@router.get("/", response_model=list[AvaliacaoRead])
def listar_avaliacoes() -> list[AvaliacaoRead]:
    # Pending Decision: a persistencia depende da escolha de ORM/banco de dados.
    # Enquanto isso, o endpoint responde uma lista vazia.
    # Ver skills/technology/fastapi/SKILL.md, secoes 13 e 15.
    return []
