جمع‌آوری اطلاعات سیستم با استفاده از Django و Django Rest Framework
مقدمه
در این پروژه، از Django و Django Rest Framework استفاده شده‌است تا اطلاعاتی از سیستم مانند CPU، حافظه و ... جمع‌آوری شود.

راه‌اندازی
نصب مورد نیازها
برای نصب وابستگی‌های مورد نیاز:

bash
Copy code
pip install -r requirements.txt
راه‌اندازی دیتابیس
برای مهاجرت دیتابیس، دستورات زیر را اجرا کنید:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
اجرای سرور
برای اجرای سرور توسط Django:

bash
Copy code
python manage.py runserver
API ها
دریافت اطلاعات CPU

URL: /api/cpu_info/
روش: GET
خروجی: اطلاعات مربوط به CPU
دریافت اطلاعات حافظه

URL: /api/memory_info/
روش: GET
خروجی: اطلاعات مربوط به حافظه
... (و همین طور برای سایر API ها)

جمع‌بندی
این پروژه به شما امکان می‌دهد تا با استفاده از یک وب API ساده، اطلاعات مختلف سیستم را مشاهده کنید.

