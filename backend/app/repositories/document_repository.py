from sqlalchemy.orm import Session
from app.models.document import Document
from uuid import UUID

class DocumentRepository:
    def __init__(self, db:Session):
        self.db=db

    def create(
        self,
        filename: str,
        s3_key: str,
        owner_id: UUID
    )-> Document:

        document= Document(
            filename=filename,
            s3_key=s3_key,
            owner_id=owner_id
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_all_by_owner(self, owner_id: int):
        return (
            self.db.query(Document)
            .filter(Document.owner_id ==owner_id)
            .all()
        )

    def get_by_id(self, document_id: int):
        return(
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def delete(self, document):
        self.db.delete(document)
        self.db.commit()


