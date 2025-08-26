from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    department: str
    salary: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
