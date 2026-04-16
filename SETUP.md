# 🌟 CAMDEEP Django Project - Setup Guide

## Project Overview

CAMDEEP is a comprehensive Django-based educational platform designed to manage and deliver a real-world educational framework with 7 core competency skills for students in Grades 6-10.

**Technology Stack:**
- Django 6.0.4
- Python 3.9+
- Tailwind CSS (CDN)
- SQLite (Development) / PostgreSQL (Production)
- DRF (Django REST Framework)
- Bootstrap & Admin Customization

---

## 📋 Prerequisites

- Python 3.9 or higher
- pip or uv package manager (recommended: uv)
- PostgreSQL (for production)
- Git

---

## 🚀 Quick Start (5 minutes)

### 1. Clone & Setup Virtual Environment

```bash
# Clone the repository
git clone <repository-url>
cd camdeep-

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies with uv

```bash
# Using uv (recommended - faster)
uv pip install -r requirements.txt

# OR using traditional pip
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# vim .env  (or use your editor)
```

### 4. Initialize Database

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load initial data (7 core skills)
python manage.py load_initial_data

# Create superuser
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
# Access at http://localhost:8000
# Admin at http://localhost:8000/admin
```

---

## 📁 Project Structure

```
camdeep-/
├── config/                  # Django settings & URLs
│   ├── settings.py         # Main configuration
│   ├── urls.py             # Root URL routing
│   ├── asgi.py             # ASGI configuration
│   └── wsgi.py             # WSGI configuration
│
├── templates/              # HTML templates (Tailwind CSS)
│   ├── base.html           # Base template with navigation
│   ├── core/
│   │   ├── home.html       # Homepage
│   │   ├── about.html      # About page
│   │   ├── contact.html    # Contact form
│   │   └── faq.html        # FAQ page
│   ├── skills/
│   ├── programs/
│   ├── schools/
│   ├── resources/
│   ├── cms/
│   └── accounts/
│
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                  # User-uploaded files
│   ├── profile_pictures/
│   ├── programs/
│   ├── branding/
│   └── ...
│
├── accounts/               # User authentication & profiles
│   ├── models.py          # CustomUser, UserRole, AuditLog
│   ├── views.py           # Login, Register, Profile
│   ├── urls.py            # Auth URLs
│   ├── admin.py           # Django admin config
│   └── migrations/
│
├── core/                   # Site settings & homepage
│   ├── models.py          # SiteSetting, HomePage, Feature, FAQ
│   ├── views.py           # Core views
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── skills/                 # 7 core skills
│   ├── models.py          # Skill, SkillLevel, SkillArea
│   ├── views.py           # Skill list & detail views
│   ├── urls.py
│   ├── admin.py
│   ├── management/
│   │   └── commands/
│   │       └── load_initial_data.py
│   └── ...
│
├── programs/               # Programs & projects
├── schools/                # Partner schools
├── students/               # Student records & enrollment
├── trainers/               # Trainer management
├── assessments/            # Assessments & activities
├── certificates/           # Certificate generation
├── partnerships/           # MOU management
├── resources/              # Learning resources
├── cms/                    # Blog & content management
│
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore file
├── manage.py              # Django management script
├── QUICKSTART.py          # Quick start guide
└── README.md              # Project documentation
```

---

## ⚙️ Configuration

### Environment Variables (.env)

```dotenv
# Django Settings
DEBUG=True
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DATABASE_URL=sqlite:///db.sqlite3
# For PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost:5432/camdeep

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Celery (optional)
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### Key Settings Features

- **Custom User Model**: Extended Django User with roles and profile fields
- **REST Framework**: Configured with pagination, filtering, and authentication
- **CORS Support**: For future mobile/frontend apps
- **Crispy Forms**: Bootstrap-styled forms with Tailwind CSS
- **Email Configuration**: Console, SMTP, or backend of choice
- **Security**: CSRF, XSS protection, secure headers in production
- **Logging**: Configured for development and production

---

## 🗄️ Database Setup

### SQLite (Development)

Default configuration - works out of the box:

```bash
python manage.py migrate
```

### PostgreSQL (Production)

1. Install PostgreSQL and create database:

```bash
createdb camdeep
```

2. Update .env:

```dotenv
DATABASE_URL=postgresql://user:password@localhost:5432/camdeep
```

3. Install psycopg2:

```bash
pip install psycopg2-binary
```

4. Run migrations:

```bash
python manage.py migrate
```

---

## 👥 User Roles

CAMDEEP supports 5 user roles:

| Role | Permissions |
|------|-------------|
| **Admin** | Full system access, user management, settings |
| **Trainer** | Manage assigned schools, provide feedback, grade assessments |
| **School Admin** | Manage school profile, students, programs |
| **Student** | Enroll in programs, submit assessments, view certificates |
| **Parent** | View student progress, access resources |

---

## 🎯 Initial Data Loading

The project includes a management command to load the 7 core skills:

```bash
python manage.py load_initial_data
```

This creates:
- 7 Core Skills (Creativity, Analytical Thinking, Management, Digital, Entrepreneurship, Ethics, Problem Solving)
- 4 Proficiency Levels per skill (Beginner, Intermediate, Advanced, Expert)
- Site Settings with CAMDEEP branding
- Featured sections for homepage

---

## 📱 Admin Panel

Access Django admin at `/admin/` with superuser credentials.

**Configured Admin Interfaces:**
- CustomUser Management
- Skill & Skill Level Management
- Program & Project Management
- School Management
- Student Enrollment
- Assessment & Grading
- Certificate Management
- Resource Management
- Blog & Content Management
- Contact Messages

---

## 🔒 Security Checklist

### Development
- ✅ DEBUG=True (for development only)
- ✅ SQLite database
- ✅ Console email backend
- ✅ CSRF protection enabled

### Production
- ⚠️ DEBUG=False
- ⚠️ SECRET_KEY = strong random string
- ⚠️ ALLOWED_HOSTS = specific domains
- ⚠️ Use PostgreSQL
- ⚠️ Configure HTTPS/SSL
- ⚠️ Set secure cookies
- ⚠️ Configure proper email backend
- ⚠️ Use environment variables for secrets
- ⚠️ Set up proper logging
- ⚠️ Configure rate limiting

---

## 🚀 Deployment

### Heroku Deployment

1. Create Procfile:

```bash
web: gunicorn config.wsgi
release: python manage.py migrate
```

2. Create runtime.txt:

```
python-3.11.0
```

3. Deploy:

```bash
heroku create camdeep-app
heroku config:set DEBUG=False SECRET_KEY=your-secret-key
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
```

### Docker Deployment

1. Create Dockerfile:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "config.wsgi"]
```

2. Build and run:

```bash
docker build -t camdeep .
docker run -p 8000:8000 camdeep
```

### AWS/DigitalOcean Deployment

Use uWSGI + Nginx:

```bash
pip install uWSGI
uwsgi --http :8000 --wsgi-file config/wsgi.py --master --processes 4
```

---

## 📊 Database Models Overview

### Core Models

**accounts.CustomUser**
- Extended Django User with roles and profile fields
- Profile picture, bio, address information
- Email verification status

**skills.Skill**
- 7 core skills
- Levels and proficiency areas
- Learning outcomes

**programs.Program**
- Skill-based programs (Grade-specific)
- Associated projects and modules
- Learning outcomes and resources

**schools.School**
- Partner schools information
- MOU status and partnership details
- Contact and administrative information

**students.Student**
- Student enrollment records
- Roll numbers and guardian information
- Program enrollments and skill progress

**certificates.Certificate**
- Issued certificates with UUID
- PDF generation and verification

---

## 🧪 Testing

Run tests with:

```bash
python manage.py test

# With coverage:
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📚 API Endpoints (Future)

REST API will support:
- `/api/skills/` - Skill list and details
- `/api/programs/` - Program management
- `/api/students/` - Student records
- `/api/assessments/` - Assessment submission
- `/api/certificates/` - Certificate generation

---

## 🛠️ Management Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load initial data
python manage.py load_initial_data

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Clear cache
python manage.py clear_cache

# Shell with Django context
python manage.py shell
```

---

## 📖 Key Files

| File | Purpose |
|------|---------|
| `config/settings.py` | Django settings & configuration |
| `config/urls.py` | URL routing |
| `templates/base.html` | Base template with Tailwind CSS |
| `.env.example` | Environment variables template |
| `requirements.txt` | Python dependencies |
| `manage.py` | Django management script |

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Database errors after migrations

**Solution:**
```bash
# Reset database (development only!)
rm db.sqlite3
python manage.py migrate
```

### Issue: Static files not loading

**Solution:**
```bash
python manage.py collectstatic --noinput
```

### Issue: Port 8000 already in use

**Solution:**
```bash
python manage.py runserver 8001
```

### Issue: Import errors in models

**Ensure:**
- All apps are in `INSTALLED_APPS` in settings.py
- Foreign keys use string references: `'app.Model'`
- Circular imports are avoided

---

## 📞 Support

For issues and questions:
- Email: info@camdeep.edu
- Phone: +92 316 8494258
- GitHub Issues: [Create an issue]

---

## 📄 License

This project is proprietary and intended for CAMDEEP's educational partnerships. Unauthorized use or reproduction without permission is prohibited.

---

## ✅ Next Steps

After setup:

1. ✅ Run initial data loading command
2. ✅ Create a superuser account
3. ✅ Access admin panel and customize
4. ✅ Create test programs and skills
5. ✅ Create test user accounts with different roles
6. ✅ Configure email settings
7. ✅ Customize templates and styling
8. ✅ Set up API endpoints
9. ✅ Deploy to production

---

**Last Updated:** April 2024
**Version:** 1.0.0

