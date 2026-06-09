from pydantic import BaseModel, field_validator


class Task(BaseModel):
    id: str
    title: str

    @field_validator("title")
    def clean_spaces(cls, v: str) -> str:
        cleaned = " ".join(v.split())

        if not cleaned:
            raise ValueError("Title is empty")

        return cleaned
