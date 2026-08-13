# OneTag Backend

Backend API for the OneTag project, developed with Django and Django REST Framework.

OneTag is an NFC bracelet platform that allows users to manage their digital profile and share information through an NFC-enabled bracelet.

## Technologies

* Python
* Django
* Django REST Framework
* JWT Authentication
* drf-spectacular / Swagger
* SQLite (development)

## Project Structure

```text
onetag-backend/
├── accounts/
├── bracelets/
├── beads/
├── colors/
├── disks/
├── cart/
├── orders/
├── payments/
├── shipping/
├── nfc/
├── social_links/
├── config/
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aya896/onetagebackend.git
cd onetagebackend
```

Create and activate a virtual environment:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI schema:

```text
http://127.0.0.1:8000/api/schema/
```

## Main API Endpoints

### Accounts

```text
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/accounts/token/refresh/
GET  /api/accounts/profile/
```

Authentication uses JWT tokens.

### Bracelets

```text
GET  /api/bracelets/
POST /api/bracelets/
GET  /api/bracelets/owned/
```

### NFC

```text
POST /api/nfc/activate/
GET  /api/nfc/profile/<bracelet_id>/
GET  /api/nfc/scan/<uid>/
```

### Cart

```text
GET    /api/cart/
POST   /api/cart/
GET    /api/cart/<id>/
PUT    /api/cart/<id>/
PATCH  /api/cart/<id>/
DELETE /api/cart/<id>/
```

### Orders

```text
GET    /api/orders/
POST   /api/orders/
GET    /api/orders/<id>/
PUT    /api/orders/<id>/
PATCH  /api/orders/<id>/
DELETE /api/orders/<id>/
```

### Other APIs

```text
/api/beads/
/api/colors/
/api/disks/
/api/payments/
/api/shipping/
/api/social-links/
```

## Frontend Integration

During local development, the frontend can communicate with the backend using:

```text
http://127.0.0.1:8000/api/
```

For example:

```text
http://127.0.0.1:8000/api/accounts/login/
http://127.0.0.1:8000/api/bracelets/
http://127.0.0.1:8000/api/nfc/scan/<uid>/
```

For authenticated requests, the frontend should send the JWT access token:

```text
Authorization: Bearer <access_token>
```

## NFC Flow

The main NFC flow is:

```text
User
  ↓
Activate Bracelet
  ↓
NFC UID is associated with the bracelet
  ↓
NFC Profile is created
  ↓
Smartphone scans the bracelet
  ↓
Backend receives the UID
  ↓
Backend returns the associated profile
```

## Development Notes

The project currently uses SQLite for development.

The local database file and virtual environment are intentionally excluded from GitHub using `.gitignore`.

The backend should be started before running the frontend during local development.

## GitHub Repository

Repository:

https://github.com/aya896/onetagebackend
