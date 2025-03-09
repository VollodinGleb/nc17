# Installation
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Dependencies**
   Install the required dependencies for the project using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Database**
   Update the `settings.py` file with your database credentials or modify the `DATABASES` dictionary if required.

   To apply the database migrations:
   ```bash
   python manage.py migrate
   ```

4. **Collect Static Files (for Production)**
   ```bash
   python manage.py collectstatic
   ```

---

# Running the Project

1. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

   By default, the application will be available at `http://127.0.0.1:8000/`.

2. **Running in Production**
   Use a WSGI server (e.g., Gunicorn, uWSGI) for deployment in production. Don't forget to configure the static files, database, and environment settings appropriately.

---

# Additional Information

- **Create a Superuser (Admin Panel Access):**
   To create an admin user for accessing the Django Admin panel:
   ```bash
   python manage.py createsuperuser
   ```
---

# Troubleshooting

If you encounter issues:
1. Make sure all dependencies are installed by verifying your virtual environment.
2. Confirm the database configuration is correct.
3. Check the console logs for errors.
