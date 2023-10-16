
# <div dir="rtl">آموزشDeploy Dotnet روی لینوکس</div>
این آموزش فقط روی دات نت ۷ و اوبونتو ۲۲.۰۴ تست شده است

## <div dir="rtl"> خروجی گرفتن</div>

<div dir="rtl">
 نخست دات نت را نصب کنیم 
</div>

    sudo apt install dotnet-sdk-7.0
<div dir="rtl">
<b>نکته:  می توانید با دستور  dotnet new mvc پروژه دات نت بسازید </b>
</div>
<br>
<div dir="rtl">
 سپس باید از پروژه خود خروجی بگیریم پس دستور زیر را اجرا کنید 
</div>

    dotnet publish

<div dir="rtl">
مکان خروجی فایل بعد از اتمام دستور به شما نشان داده خواهد شد معمولا خروجی پروژه در مکان زیر قرار خواهد گرفت  
</div>

**bin/Debug/net7.0/publish**

## <div dir="rtl"> نصب Ngnix</div>
<div dir="rtl">
اِنجین‌اِکس (به انگلیسی: nginx) یک کارساز وب با حجم پایین و کارایی بالا است که تحت مجوز بی‌اس‌دی منتشر می‌شود. این کارساز وب در یونیکس، گنو/لینوکس، بی‌اس‌دی، مک او اس و ویندوز اجرا می‌شود. بر طبق گفتهٔ نت‌کرافت، در حال 
حاضر ۱۲٫۰۷٪ از دامنه‌های اینترنت از این کارساز استفاده می‌کنند.
</div>
<br/>
<div dir="rtl">
<b>برای نصب Ngnix از طریق apt از دستور زیر استفاده کنید
</b>
</div>

    sudo apt install ngnix

<div dir="rtl">
سپس با استفاده از دستور  sudo ufw disable  فایروال را غیرفعال کنید
اگر با این دستور با خطا مواجه شد یعنی شما فایروال ندارد پس از روی این بخش رد شوید

</div>
<br>
<div dir="rtl">
اگر نصب موفقیت آمیز بوده باشد با تایپ کردن localhost در مرورگر باید با پیام Welcome to Ngnix مواجه شوید
</div>

## <div dir="rtl"> تنظیمات Ngnix</div>
<div dir="rtl">
با دستور زیر یک پوشه برای سایت خود می سازیم
</div>

    sudo mkdir /var/www/app1 


<div dir="rtl">
محتویات پوشه publish را به پوشه ای که ساختیم کپی کنید
</div>

    sudo cp yourprojectFolder/bin/Debug/net7.0/publish /var/www/app1

<br>

<div dir="rtl">
سپس با دستور زیر وارد کانفیگ Ngnix می شویم
</div>

    sudo vim /etc/nginx/sites-available/default

<div dir="rtl">
و محتویات داخل فایل را با زیر عوض می کنیم
</div>

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

<div dir="rtl">
<b>نکته: به جای example.com آدرس سایت خود را بگذارید
</b>
</div>
<br>
<div dir="rtl">
با دستور زیر محتویات فایلی را که تغییر دادیم را بررسی کنید
</div>

    sudo ngnix -t

<br>
<div dir="rtl">
اگر با خطا مواجه نشدید دستور زیر را فراخوانی کنید تا تنظیمات Ngnix دوباره بارگذاری شود
</div>

    sudo ngnix -s reload

## <div dir="rtl"> افزودن سایت به عنوان سرویس</div>
<div dir="rtl">
با دستور زیر فایلی برای سرویس خود درست می کنیم</div>

    sudo vim /etc/systemd/system/app1.service

<br>

  <div dir="rtl">
کد زیر در فایل بالا کپی کنید
</div>

    [Unit] 
    Description= dotnet webapp
    [Service] 
    WorkingDirectory=/var/www/app1
    ExecStart=/usr/bin/dotnet /var/www/app/projectname.dll 
    Restart=always
    RestartSec=10
    SyslogIdentifier=projectname
    Environment=ASPNETCORE_ENVIRONMENT=Production
    
    [Install]
    WantedBy=multi-user.target

<div dir="rtl">
<b>
نکته: به جای projectname اسم پروژه خود را بگذارید
</b>
</div>
<br>
<div dir="rtl">
با دستور های زیر سایت را فعال کنید و از وضعیت آن مطلع شوید
</div>

    sudo systemctl enable app1.service
    sudo systemctl start app1.service
    sudo systemctl status app1.service



