# UniSolver API Specification

## Authentication

### Register
POST /api/auth/register/

Request:
{
  "username": "maria",
  "email": "maria@example.com",
  "password": "test12345"
}

Response:
{
  "id": 2,
  "username": "maria",
  "email": "maria@example.com"
}

### Login
POST /api/auth/login/

Request:
{
  "username": "maria",
  "password": "test12345"
}

Response:
{
  "refresh": "...",
  "access": "..."
}

---

## Users

### Get users
GET /api/users/

Headers:
Authorization: Bearer <access_token>

Response:
[
  {
    "id": 1,
    "username": "larisa",
    "email": "larisa@example.com"
  }
]

---

## Academic Profiles

### Get academic profiles
GET /api/academic-profiles/

### Create academic profile
POST /api/academic-profiles/

Request:
{
  "university": "Universitatea X",
  "specialization": "Informatica",
  "study_year": 2,
  "bio": "Student interesat de baze de date"
}

---

## Skills

### Get skills
GET /api/skills/

### Create skill
POST /api/skills/

Request:
{
  "subject": "Baze de date",
  "level": "advanced",
  "user": 1
}

---

## Tutoring Requests

### Get tutoring requests
GET /api/tutoring-requests/

### Create tutoring request
POST /api/tutoring-requests/

Request:
{
  "tutor": 1,
  "subject": "Baze de date",
  "message": "Am nevoie de ajutor pentru proiectul SQL."
}

Response:
{
  "id": 1,
  "student": "maria",
  "tutor": 1,
  "subject": "Baze de date",
  "message": "Am nevoie de ajutor pentru proiectul SQL.",
  "status": "pending",
  "created_at": "2026-05-13T16:09:54Z"
}

### Update tutoring request
PATCH /api/tutoring-requests/1/

Request:
{
  "status": "accepted"
}

### Delete tutoring request
DELETE /api/tutoring-requests/1/

---

## Project Teams

### Get project teams
GET /api/project-teams/

### Create project team
POST /api/project-teams/

Request:
{
  "owner": 1,
  "title": "Platforma colaborare studenti",
  "description": "Aplicatie pentru tutoring si proiecte",
  "subject": "Inginerie software",
  "status": "open"
}

---

## Reviews

### Get reviews
GET /api/reviews/

### Create review
POST /api/reviews/

Request:
{
  "reviewer": 1,
  "reviewed_user": 2,
  "rating": 5,
  "comment": "Explicatii foarte clare."
}