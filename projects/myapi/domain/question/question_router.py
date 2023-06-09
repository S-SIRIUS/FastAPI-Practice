from fastapi import APIRouter, Depends
from domain.question import question_crud, question_schema
from sqlalchemy.orm import Session
from database import get_db

router=APIRouter(
    prefix = "/api/question",
)

@router.get("/list", response_model=list[question_schema.Question])
def question_list(db:Session=Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question(question_id : int ,db:Session=Depends(get_db)):
    question = question_crud.get_question(db,question_id)
    return question