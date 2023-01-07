from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate date while creating a job
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


# this will be used to format the response to not have id, owner_id etc...
class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config:  # to convert non dict object to json
        orm_mode = True