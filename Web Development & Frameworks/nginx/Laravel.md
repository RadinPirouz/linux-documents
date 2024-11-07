
# Deploying a Laravel Application on Nginx

This guide covers the steps to deploy a Laravel application on an Nginx web server. You’ll configure Nginx, install PHP and required extensions, set up Composer, and secure your Laravel application.

---

## Prerequisites

- **A Linux server** with root or sudo privileges.
- **Nginx installed** or installation instructions are provided below.
- **PHP and required extensions** for running Laravel applications.
- **Composer installed** for managing Laravel dependencies.
  
---

## Step 1: Install Nginx

1. **Update the package list**:
   ```bash
   sudo apt update
   ```

2. **Install Nginx**:
   ```bash
   sudo apt install nginx
   ```

---

## Step 2: Configure Nginx for Laravel

1. **Open the default Nginx configuration file**:
   ```bash
   sudo nano /etc/nginx/sites-available/default
   ```

2. **Replace the existing content** with the following configuration. Make sure to replace `your_domain.com` with your domain or server’s IP address.

   ```nginx
   server {
       listen 80;
       server_name your_domain.com;
       root /var/www/html/your_laravel_project/public;

       index index.php index.html index.htm;

       location / {
           try_files $uri $uri/ /index.php?$query_string;
       }

       location ~ \.php$ {
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;  # Adjust PHP version if necessary
       }

       location ~ /\.ht {
           deny all;
       }
   }
   ```

3. **Save and close the file**.

4. **Test the Nginx configuration** for syntax errors:
   ```bash
   sudo nginx -t
   ```

5. **Restart Nginx** to apply the new configuration:
   ```bash
   sudo systemctl restart nginx
   ```

---

## Step 3: Install PHP and Required Extensions

1. **Add the PHP PPA repository**:
   ```bash
   sudo add-apt-repository ppa:ondrej/php
   sudo apt update
   ```

2. **Install PHP and required extensions** for Laravel:
   ```bash
   sudo apt install php7.4-fpm php7.4-mbstring php7.4-xml php7.4-zip php7.4-mysql php7.4-curl php7.4-gd
   ```

---

## Step 4: Install Composer

1. **Download and install Composer globally**:
   ```bash
   curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
   ```

---

## Step 5: Deploy the Laravel Application

1. **Clone or upload your Laravel project** to the Nginx web root:
   ```bash
   sudo mkdir -p /var/www/html/your_laravel_project
   # Clone or upload your project files here
   ```

2. **Set appropriate permissions** for the Laravel `storage` and `bootstrap/cache` directories:
   ```bash
   cd /var/www/html/your_laravel_project
   sudo chown -R www-data:www-data storage bootstrap/cache
   sudo chmod -R 775 storage bootstrap/cache
   ```

3. **Install Laravel dependencies** with Composer:
   ```bash
   cd /var/www/html/your_laravel_project
   composer install --no-dev --optimize-autoloader
   ```

4. **Generate an application key** for Laravel:
   ```bash
   php artisan key:generate
   ```

---

## Step 6: Restart PHP-FPM

Restart PHP-FPM to apply any changes:
```bash
sudo systemctl restart php7.4-fpm  # Adjust PHP version as needed
```

---

## Summary and Final Checks

Your Laravel application should now be deployed and accessible through Nginx. Visit `http://your_domain.com` in a browser to confirm that the application is working.

---

## Additional Notes

- **Security**: Ensure the `APP_ENV` in your `.env` file is set to `production` for live applications.
- **Permissions**: For added security, periodically review file and folder permissions, particularly within the `storage` and `bootstrap/cache` directories.
- **SSL/TLS**: For a production environment, set up SSL using [Certbot](https://certbot.eff.org/) for secure HTTPS access.

This guide provides the foundational steps to deploy a Laravel application on Nginx. Customize configurations further as per your project requirements.

## Author
[alinuxist](https://github.com/alinuxist)
