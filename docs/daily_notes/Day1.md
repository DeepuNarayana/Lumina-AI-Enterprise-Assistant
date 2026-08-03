# Day 01 - React to FastAPI Communication

## Goal

Connect React frontend with FastAPI backend.

---

## Topics Learned

- React Components
- useState
- Controlled Components
- Form Submission
- preventDefault()
- Axios
- Async / Await
- FastAPI REST API
- CORS

---

## Flow

User

↓

LoginForm

↓

handleLogin()

↓

AuthService.login()

↓

Axios POST

↓

FastAPI /ai/chat

↓

AIService

↓

Planner Agent

↓

LLM Agent

↓

Response

↓

React UI

---

## Problems Faced

### Problem 1

```
await expressions are only allowed within async functions
```

Reason:

handleLogin was not declared as async.

Solution:

```tsx
const handleLogin = async (event: FormEvent) => {
```

---

### Problem 2

```
Axios Network Error
```

Reason:

CORS middleware was missing.

Solution:

Added:

```python
CORSMiddleware
```

---

### Problem 3

405 Method Not Allowed

Reason:

Browser sent OPTIONS request before POST.

Understanding:

React

↓

OPTIONS

↓

FastAPI CORS

↓

POST

---

## Final Result

Successfully sent request from React to FastAPI and received AI response.

Example:

```json
{
  "response": "AI Response: I understand your question..."
}
```