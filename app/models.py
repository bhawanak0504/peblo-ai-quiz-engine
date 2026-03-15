
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    subject = Column(String)
    grade = Column(Integer)

class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey("sources.id"))
    text = Column(Text)
    topic = Column(String)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    type = Column(String)
    options = Column(Text)
    answer = Column(String)
    difficulty = Column(String)
    source_chunk_id = Column(Integer)

class StudentAnswer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    student_id = Column(String)
    question_id = Column(Integer)
    selected_answer = Column(String)
    is_correct = Column(String)
