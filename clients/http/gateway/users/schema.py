from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    User data structure.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')  
    first_name: str = Field(alias='firstName')  
    middle_name: str = Field(alias='middleName')  
    phone_number: str = Field(alias='phoneNumber')  


class GetUserResponseSchema(BaseModel):
    """
    Get user data structure response.
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Data structure to create a new user.
    """
    # populate_by_name=True allows us **to pass** params to the model in snake_case when we create it
    # to dump it properly and send to the server in expected format, use model_dump(by_alias=True)
    model_config = ConfigDict(populate_by_name=True)

    # alias from `Field` will be applied to data which is incoming from some source to validate it against Pydantic model
    email: EmailStr
    last_name: str = Field(alias='lastName')  
    first_name: str = Field(alias='firstName')  
    middle_name: str = Field(alias='middleName')  
    phone_number: str = Field(alias='phoneNumber')  


class CreateUserResponseSchema(BaseModel):
    """
    Create user data structure response.
    """
    user: UserSchema
