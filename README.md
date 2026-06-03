# UniSolver

UniSolver este o platformă web educațională dezvoltată pentru facilitarea colaborării academice dintre studenți, elevi și tutori. Aplicația permite găsirea tutorilor, programarea sesiunilor de tutoring, gestionarea cererilor și colaborarea în echipe pentru proiecte academice.

---

# Funcționalități principale

## Autentificare și roluri

Platforma oferă autentificare și înregistrare pentru trei tipuri de utilizatori:

- Student/Elev
- Tutor
- Administrator

Fiecare rol are acces la funcționalități și dashboard-uri specifice.

---

# Funcționalități pentru tutori

Tutorii pot:

- publica anunțuri pentru materiile predate;
- selecta una sau mai multe date disponibile;
- seta intervale orare pentru fiecare zi;
- gestiona cererile primite;
- accepta sau respinge cereri;
- vizualiza sesiunile programate în calendar;
- primi review-uri și feedback.

---

# Funcționalități pentru studenți

Studenții pot:

- căuta tutori după materie;
- filtra anunțurile disponibile;
- trimite cereri de tutoring;
- selecta intervale orare din disponibilitatea tutorului;
- vizualiza statusul cererilor;
- vedea sesiunile aprobate în calendar;
- aplica la proiecte academice.

---

# Calendar interactiv

Platforma include un calendar pentru sesiunile de tutoring:

- sesiunile acceptate sunt adăugate automat;
- utilizatorii pot selecta o zi din calendar;
- sunt afișate programările din ziua respectivă;
- sincronizare între student și tutor.

---

# Sistem de cereri

Fluxul unei cereri:

1. Studentul selectează un tutor;
2. Alege materia și intervalul disponibil;
3. Trimite cererea;
4. Tutorul acceptă sau respinge;
5. Dacă este acceptată:
   - sesiunea este creată automat;
   - apare în calendarul ambilor utilizatori.

---

# Modul pentru proiecte

Platforma permite:

- crearea echipelor de proiect;
- publicarea anunțurilor pentru proiecte;
- aplicarea la proiecte;
- gestionarea membrilor echipei.

---

# Tehnologii utilizate

## Backend
- Python
- Django
- Django REST Framework
- JWT Authentication

## Frontend
- HTML
- CSS
- JavaScript
- Django Templates

## Bază de date
- SQLite

## Tooling
- Git & GitHub
- VS Code
- Overleaf
- Draw.io / Mermaid

---

# Structura proiectului

```text
UniSolver/
│
├── config/
├── users/
├── tutoring/
├── teams/
├── reviews/
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt

# Echipa proiectului

| Membru | Rol | Contribuții |
|---|---|---|
| Blidar Larisa-Anamaria | Project Manager & Backend Developer | Coordonarea proiectului, dezvoltarea backend-ului Django, autentificare, sistem tutoring, calendar, integrarea funcționalităților principale |
| Balaj Andreea-Paula | Backend Developer | Implementarea modelelor bazei de date, dezvoltarea API-urilor REST și logica backend |
| Chilea Daniela-Florentina | Frontend Developer | Dezvoltarea interfeței utilizator folosind HTML, CSS și JavaScript |
| Cocoș Patric-Daniel-Traian | UI/UX Designer | Design-ul aplicației, organizarea componentelor vizuale și îmbunătățirea experienței utilizatorului |