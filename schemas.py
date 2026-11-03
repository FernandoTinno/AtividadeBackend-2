from pydantic import BaseModel, ConfigDict

#mesmo intuito do arquivo que antes era pydanticmodel.py
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    # Configuração necessária no Pydantic para ler dados do SQLAlchemy
    model_config = ConfigDict(from_attributes=True)