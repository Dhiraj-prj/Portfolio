# Dhiraj Parajuli — Django Portfolio

A modern, aesthetic personal portfolio website built with Django.

## Features
- Dynamic content via Django Admin Panel
- Profile photo upload support
- Projects, Skills, Experience, Education, Achievements — all editable from admin
- Custom cursor, scroll animations, marquee, floating chips
- Fully responsive (mobile-friendly)
- SQLite database (zero config)

## Setup Instructions

### 1. Install Requirements
```bash
pip install django pillow
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```

### 4. Load Sample Data (optional — pre-seeded with your CV info)
The database `db.sqlite3` included already has all your data seeded.

### 5. Run the Server
```bash
python manage.py runserver
```

Then open:
- **Portfolio:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Admin Login (pre-created)
- **Username:** dhiraj
- **Password:** admin123
> ⚠️ Change this password immediately in production!

## How to Update Your Portfolio
1. Go to http://127.0.0.1:8000/admin/
2. Log in with your credentials
3. Edit any section:
   - **Profile** → Update name, bio, photo, contact info, resume
   - **Projects** → Add/edit/delete projects with tech stack and links
   - **Skill Categories** → Add new skill groups and individual skills
   - **Experience** → Update your work history
   - **Education** → Add/edit academic records
   - **Achievements** → Highlight your wins

## Adding Your Profile Photo
1. Go to Admin → Profile → Edit
2. Upload a photo (JPG/PNG recommended, square or portrait)
3. Save — it appears instantly on the site

## Project Structure
```
portfolio/
├── core/
│   ├── models.py       # All data models
│   ├── views.py        # Homepage view
│   ├── admin.py        # Admin panel config
│   └── urls.py
├── templates/
│   └── core/
│       └── index.html  # Main template
├── static/
│   ├── css/style.css   # All styles
│   └── js/main.js      # Animations & cursor
├── portfolio/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3          # Pre-seeded database
└── manage.py
```

## Deploying to Production
For deployment (e.g. PythonAnywhere, Railway, Render):
1. Set `DEBUG = False` in settings.py
2. Set a strong `SECRET_KEY`
3. Add your domain to `ALLOWED_HOSTS`
4. Run `python manage.py collectstatic`
