# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User, PartnerApplication
from app.schemas import (
    UserCreate, UserOut,
    PartnerApplicationCreate, PartnerApplicationOut,
)

# ✅ IMPORTANT: no prefix here
router = APIRouter()

# ---------- health / ping ----------
@router.get("/ping", tags=["Health"])
def ping():
    return {"pong": True}

# ---------- users ----------
@router.post(
    "/users",
    response_model=UserOut,
    tags=["Users"],
)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    # unique email check
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(**payload.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# ---------- partner applications ----------
@router.post(
    "/partners/applications",
    response_model=PartnerApplicationOut,
    tags=["Partner Applications"],
)
def create_partner_application(payload: PartnerApplicationCreate, db: Session = Depends(get_db)):
    rec = PartnerApplication(**payload.model_dump())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec
