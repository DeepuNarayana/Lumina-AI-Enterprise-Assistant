# Lumina AI Backend Notes – Day 9
## Topic: SQLAlchemy + Alembic Migrations + Production Migration Strategy

---

# 1. Why Alembic?

FastAPI itself does not provide database migration support.

We use:

- FastAPI → Web Framework
- SQLAlchemy → ORM
- Alembic → Migration Tool
- PostgreSQL → Database

Architecture

FastAPI
        │
        ▼
SQLAlchemy ORM
        │
        ▼
Alembic
        │
        ▼
PostgreSQL

---

# 2. SQLAlchemy ORM

ORM (Object Relational Mapping)

Python Class

```python
class Sales(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    customer = Column(String)
    amount = Column(Float)
    region = Column(String)
```

represents

```sql
CREATE TABLE sales(
    id INTEGER PRIMARY KEY,
    customer VARCHAR,
    amount FLOAT,
    region VARCHAR
);
```

No SQL is written manually.

---

# 3. Base Class

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

Every ORM model inherits from Base.

```
               Base
                 │
        ┌────────┴────────┐
        │                 │
      User              Sales
```

Base collects metadata of all ORM models.

---

# 4. Base.metadata

Base.metadata stores metadata of every ORM model.

Alembic uses

```python
target_metadata = Base.metadata
```

to compare

```
Python Models

↓

Current Database Schema

↓

Generate Migration
```

---

# 5. __init__.py

Purpose

- Makes folder a Python package.
- Executes automatically when package is imported.
- Often used for registering models.

Example

```python
from app.models.user import User
from app.models.sales import Sales
```

Without importing Sales,
Alembic cannot detect it.

---

# 6. Alembic Folder Structure

```
backend/

│
├── alembic.ini

│
├── migrations/

        env.py
        script.py.mako
        versions/
```

The folder name may be

- migrations
- alembic

Both are valid.

---

# 7. env.py

Flow

```
Alembic Command

↓

env.py

↓

Load DATABASE_URL

↓

Load Base.metadata

↓

Compare Models

↓

Generate Migration
```

Important line

```python
target_metadata = Base.metadata
```

---

# 8. Migration Lifecycle

Step 1

Modify ORM Model

↓

Step 2

Generate Migration

```bash
alembic revision --autogenerate -m "create sales table"
```

Only generates Python migration.

Database remains unchanged.

↓

Step 3

Review Migration

Always review

```python
upgrade()

downgrade()
```

↓

Step 4

Apply Migration

```bash
alembic upgrade head
```

Now SQL executes against PostgreSQL.

---

# 9. Difference Between Commands

## revision

```bash
alembic revision --autogenerate
```

Creates migration file only.

Database NOT modified.

---

## upgrade

```bash
alembic upgrade head
```

Executes migration.

Updates PostgreSQL.

Updates alembic_version table.

---

## downgrade

```bash
alembic downgrade -1
```

Executes

```python
downgrade()
```

inside migration.

Rolls back schema changes.

---

## stamp

```bash
alembic stamp head
```

Does NOT execute SQL.

Only updates

```
alembic_version
```

Useful when database already contains schema but migration history is missing.

---

# 10. Why We Got

```
Target database is not up to date
```

Reason

Migration File

```
Users Migration
```

Database

```
No migration applied
```

Alembic prevents generating another migration until database reaches latest version.

---

# 11. Debugging Migration Issues

Check Current Migration

```bash
alembic current
```

Check Latest Migration

```bash
alembic heads
```

Check Applied Revision

```sql
SELECT * FROM alembic_version;
```

Check Existing Tables

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';
```

---

# 12. Repository Pattern

Architecture

```
Router

↓

ChatService

↓

PlannerAgent

↓

AgentFactory

↓

SQLAgent

↓

SalesRepository

↓

PostgreSQL
```

Repository is responsible only for database access.

Agents never access database directly.

---

# 13. Production Migration Strategy

Development

```
Create Migration

↓

Downgrade

↓

Modify Migration

↓

Upgrade
```

Allowed.

---

Production

Never modify old migration.

Instead

```
001 Users

002 Sales

003 Orders

004 Fix Users
```

Migration history remains immutable.

---

# 14. Why Not Modify Old Migration?

Suppose

Developer A

```
Migration 001
```

Developer B

```
Modified Migration 001
```

Production

```
Old Migration 001
```

Three different versions.

Chaos.

Industry Rule

Once migration is

- committed
- merged
- deployed

Never modify it.

Create a new migration.

---

# 15. Rollback in Production

Never immediately execute

```bash
alembic downgrade -1
```

First identify

- Application issue?
- Database issue?
- Infrastructure issue?

Rollback is used only after root cause analysis.

---

# 16. Forward Fix Strategy

Instead of

```
Version 2

↓

Downgrade

↓

Version 1
```

Industry prefers

```
Version 2

↓

Bug

↓

Version 3 (Fix)
```

This is called

**Forward Fix**

Used by

- Amazon
- Microsoft
- Google
- Netflix

---

# 17. Important Interview Answers

## Why Alembic?

Alembic provides version-controlled database schema migrations for SQLAlchemy applications.

---

## Difference between revision and upgrade?

revision

Creates migration scripts.

upgrade

Executes migration scripts.

---

## How does Alembic detect changes?

By comparing

```
Base.metadata

↓

Current Database Schema
```

---

## How to verify migration?

```bash
alembic current

alembic heads
```

```sql
SELECT * FROM alembic_version;
```

---

## Can we modify an existing migration?

Development

YES

Production

NO

Create a new migration instead.

---

## Will you use downgrade in production?

Not immediately.

First identify root cause.

If migration caused irreversible data loss,

prefer Forward Fix over rollback.

---

# 18. Biggest Learning

Database migration is NOT just executing commands.

It is

- Version Control
- Change History
- Production Safety
- Team Collaboration

---

# 19. Tech Lead Mindset

A Tech Lead never asks

> Which command should I execute?

A Tech Lead asks

- Why is this happening?
- What is the safest recovery?
- What will happen in Production?
- How will this affect other developers?
- Can this cause downtime?

This mindset is what separates a Senior Developer from a Tech Lead.

---