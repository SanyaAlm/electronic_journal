from datetime import datetime

from sqlalchemy import Integer, String, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.db_connection import Base


class Students(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(length=250), nullable=False,)
    email: Mapped[str] = mapped_column(String(length=250), unique=True, nullable=False, )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class Score(Base):
    __tablename__ = 'score'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    grade: Mapped[int] = mapped_column(Integer, CheckConstraint('grade >= 1 AND grade <= 10'))
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
