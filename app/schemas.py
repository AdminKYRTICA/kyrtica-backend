# app/schemas.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# -------- Users --------
class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

# --- Partner Applications ---
class PartnerApplicationCreate(BaseModel):
    user_id: int
    business_name: str = Field(min_length=1)
    kind: str = Field(min_length=1)  # e.g., 'proprietor' | 'partner' | 'llp' | 'pvt_ltd' | 'public_ltd'

class PartnerApplicationOut(BaseModel):
    id: int
    user_id: int
    business_name: str
    kind: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
