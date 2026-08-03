# Lumina AI Enterprise Assistant - Progress Document

## Date
28 July 2026

---

# Objective

Build an enterprise-grade AI Assistant using:

- FastAPI
- PostgreSQL
- LangChain
- LangGraph
- AWS Bedrock
- React
- Planner Agent
- Factory Pattern
- Multiple AI Agents

The goal is to understand every component deeply rather than copying code.

---

# Completed Architecture

```text
Frontend (React)

        │

        ▼

POST /ai/chat

        │

        ▼

FastAPI Router

        │

        ▼

ChatService

        │

        ▼

PlannerAgent

        │

        ▼

AgentFactory

        │

        ▼

SQLAgent

        │

        ▼

Response

        │

        ▼

React
```

---

# Folder Structure

```text
backend/

│

├── app/

│   ├── main.py

│   ├── services/

│   │      chat_service.py

│

├── ai/

│   ├── router.py

│   ├── schemas.py

│   ├── factory/

│   │      agent_factory.py

│   ├── agents/

│   │      planner.py

│   │      sql_agent.py

│
├── main.py
```

---

# Components Implemented

## 1. Planner Agent

Planner analyzes user intent.

Example:

```
User

↓

"What is today's sales?"
```

Planner returns

```python
Intent(
    agent="sql",
    confidence=0.98,
    reason="Structured business data"
)
```

Planner never executes business logic.

It only decides:

> Which Agent should process the request?

---

## 2. Factory Pattern

Factory decides which Agent object to return.

Current implementation:

```python
SQLAgent

RAGAgent (future)

LLMAgent (future)
```

Factory completely hides object creation from ChatService.

---

## 3. SQLAgent

Implemented

```python
execute(message)
```

Current response:

```python
{
    "agent":"sql",
    "response":"SQL Agent processed your request..."
}
```

Later this will execute actual SQL queries.

---

## 4. ChatService

Responsibilities

- Receive request
- Call Planner
- Receive Intent
- Call Factory
- Receive Agent
- Execute Agent
- Return response

ChatService never knows whether it is talking to:

- SQLAgent
- RAGAgent
- LLMAgent

This follows the Open Closed Principle.

---

## 5. FastAPI Router

Current endpoint

```
POST /ai/chat
```

Request

```json
{
    "message":"Show sales report"
}
```

Current Response

```json
{
    "response":"SQL Agent processed your request: show sales report"
}
```

---

# Concepts Learned

## Object Creation vs Method Calling

Object Creation

```python
chat_service = ChatService()
```

Runs only once.

Method Calling

```python
chat_service.process()
```

Runs every request.

Important Interview Question:

__init__()

runs only when object is instantiated.

---

## Factory Pattern

Factory answers

```
Which object should be returned?
```

Not

```
When to create?
```

Not

```
Who gives object?
```

---

## Object Lifecycle

Answers

```
When should object be created?
```

---

## Dependency Injection

Answers

```
Who should provide the object?
```

(Currently not implemented.
Will be implemented later using FastAPI Depends.)

---

## Singleton

Answers

```
Should only one object exist?
```

(Current implementation behaves similarly because ChatService is created once during application startup.)

---

## Heap Memory

Objects live inside

```
RAM (Heap Memory)
```

Variables store references.

Example

```python
chat_service

↓

Heap Memory

↓

ChatService Object
```

---

## API Request Models

Instead of

```python
message: str
```

we use

```python
ChatRequest(BaseModel)
```

Advantages

- Automatic Validation
- Swagger Documentation
- Strong API Contract
- Easily Extendable
- Cleaner Endpoint

---

## FastAPI Serialization

SQLAgent returns

Python Dictionary

FastAPI automatically converts

↓

JSON

before sending to frontend.

---

# Design Patterns Covered

✅ Factory Pattern

Understood deeply.

Purpose:

Hide object creation and return the correct implementation.

---

# Interview Answers Learned

## Why Factory Pattern?

Factory removes direct dependency on concrete classes.

Adding a new Agent never changes ChatService.

---

## Why ChatRequest?

To provide a clean API contract, automatic validation, scalability, and documentation.

---

## Why create ChatService outside endpoint?

Objects are initialized once during application startup.

Every request reuses the same object.

Avoids unnecessary initialization.

---

## Difference between Object Creation and Method Calling

Object Creation

```python
ChatService()
```

Method Calling

```python
chat_service.process()
```

Object is created once.

Method is called many times.

---

# Current Status

Completed

- Planner
- Factory
- SQLAgent
- ChatService
- FastAPI Router
- End-to-End Pipeline

Successfully tested

```
React

↓

FastAPI

↓

Planner

↓

Factory

↓

SQLAgent

↓

Response
```

---

# Next Phase

## Phase 2

Connect SQLAgent with PostgreSQL.

Flow

```
SQLAgent

↓

Repository

↓

PostgreSQL

↓

Actual SQL Query

↓

Result
```

---

## Phase 3

Connect Bedrock / Claude

```
SQL Result

↓

LLM

↓

Natural Language Summary
```

Example

Instead of

```
1000 rows
```

Return

```
Sales increased by 18% compared to last month.
```

---

## Phase 4

Replace manual routing with LangGraph

Planner

↓

Conditional Routing

↓

SQL

↓

Critic

↓

Memory

↓

Final Answer

---

# Personal Note

This project is being built to understand enterprise AI architecture from first principles rather than copying tutorials.

Every component is implemented only after understanding:

- Why it exists
- What problem it solves
- How it is used in production
- How to explain it confidently in interviews