from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Company, status_code=status.HTTP_201_CREATED)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    """
    Register a new company.
    """
    # You might want to add logic here to check for duplicate companies
    # before creating.
    db_company = crud.create_company(db=db, company=company)
    return db_company

# You can add other endpoints for GET, PUT, DELETE company operations here later
# @router.get("/{company_id}", response_model=schemas.Company)
# def read_company(company_id: int, db: Session = Depends(get_db)):
#     db_company = crud.get_company(db=db, company_id=company_id)
#     if db_company is None:
#         raise HTTPException(status_code=404, detail="Company not found")
#     return db_company