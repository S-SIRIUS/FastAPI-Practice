from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from domain.question import question_crud,question_schema
router = APIRouter(
    prefix = "/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db:Session=Depends(get_db)):
    __question_list = question_crud.get_question_list(db)
    return __question_list
