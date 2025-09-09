from uuid import uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default='user@example.com')
    last_name: str = Field(default='Smith')
    first_name: str = Field(default='Tom')
    middle_name: str = Field(default='B.')
    phone_number: str = Field(default='123-456-78-90')


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
