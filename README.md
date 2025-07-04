# Feedback Portal – Django Project

A mini project built with Django that demonstrates:

- Django Models, Views, Templates (MVT)
- Admin Panel integration
- Decorators for validation
- OOP practices using form/service layers
- GitHub version control
- Jenkins CI/CD support
- Jira ticket-based workflow simulation

## Tech Stack

- Python 3.12
- Django 5.2
- SQLite3 (for development)
- Git & GitHub
- Jenkins

## Setup Instructions

```bash
git clone https://github.com/<your-username>/feedback_portal.git
cd feedback_portal
python -m venv .venv
source .venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


```bash
pip freeze > requirements.txt