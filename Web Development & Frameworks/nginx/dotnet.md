# Deploying .NET on Linux

This tutorial has been tested only on .NET 7 and Ubuntu 22.04.

## Getting the Output

First, let's install .NET:
```bash
sudo apt install dotnet-sdk-7.0
```
*Note: You can create a .NET project using `dotnet new mvc` command.*

Then, we need to publish our project:
```bash
dotnet publish
```
The location of the output file will be displayed after the command finishes. Typically, the project output will be placed in:
**bin/Debug/net7.0/publish**

## Installing Nginx

**Nginx** is a high-performance web server with low resource usage, distributed under the terms of the BSD license. It runs on Unix-like operating systems and is widely used, currently powering 12.07% of the internet's domains.

To install **Nginx** via `apt`, use the following command:
```bash
sudo apt install nginx
```

Then, disable the firewall with:
```bash
sudo ufw disable
```
If you encounter an error with this command, it means you don't have a firewall. In that case, skip this part.

If the installation is successful, you should see "Welcome to Nginx" when typing `localhost` in your browser.

## Configuring Nginx

Create a directory for your site:
```bash
sudo mkdir /var/www/app1 
```

Copy the contents of the `publish` directory to the newly created directory:
```bash
sudo cp yourprojectFolder/bin/Debug/net7.0/publish /var/www/app1
```

Then, navigate to the Nginx configuration:
```bash
sudo vim /etc/nginx/sites-available/default
```

Replace the contents of the file with the following:
```nginx
server {
    listen        80;
    server_name   example.com *.example.com;
    location / {
        proxy_pass         http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection keep-alive;
        proxy_set_header   Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
```
*Note: Replace `example.com` with your site address.*

Check the configuration file syntax:
```bash
sudo nginx -t
```

If no errors are reported, reload Nginx to apply the changes:
```bash
sudo nginx -s reload
```

## Adding the Site as a Service

Create a service file for your site:
```bash
sudo vim /etc/systemd/system/app1.service
```

Copy the following code into the file:
```plaintext
[Unit] 
Description=dotnet webapp
[Service] 
WorkingDirectory=/var/www/app1
ExecStart=/usr/bin/dotnet /var/www/app/projectname.dll 
Restart=always
RestartSec=10
SyslogIdentifier=projectname
Environment=ASPNETCORE_ENVIRONMENT=Production
    
[Install]
WantedBy=multi-user.target
```
*Note: Replace `projectname` with your project's name.*

Enable and start the site, and check its status:
```bash
sudo systemctl enable app1.service
sudo systemctl start app1.service
sudo systemctl status app1.service
```
## Author
(Mahdiyar Abdollahi)[https://github.com/IAmMahdiyar]
