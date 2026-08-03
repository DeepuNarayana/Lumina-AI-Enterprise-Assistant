# Day 04 - Document Module CRUD (FastAPI + PostgreSQL + AWS S3)

## Objective

Implemented a complete Document CRUD module using:

- FastAPI
- PostgreSQL
- SQLAlchemy
- AWS S3 (boto3)
- Repository Pattern
- Service Layer

---

# What We Built

```
Client
      │
      ▼
FastAPI Router
      │
      ▼
Document Service
      │
      ├─────────────► S3 Client
      │                  │
      │                  ▼
      │               AWS S3
      │
      ▼
Document Repository
      │
      ▼
PostgreSQL
```

---

# Folder Structure

```
app/
│
├── api/
│     document_api.py
│
├── services/
│     document_service.py
│
├── repositories/
│     document_repository.py
│
├── aws/
│     s3_client.py
│
├── models/
│     document.py
│
├── db/
│     session.py
│     dependencies.py
│
└── database/
      base.py
```

---

# APIs Implemented

## 1 Upload Document

```
POST /documents/upload
```

Flow

```
Upload File
      │
      ▼
Save Temp File
      │
      ▼
Upload To S3
      │
      ▼
Save Metadata To PostgreSQL
      │
      ▼
Return Response
```

Response

```json
{
  "uploaded": true,
  "document_id": 1,
  "filename": "sample.txt",
  "s3_key": "documents/sample.txt"
}
```

---

## 2 List Documents

```
GET /documents
```

Flow

```
Client

↓

Repository

↓

SELECT * FROM documents

↓

Return JSON
```

Response

```json
[
  {
    "id": 1,
    "filename": "sample.txt",
    "s3_key": "documents/sample.txt"
  }
]
```

---

## 3 Download Document

```
GET /documents/{id}/download
```

Flow

```
Client

↓

Repository

↓

Find S3 Key

↓

Generate Pre-signed URL

↓

Return URL
```

Response

```json
{
  "download_url": "https://...."
}
```

---

## 4 Delete Document

```
DELETE /documents/{id}
```

Flow

```
Find Document

↓

Delete File From S3

↓

Delete Row From PostgreSQL

↓

Return Success
```

Response

```json
{
  "message": "Document deleted successfully"
}
```

---

# Database

Table

```
documents
```

Columns

```
id

filename

s3_key
```

Model

```python
class Document(Base):

    __tablename__ = "documents"

    id

    filename

    s3_key
```

---

# Repository Layer

Methods

```
create()

get_all()

get_by_id()

delete()
```

Repository only talks to Database.

No business logic.

---

# Service Layer

Methods

```
upload_document()

list_documents()

download_document()

delete_document()
```

Service coordinates:

- Repository
- AWS S3

Business logic stays here.

---

# S3 Client Methods

Implemented

```
upload_document()

generate_download_url()

delete_document()
```

---

# DB Session

Created

```
app/db/session.py
```

Purpose

- Creates SQLAlchemy Engine
- SessionLocal
- Database Connection

---

Created

```
app/db/dependencies.py
```

Purpose

Dependency Injection

```
yield db

↓

Automatically closes connection
```

---

# Alembic Learning

Big learning today.

Initially

Migration generated

BUT

```
upgrade()

pass
```

No SQL generated.

Reason

Document model wasn't imported.

Correct

```
models/__init__.py

↓

from .document import Document
```

AND

```
env.py

↓

from app.models import User, Sales, Document
```

Only then

```
target_metadata
```

contains Document table.

Lesson

Always open migration file.

Never blindly run

```
alembic upgrade head
```

Check if migration actually contains

```
op.create_table(...)
```

---

# Issues Fixed Today

## Issue 1

```
NameError

document_service not defined
```

Solution

Create DocumentService inside API using Dependency Injection.

---

## Issue 2

```
DocumentService()

missing db parameter
```

Solution

```
db = Depends(get_db)

↓

DocumentService(db)
```

---

## Issue 3

```
S3Client.upload_document()

missing self
```

Reason

Using class instead of object.

Correct

```
self.s3 = S3Client()
```

---

## Issue 4

```
AWS_REGION not found
```

Reason

Missing field in Settings.

Added

```
AWS_REGION

S3_BUCKET_NAME
```

---

## Issue 5

```
upload_file()

unexpected keyword FileName
```

Correct Parameter

```
Filename
```

NOT

```
FileName
```

---

## Issue 6

```
generate_url()

doesn't exist
```

Correct

```
generate_presigned_url()
```

---

## Issue 7

```
Can't locate revision
```

Reason

Broken Alembic migration history.

Solution

Removed invalid migration.

Created new migration.

---

# Architecture Learned

```
API

↓

Service

↓

Repository

↓

Database
```

AWS

```
API

↓

Service

↓

S3 Client

↓

AWS S3
```

---

# Senior Interview Notes

## Why Repository Pattern?

Separates Database logic from Business logic.

---

## Why Service Layer?

Keeps business logic centralized.

Repository stays clean.

---

## Why Dependency Injection?

Avoids global objects.

Each request gets its own DB Session.

---

## Why Delete S3 First?

If DB deleted first

and S3 deletion fails

↓

Orphan File

If S3 deleted first

↓

Database deleted

↓

Both remain consistent.

---

## Why Store Metadata?

Instead of querying S3 every time

Store

```
filename

s3_key

created_at

owner
```

inside Database.

Faster.

---

# Current Project Status

```
Authentication

⬜

User CRUD

✅

Sales CRUD

✅

Document Upload

✅

Document List

✅

Document Download

✅

Document Delete

✅

AWS S3 Integration

✅

Alembic Migrations

✅
```

---

# Next Module

JWT Authentication

Topics

- bcrypt
- JWT Token
- Login API
- Protect Routes
- Refresh Tokens
- Authorization

This is the next major milestone.