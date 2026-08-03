from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from app.auth.dependencies import get_current_user
from fastapi import APIRouter, UploadFile, File
from app.services.document_service import DocumentService
from app.db.dependencies import get_db

router=APIRouter(
    prefix="/documents",
    tags=["Documents"]
)
#document_service=DocumentService()

@router.post("/upload")
async def upload_document(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user),
    file: UploadFile=File(...)
):
    print(current_user)
    document_service = DocumentService(db)

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())

    uploaded= document_service.upload_document(
        local_file=temp_file,
        object_key=f"documents/{file.filename}",
        owner_id=current_user["user_id"]
    )
    return {
        "uploaded":True,
        "document_id": uploaded.id,
        "filename":uploaded.filename,
        "s3_key": uploaded.s3_key
    }

@router.get("/")
async def lsit_documents(
    db: Session = Depends(get_db),
    current_user= Depends(get_current_user)
):
    document_service = DocumentService(db)

    documents= document_service.get_all_documents(
        owner_id= get_current_user["user_id"]
    )

    return documents

@router.get("/{document_id}/download")
async def download_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    document_service = DocumentService(db)

    url = document_service.download_document(document_id)

    if not url:
        raise HTTPException(
            status_code = 404,
            detail="Document not found"
        )
    return {
        "download url": url
    }

@router.delete("/{document_id}")
async def delete_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    document_service = DocumentService(db)

    deleted = document_service.delete_document(document_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "message": "Document Deleted successfully"
    }

