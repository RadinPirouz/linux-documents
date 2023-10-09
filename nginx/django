****installing the packages from the ubuntu repositories****

1.at first update your ubuntu:
$ sudo apt update

2.then install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl:
$ sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl

****Creating the PostgreSQL Database and User****

3.Log into an interactive Postgres session by typing:
$ sudo -u postgres psql

4.You will be given a PostgreSQL prompt where you can set up our requirements.
First, create a database for your project:
CREATE DATABASE myproject;

Next, create a database user for our project. Make sure to select a secure password:
CREATE USER myprojectuser WITH PASSWORD 'password';

5.Afterwards, you’ll modify a few of the connection parameters for the user that you just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

6.You will set the default character encoding to UTF-8, which Django expects. You are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, you are setting the timezone. By default, Django projects will be set to use UTC.do it:
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';

7.Now, you can give the new user access to administer the new database:
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

8.When you are finished, exit out of the PostgreSQL prompt by typing:
\q

****Creating a python virtual environment for your project****

8.First, create and change into a directory where your can keep your project files:
$ mkdir ~/myprojectdir
$ cd ~/myprojectdir

9.Within the project directory, create a Python virtual environment by typing:
$ python3 -m venv myprojectenv

10.Before installing your project’s Python requirements, you will need to activate the virtual environment. You can do that by typing:
$ source myprojectenv/bin/activate

when you enter this command your terminal be likes:
(myprojectenv) $ ..........................

11.With your virtual environment active, install Django, Gunicorn, and the psycopg2 PostgreSQL adaptor with the local instance of pip:
(myprojectenv) $ pip install django gunicorn psycopg2-binary

****Creating and Configuring a new django project****

12.the key to this is that you are defining the directory explicitly instead of allowing Django to make decisions relative to our current directory:
$ django-admin startproject myproject ~/myprojectdir

13.The first thing you should do with your newly created project files is adjust the settings. Open the settings file in your text editor:
$ nano ~/myprojectdir/myproject/settings.py

14.change ALLOWED_HOSTS =[] to ALLOWED_HOSTS =[*]

15.and change DATABASES = {} to DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

16.and type:
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
on settings.py

17.save and exit

18.Now, you can migrate the initial database schema to our PostgreSQL database using the management script:
(myprojectenv) $ ~/myprojectdir/manage.py makemigrations
(myprojectenv) $ ~/myprojectdir/manage.py migrate

19.Create an administrative user for the project by typing:
(myprojectenv) $ ~/myprojectdir/manage.py createsuperuser

20.You will have to select a username, provide an email address, and choose and confirm a password.

21.You can collect all of the static content into the directory location that you configured by typing:
(myprojectenv) $ ~/myprojectdir/manage.py collectstatic

22.Create an exception for port 8000 by typing:
(myprojectenv) $ sudo ufw allow 8000

23.Finally, you can test out your project by starting up the Django development server with this command:
(myprojectenv) $ ~/myprojectdir/manage.py runserver 0.0.0.0:8000

24.In your web browser, visit your server’s domain name or IP address followed by :8000:
http://server_domain_or_IP:8000

You should receive the default Django index page

If you append /admin to the end of the URL in the address bar, you will be prompted for the administrative username and password you created with the createsuperuser command

After authenticating, you can access the default Django admin interface

When you are finished exploring, hit CTRL-C in the terminal window to shut down the development server.

25.to stop apache2.service type:
sudo /etc/init.d/apache2 restart

26.The last thing you need to do before leaving your virtual environment is test Gunicorn to make sure that it can serve the application.

27.You can do this by entering the project directory and using gunicorn to load the project’s WSGI module:
(myprojectenv) $ cd ~/myprojectdir
(myprojectenv) $ gunicorn --bind 0.0.0.0:8000 myproject.wsgi

28.This will start Gunicorn on the same interface that the Django development server was running on. You can go back and test the app again in your browser.
29.When you are finished testing, hit CTRL-C in the terminal window to stop Gunicorn.

30.You’re now finished configuring your Django application. You can back out of our virtual environment by typing:
(myprojectenv) $ deactivate

31.The virtual environment indicator in your prompt will be removed.

****Creating systemd Socket and service files for gunicorn****

32.Start by creating and opening a systemd socket file for Gunicorn with sudo privileges:
$ sudo nano /etc/systemd/system/gunicorn.socket

33.inside, you will create a [Unit] section to describe the socket, a [Socket] section to define the socket location, and an [Install] section to make sure the socket is created at the right time:
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
34.Save and close the file when you are finished.
35.Next, create and open a systemd service file for Gunicorn with sudo privileges in your text editor. The service filename should match the socket filename with the exception of the extension:
sudo nano /etc/systemd/system/gunicorn.service
36.type this on gunicorn.service:
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=fb
Group=www-data
WorkingDirectory=/home/fb/myprojectdir
ExecStart=/home/fb/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target
37.With that, your systemd service file is complete. Save and close it now.
38.You can now start and enable the Gunicorn socket. This will create the socket file at /run/gunicorn.sock now and at boot. When a connection is made to that socket, systemd will automatically start the gunicorn.service to handle it:
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket

****Checking for the Gunicorn socket file****

39.Check the status of the process to find out whether it was able to start:
$ sudo systemctl status gunicorn.socket

40.You should receive an output like this:

Output
● gunicorn.socket - gunicorn socket
     Loaded: loaded (/etc/systemd/system/gunicorn.socket; enabled; vendor preset: enabled)
     Active: active (listening) since Mon 2022-04-18 17:53:25 UTC; 5s ago
   Triggers: ● gunicorn.service
     Listen: /run/gunicorn.sock (Stream)
     CGroup: /system.slice/gunicorn.socket

oct 9 10:53:25 django systemd[1]: Listening on gunicorn socket.

41.Next, check for the existence of the gunicorn.sock file within the /run directory:
$ file /run/gunicorn.sock

Output
/run/gunicorn.sock: socket

42.If the systemctl status command indicated that an error occurred or if you do not find the gunicorn.sock file in the directory, it’s an indication that the Gunicorn socket was not able to be created correctly. Check the Gunicorn socket’s logs by typing:
$ sudo journalctl -u gunicorn.socket

****Testing Socket Activation****

43.Currently, if you’ve only started the gunicorn.socket unit, the gunicorn.service will not be active yet since the socket has not yet received any connections. You can check this by typing:
$ sudo systemctl status gunicorn

Output
○ gunicorn.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: ● gunicorn.socket

44.To test the socket activation mechanism, you can send a connection to the socket through curl by typing:
$ curl --unix-socket /run/gunicorn.sock localhost

45.You should receive the HTML output from your application in the terminal. This indicates that Gunicorn was started and was able to serve your Django application. You can verify that the Gunicorn service is running by typing:
$ sudo systemctl status gunicorn

Output
● gunicorn.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-04-18 17:54:49 UTC; 5s ago
TriggeredBy: ● gunicorn.socket
   Main PID: 102674 (gunicorn)
      Tasks: 4 (limit: 4665)
     Memory: 94.2M
        CPU: 885ms
     CGroup: /system.slice/gunicorn.service
             ├─102674 /home/fb/myprojectdir/myprojectenv/bin/python3 /home/sammy/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
             ├─102675 /home/fb/myprojectdir/myprojectenv/bin/python3 /home/sammy/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
             ├─102676 /home/fb/myprojectdir/myprojectenv/bin/python3 /home/sammy/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
             └─102677 /home/fb/myprojectdir/myprojectenv/bin/python3 /home/sammy/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application

Oct 3 9:54:49 django systemd[1]: Started gunicorn daemon.
Oct 3 9:54:49 django gunicorn[102674]: [2022-04-18 17:54:49 +0000] [102674] [INFO] Starting gunicorn 20.1.0
Oct 3 9:54:49 django gunicorn[102674]: [2022-04-18 17:54:49 +0000] [102674] [INFO] Listening at: unix:/run/gunicorn.sock (102674)
Oct 3 9:54:49 django gunicorn[102674]: [2022-04-18 17:54:49 +0000] [102674] [INFO] Using worker: sync
Oct 3 9:54:49 django gunicorn[102675]: [2022-04-18 17:54:49 +0000] [102675] [INFO] Booting worker with pid: 102675
Oct 3 9:54:49 django gunicorn[102676]: [2022-04-18 17:54:49 +0000] [102676] [INFO] Booting worker with pid: 102676
Oct 3 9:54:50 django gunicorn[102677]: [2022-04-18 17:54:50 +0000] [102677] [INFO] Booting worker with pid: 102677
Oct 3 9:54:50 django gunicorn[102675]:  - - [18/Apr/2022:17:54:50 +0000] "GET / HTTP/1.1" 200 10697 "-" "curl/7.81.0"

46.If the output from curl or the output of systemctl status indicates that a problem occurred, check the logs for additional details:
$ sudo journalctl -u gunicorn

47.Check your /etc/systemd/system/gunicorn.service file for problems. If you make changes to the /etc/systemd/system/gunicorn.service file, reload the daemon to reread the service definition and restart the Gunicorn process by typing:
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn

48.Make sure you troubleshoot the above issues before continuing.

****Configure Nginx to proxy oass to gunicorn****

49.Start by creating and opening a new server block in Nginx’s sites-available directory:
$ sudo nano /etc/nginx/sites-available/myproject

50.Inside, open up a new server block. You will start by specifying that this block should listen on the normal port 80 and that it should respond to your server’s domain name or IP address:

server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/fb/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

51.Save and close the file when you are finished. Now, you can enable the file by linking it to the sites-enabled directory:
$ sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled

52.Test your Nginx configuration for syntax errors by typing:
$ sudo nginx -t

53.If no errors are reported, go ahead and restart Nginx by typing
$ sudo systemctl restart nginx

54.Finally, you need to open up your firewall to normal traffic on port 80. Since you no longer need access to the development server, you can remove the rule to open port 8000 as well:
$ sudo ufw delete allow 8000
$ sudo ufw allow 'Nginx Full'

55.You should now be able to go to your server’s domain or IP address to view your application.
