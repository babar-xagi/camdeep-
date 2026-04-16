#!/usr/bin/env python
"""
CAMDEEP Django Project - Quick Start Guide

🎯 SETUP INSTRUCTIONS:

1. Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies using uv (recommended):
   uv pip install -r requirements.txt

3. Setup environment:
   cp .env.example .env
   # Update .env with your settings

4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser:
   python manage.py createsuperuser

6. Load initial data (7 core skills):
   python manage.py load_initial_data

7. Run development server:
   python manage.py runserver

8. Access the application:
   - Homepage: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - Default login: Use your superuser credentials

📁 PROJECT STRUCTURE:

camdeep-/
├── config/              # Project configuration
├── templates/           # HTML templates (Tailwind CSS)
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded files
├── accounts/           # User authentication & profiles
├── core/               # Site settings & homepage
├── skills/             # 7 core skills management
├── programs/           # CAMDEEP programs & projects
├── schools/            # Partner schools management
├── students/           # Student records & enrollment
├── trainers/           # Trainer profiles & assignments
├── assessments/        # Activities & worksheets
├── certificates/       # Certificate generation
├── partnerships/       # MOU & partnership management
├── resources/          # Learning resources
├── cms/                # Blog & dynamic content
└── manage.py           # Django management

🔐 SECURITY:
- Change SECRET_KEY in production
- Set DEBUG=False in production
- Use PostgreSQL instead of SQLite for production
- Configure ALLOWED_HOSTS properly
- Use environment variables for sensitive data

📚 DOCUMENTATION:
- Django: https://docs.djangoproject.com/en/6.0/
- Tailwind CSS: https://tailwindcss.com/docs
- DRF: https://www.django-rest-framework.org/

🆘 TROUBLESHOOTING:

Q: ModuleNotFoundError when running migrations
A: Ensure all apps are in INSTALLED_APPS in settings.py

Q: Static files not loading
A: Run: python manage.py collectstatic

Q: Database errors
A: Delete db.sqlite3 and migrations, then:
   python manage.py makemigrations
   python manage.py migrate

Q: Port 8000 already in use
A: python manage.py runserver 8001

💡 DEVELOPMENT TIPS:
- Use Django Debug Toolbar: pip install django-debug-toolbar
- Use django-extensions for shell_plus: python manage.py shell_plus
- Create custom management commands for data loading
- Use signals for automatic model updates
- Implement caching for frequently accessed data

🚀 NEXT STEPS:
1. Create fixture data for the 7 core skills
2. Set up email configuration
3. Implement user registration and email verification
4. Create student dashboards
5. Set up assessment grading system
6. Implement certificate generation (WeasyPrint/ReportLab)
7. Configure Celery for async tasks
8. Set up Redis for caching
9. Create API endpoints for mobile apps
10. Deploy to production (Heroku, AWS, DigitalOcean)

"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    print(__doc__)

