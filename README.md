# ExploreEase – Django Backend Starter

This project is based on the uploaded ExploreEase Tour & Travel PPT. It uses Python, Django and SQLite.

## Included modules
- City
- Package
- Booking
- Contact
- Gallery
- Review
- Team
- Feedback (admin-managed)

The project includes Django Admin and simple Django templates so you can test the backend in a browser. The design is intentionally basic; your team's final frontend styling can replace these templates.

## 1. Requirements
- Python 3.10 or newer
- VS Code (recommended)

## 2. Setup on Windows PowerShell

Open PowerShell in this folder and run these commands one by one:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations tours 
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
If PowerShell blocks activation, run this once in the same terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate the environment again.

## 3. Open the website
- Website: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

Log in to Admin using the superuser username and password you created.

## 4. Add sample data
From Admin, add City records first, then add Package records because each package belongs to a city. Add gallery images, team members and other content as needed.

## 5. Important notes
- SQLite database is created automatically after `migrate`.
- Uploaded images are stored in the `media/` folder.
- `DEBUG=True` and the development secret key are for local learning only. Do not deploy this configuration publicly.
- This is a working starter implementation, not a deployed website. Payment gateway, email/SMS notifications, live transport/hotel availability and mobile app features from the PPT's Future Scope are not implemented.
- The PPT mentions both SQLite and MySQL; this starter uses SQLite for easy beginner setup. MySQL can be configured later if the team requires it.
