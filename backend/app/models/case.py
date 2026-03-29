from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.core.database import Base


class Case(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    case_id: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    parent_case_id: Mapped[str | None] = mapped_column(String(50), nullable=True)
    case_title: Mapped[str] = mapped_column(String(255), nullable=False)
    customer_name: Mapped[str] = mapped_column(String(255), nullable=False)
    segment: Mapped[str | None] = mapped_column(String(100), nullable=True)
    application: Mapped[str | None] = mapped_column(String(255), nullable=True)
    case_type: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="New Intake")
    priority: Mapped[str] = mapped_column(String(20), nullable=False, default="Medium")
    strategy_version: Mapped[str] = mapped_column(String(50), nullable=False)
    notes_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
