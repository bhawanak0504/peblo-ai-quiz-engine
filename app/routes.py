
from fastapi import APIRouter, UploadFile
from sqlalchemy.orm import Session
from .ingestion import extract_text, chunk_text
from .quiz_generator import generate_questions
from .database import SessionLocal
from .models import Chunk, Question

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile):

    path = f"data/{file.filename}"

    with open(path,"wb") as f:
        f.write(await file.read())

    text = extract_text(path)
    chunks = chunk_text(text)

    db: Session = SessionLocal()

    for c in chunks:
        chunk = Chunk(text=c, topic="general")
        db.add(chunk)

    db.commit()

    return {"chunks_created": len(chunks)}


@router.post("/generate-quiz")
def generate_quiz():

    db: Session = SessionLocal()
    chunks = db.query(Chunk).all()

    questions = []

    for chunk in chunks:
        q = generate_questions(chunk.text)
        questions.append(q)

    return {"generated": questions}


@router.get("/quiz")
def get_quiz():

    db: Session = SessionLocal()
    q = db.query(Question).all()

    return q


@router.post("/submit-answer")
def submit_answer(data: dict):

    return {"status":"received"}
