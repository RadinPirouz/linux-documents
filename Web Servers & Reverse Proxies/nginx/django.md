### Installing Packages from Ubuntu Repositories

1. Update your Ubuntu system:
    ```bash
    sudo apt update
    ```

2. Install necessary packages:
    ```bash
    sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
    ```

### Creating the PostgreSQL Database and User

3. Log into an interactive Postgres session:
    ```bash
    sudo -u postgres psql
    ```

4. Inside the PostgreSQL prompt, create a database for your project:
    ```sql
    CREATE DATABASE myproject;
    ```

5. Create a database user for your project with a secure password:
    ```sql
    CREATE USER myprojectuser WITH PASSWORD 'password';
    ```

6. Modify connection parameters for the user:
    ```sql
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    ```

7. Grant the new user access to administer the new database:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    ```

8. Exit the PostgreSQL prompt:
    ```sql
    \q
    ```

### Creating a Python Virtual Environment for Your Project

9. Create a directory for your project files:
    ```bash
    mkdir ~/myprojectdir
    cd ~/myprojectdir
    ```

10. Create a Python virtual environment:
    ```bash
    python3 -m venv myprojectenv
    ```

11. Activate the virtual environment:
    ```bash
    source myprojectenv/bin/activate
    ```

12. Install Django, Gunicorn, and psycopg2:
    ```bash
    pip install django gunicorn psycopg2-binary
    ```

### Creating and Configuring a New Django Project

13. Create a new Django project with a defined directory:
    ```bash
    django-admin startproject myproject ~/myprojectdir
    ```

14. Adjust settings in the `settings.py` file:
    - Set `ALLOWED_HOSTS` to `['*']`
    - Configure `DATABASES` with PostgreSQL details

15. Add static root configuration to `settings.py`:
    ```python
    import os
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    ```

16. Migrate initial database schema:
    ```bash
    ~/myprojectdir/manage.py makemigrations
    ~/myprojectdir/manage.py migrate
    ```

17. Create an administrative user:
    ```bash
    ~/myprojectdir/manage.py createsuperuser
    ```

18. Collect static content:
    ```bash
    ~/myprojectdir/manage.py collectstatic
    ```

19. Allow port 8000:
    ```bash
    sudo ufw allow 8000
    ```

20. Start Django development server:
    ```bash
    ~/myprojectdir/manage.py runserver 0.0.0.0:8000
    ```

21. Access your application in a web browser.

22. Stop Apache2 service:
    ```bash
    sudo /etc/init.d/apache2 restart
    ```

### Testing Gunicorn

23. Test Gunicorn to ensure it can serve the application:
    ```bash
    cd ~/myprojectdir
    gunicorn --bind 0.0.0.0:8000 myproject.wsgi
    ```

24. Stop Gunicorn:
    - Press `CTRL-C`

### Creating systemd Socket and Service Files for Gunicorn

25. Create a systemd socket file for Gunicorn:
    ```bash
    sudo nano /etc/systemd/system/gunicorn.socket
    ```

26. Create and open a systemd service file for Gunicorn:
    ```bash
    sudo nano /etc/systemd/system/gunicorn.service
    ```

27. Configure the service file with appropriate details.

### Checking for the Gunicorn Socket File

28. Check the status of the Gunicorn socket:
    ```bash
    sudo systemctl status gunicorn.socket
    ```

29. Check for the existence of the Gunicorn socket file:
    ```bash
    file /run/gunicorn.sock
    ```

30. Check Gunicorn socket logs:
    ```bash
    sudo journalctl -u gunicorn.socket
    ```

### Testing Socket Activation

31. Test the socket activation mechanism:
    ```bash
    sudo systemctl status gunicorn
    ```

32. Send a connection to the socket through curl:
    ```bash
    curl --unix-socket /run/gunicorn.sock localhost
    ```

### Configuring Nginx to Proxy Pass to Gunicorn

33. Create and open a new server block in Nginx's sites-available directory:
    ```bash
    sudo nano /etc/nginx/sites-available/myproject
    ```

34. Configure the server block with appropriate settings.

35. Enable the server block:
    ```bash
    sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
    ```

36. Test Nginx configuration for syntax errors:
    ```bash
    sudo nginx -t
    ```

37. Restart Nginx:
    ```bash
    sudo systemctl restart nginx
    ```

38. Open firewall to normal traffic on port 80:
    ```bash
    sudo ufw delete allow 8000
    sudo ufw allow 'Nginx Full'
    ```

### Conclusion

You should now be able to access your Django application via your server's domain or IP address.
