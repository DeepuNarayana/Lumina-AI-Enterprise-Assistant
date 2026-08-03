from app.aws.s3_client import S3Client
from sqlalchemy.orm import Session
from app.repositories.document_repository import DocumentRepository


class DocumentService:

    def __init__(self, db: Session):
        self.s3 = S3Client()
        self.repository = DocumentRepository(db)

    def upload_document(
        self,
        local_file: str,
        object_key: str,
        owner_id
    ):

        uploaded = self.s3.upload_document(

            local_file=local_file,
            object_key=object_key
        )

        if not uploaded:

            return None

        filename = object_key.split("/")[-1]

        document = self.repository.create(
            filename=filename,
            s3_key=object_key,
            owner_id=owner_id
        )

        return document

    def get_all_documents(self, owner_id: int):
        return self.repository.get_all_by_owner(owner_id)

    def download_document(
        self,
        document_id: int
    ):
        document = self.repository.get_by_id(document_id)

        if not document:
            return None

        url = self.s3.generate_download_url(
            object_key=document.s3_key
        )

        return url

    def delete_document(
        self,
        document_id: int
    ):
        document = self.repository.get_by_id(document_id)

        if not document:
            return False

        deleted = self.s3.delete_document(
            object_key = document.s3_key
        )
        if not deleted:
            return False

        self.repository.delete(document)
        return True