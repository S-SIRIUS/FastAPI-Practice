from pydantic import BaseModel
import datetime
class Question(BaseModel):
    id : int
    subject : str
    content : str
    create_date : datetime.datetime

    class Config:
        orm_mode = True