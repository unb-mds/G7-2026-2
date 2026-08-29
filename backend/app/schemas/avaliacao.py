from pydantic import BaseModel, Field

# NOTA: os campos abaixo sao um placeholder de scaffold. Alinhar com o modelo
# de dados de "Avaliacao" acordado pela equipe antes de expor a API.


class AvaliacaoBase(BaseModel):
    disciplina: str = Field(..., description="Nome ou codigo da disciplina avaliada")
    professor: str = Field(..., description="Nome do professor avaliado")
    nota: int = Field(..., ge=1, le=5, description="Nota de 1 a 5")
    comentario: str | None = Field(default=None, max_length=2000)


class AvaliacaoCreate(AvaliacaoBase):
    pass


class AvaliacaoRead(AvaliacaoBase):
    id: int
