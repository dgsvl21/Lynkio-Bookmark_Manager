# Lynkio - Software Requirements Specification

## 1. Introduction

### 1.1 Purpose

This document defines the functional and non-functional requirements for Lynkio.

Lynkio is an intelligent bookmark management platform designed to help users save, organize, and rediscover web content through Artificial Intelligence-powered features such as automatic summarization, tag generation, and semantic search.

The purpose of this document is to establish a clear understanding of the system's expected behavior before implementation begins.

---

## 1.2 Scope

Lynkio allows users to:

- Create personal accounts
- Save bookmarks
- Organize bookmarks
- Search bookmarks
- Access bookmarks from any device
- Generate AI-powered summaries
- Generate AI-powered tags
- Discover previously saved content

The system will be developed as a web application accessible through modern browsers.

---

## 1.3 Intended Audience

This document is intended for:

- Developers
- Project stakeholders
- Future contributors
- Academic evaluation purposes

---

# 2. Product Overview

## 2.1 Product Vision

Traditional bookmark managers only store links.

Lynkio aims to transform bookmarks into a personal knowledge repository by automatically enriching saved content with metadata, summaries, and intelligent search capabilities.

---

## 2.2 Product Goals

The system should:

- Simplify bookmark organization
- Improve information retrieval
- Reduce information loss
- Support personal knowledge management
- Provide intelligent content discovery

---

# 3. User Roles

## 3.1 Registered User

A registered user can:

- Register an account
- Authenticate
- Create bookmarks
- Update bookmarks
- Delete bookmarks
- Search bookmarks
- Manage collections
- Access personal data

---

# 4. Functional Requirements

## Authentication

### FR-01 User Registration

The system shall allow users to create an account using:

- Email
- Password

Acceptance Criteria:

- Email must be unique
- Password must meet minimum security requirements

---

### FR-02 User Login

The system shall allow registered users to authenticate.

Acceptance Criteria:

- Valid credentials grant access
- Invalid credentials are rejected

---

### FR-03 User Logout

The system shall allow authenticated users to terminate their session.

---

## Bookmark Management

### FR-04 Create Bookmark

The system shall allow users to save a bookmark.

Required Information:

- URL

Optional Information:

- Custom title
- Notes

---

### FR-05 View Bookmarks

The system shall allow users to view all personal bookmarks.

---

### FR-06 Update Bookmark

The system shall allow users to update bookmark information.

Editable Fields:

- Title
- Notes
- Collections
- Favorite status

---

### FR-07 Delete Bookmark

The system shall allow users to permanently delete bookmarks.

---

### FR-08 Bookmark Details

The system shall display bookmark details including:

- URL
- Title
- Summary
- Tags
- Creation date

---

## Search

### FR-09 Keyword Search

The system shall allow users to search bookmarks using keywords.

---

### FR-10 Filter Search

The system shall allow filtering by:

- Tags
- Collections
- Favorites

---

## AI Features

### FR-11 Summary Generation

The system shall automatically generate a summary for newly saved bookmarks.

---

### FR-12 Tag Generation

The system shall automatically generate tags for newly saved bookmarks.

---

### FR-13 Content Extraction

The system shall extract relevant textual content from a webpage before AI processing.

---

## Collections

### FR-14 Create Collection

The system shall allow users to create collections.

Examples:

- Programming
- University
- Personal
- Research

---

### FR-15 Manage Collections

The system shall allow bookmarks to be assigned to collections.

---

## Favorites

### FR-16 Favorite Bookmarks

The system shall allow users to mark bookmarks as favorites.

---

# 5. Future Functional Requirements

These requirements are planned for future releases.

---

### FFR-01 Semantic Search

The system shall allow users to search bookmarks based on meaning rather than exact keywords.

---

### FFR-02 Recommendations

The system shall suggest relevant bookmarks based on user activity.

---

### FFR-03 Similar Content Discovery

The system shall identify bookmarks related to the currently viewed bookmark.

---

# 6. Non-Functional Requirements

## NFR-01 Security

The system shall:

- Hash passwords
- Use JWT authentication
- Protect user data
- Validate user input

---

## NFR-02 Performance

The system should:

- Return API responses within acceptable time limits
- Handle concurrent users efficiently

---

## NFR-03 Scalability

The architecture shall support future growth in:

- Users
- Bookmarks
- Collections

---

## NFR-04 Availability

The system should remain accessible whenever deployed.

---

## NFR-05 Usability

The user interface shall be:

- Intuitive
- Responsive
- Easy to navigate

---

## NFR-06 Maintainability

The codebase shall:

- Follow modular architecture
- Be documented
- Be easily extensible

---

## NFR-07 Portability

The application shall be deployable using Docker containers.

---

# 7. Constraints

The project will use:

- Python (FastAPI)
- React
- PostgreSQL
- OpenAI API
- Docker

---

# 8. Assumptions

It is assumed that:

- Users have internet access
- OpenAI API is available
- Target browsers support modern web standards

---

# 9. Success Criteria

The project will be considered successful if users can:

- Create an account
- Save bookmarks
- Organize bookmarks
- Retrieve bookmarks efficiently
- Benefit from AI-generated summaries and tags

while maintaining acceptable performance and security standards.
