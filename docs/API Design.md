# Lynkio - API Design

## 1. Overview

This document describes the REST API design for Lynkio.

The API follows REST principles and communicates using JSON.

All endpoints are exposed through the FastAPI backend.

Base URL:

```text
/api/v1
```

---

# 2. Authentication

Authentication uses JWT (JSON Web Tokens).

Protected endpoints require:

```http
Authorization: Bearer <token>
```

---

# 3. Authentication Endpoints

## Register

Endpoint:

```http
POST /auth/register
```

Request:

```json
{
  "email": "user@example.com",
  "password": "SecurePassword123"
}
```

Response:

```json
{
  "message": "User registered successfully"
}
```

---

## Login

Endpoint:

```http
POST /auth/login
```

Request:

```json
{
  "email": "user@example.com",
  "password": "SecurePassword123"
}
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

## Get Current User

Endpoint:

```http
GET /auth/me
```

Response:

```json
{
  "id": "uuid",
  "email": "user@example.com"
}
```

---

# 4. Bookmark Endpoints

## Create Bookmark

Endpoint:

```http
POST /bookmarks
```

Request:

```json
{
  "url": "https://fastapi.tiangolo.com",
  "notes": "Useful FastAPI documentation"
}
```

Response:

```json
{
  "id": "uuid",
  "title": "FastAPI",
  "summary": "Generated summary...",
  "tags": ["python", "api", "fastapi"]
}
```

---

## Get All Bookmarks

Endpoint:

```http
GET /bookmarks
```

Optional Query Parameters:

```http
?page=1
&limit=20
&search=python
```

Response:

```json
[
  {
    "id": "uuid",
    "title": "FastAPI",
    "url": "https://..."
  }
]
```

---

## Get Bookmark By Id

Endpoint:

```http
GET /bookmarks/{id}
```

---

## Update Bookmark

Endpoint:

```http
PUT /bookmarks/{id}
```

Request:

```json
{
  "title": "Updated Title",
  "notes": "Updated Notes",
  "is_favorite": true
}
```

---

## Delete Bookmark

Endpoint:

```http
DELETE /bookmarks/{id}
```

Response:

```json
{
  "message": "Bookmark deleted successfully"
}
```

---

# 5. Collection Endpoints

## Create Collection

Endpoint:

```http
POST /collections
```

Request:

```json
{
  "name": "Programming",
  "description": "Programming resources"
}
```

---

## Get Collections

Endpoint:

```http
GET /collections
```

---

## Update Collection

Endpoint:

```http
PUT /collections/{id}
```

---

## Delete Collection

Endpoint:

```http
DELETE /collections/{id}
```

---

# 6. Tag Endpoints

## Get Tags

Endpoint:

```http
GET /tags
```

---

## Get Bookmarks By Tag

Endpoint:

```http
GET /tags/{id}/bookmarks
```

---

# 7. Favorites

## Add Favorite

Endpoint:

```http
PATCH /bookmarks/{id}/favorite
```

---

## Remove Favorite

Endpoint:

```http
PATCH /bookmarks/{id}/unfavorite
```

---

# 8. AI Features

## Regenerate Summary

Endpoint:

```http
POST /bookmarks/{id}/generate-summary
```

---

## Regenerate Tags

Endpoint:

```http
POST /bookmarks/{id}/generate-tags
```

---

# 9. Future Endpoints

Future API capabilities:

## Semantic Search

```http
POST /search/semantic
```

Request:

```json
{
  "query": "FastAPI authentication tutorials"
}
```

---

## Recommendations

```http
GET /recommendations
```

---

# 10. Error Handling

Standard error format:

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Bookmark not found"
  }
}
```

---

# 11. API Versioning

Current version:

```text
v1
```

Example:

```text
/api/v1/bookmarks
```

Future versions:

```text
/api/v2
/api/v3
```
