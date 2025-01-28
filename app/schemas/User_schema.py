from pydantic import BaseModel, ConfigDict, Field


class AuthUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str = Field(...)
    password: str = Field(..., min_length=6)