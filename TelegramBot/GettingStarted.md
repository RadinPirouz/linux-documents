# کد نویسی برای بات تلگرام
ربات **تلگرام** (**telegram** bot) یک نوع حساب کاربری ویژه در **تلگرام** است که به صورت اتوماتیک پیام ها را ارسال و دریافت می نماید . کاربران از طریق ارسال دستورات گوناگون با ربات ها در ارتباط هستند و امکان مدیریت ربات ها از طریق API **تلگرام** و درخواست های HTTPS وجود دارد . عبارت bot برای ربات ها نمایش داده می شود.

## ساخت بات با BotFather
اولین مرحله برای کد نویسی بات تلگرام ساختن بات است. از طریق [BotFather](https://telegram.me/BotFather) بات را خواهیم ساخت. پیام `start/` را در BotFather وارد کنید سپس روی **newbot - create a new bot/** کلیک کنید. بعد از مشاهده پیام **Alright, a new bot. How are we going to call it? Please choose a name for your bot.** یک اسم برای بات خود وارد کنید. 
سپس بعد از مشاهده پیام **Good. Now let's choose a username for your bot. It must end in bot. Like this, for example: TetrisBot or tetris_bot.** یک نام **خاص و Unique انگلیسی** که حتما در آخرش کلمه **bot** را دارد وارد کنید.

زمانی که بات شما ساخته شد توکن بات را که زیر **Use this token to access the HTTP API** قرار دارد را کپی کنید و در محل امنی قرار دهید.

## آماده سازی محیط کد نویسی
به طور کلی از دو روش می توان برای بات های تلگرام برنامه نویسی کرد. 
**روش اول: استفاده از Rest API رسمی تلگرام که نحوه استفاده از در سایت core.telegram.org/bots/api قابل دسترس است**
**روش دوم: استفاده از پکیج هایی که کد های پایه بات را برای زبان برنامه نویسی مورد نظر شما ساخته اند**
برخی از این پکیج های عبارت اند از:
برای سی شارپ ([Telegram.Bot](https://www.nuget.org/packages/Telegram.Bot)) 
	این پکیج از طریق کامند زیر در **Dotnet CLI** نصب می شود

	dotnet add package Telegram.Bot --version 19.0.0

برای پایتون ( [python-telegram-bot](https://pypi.org/project/python-telegram-bot/2.4/))
این پکیج نیز از طریق کامند زیر قابل نصب است

    pip install python-telegram-bot==2.4

برای اینکه این آموزش بر Core و Universal بودن تاکید دارد ما از از طریق روش اول برای بات خود کد نویسی هر چند این روش کمی سخت تر است اما اگر به خوبی این روش را یادبگرید خود می توانید کتابخانه مانند دو نمونه بالا بنوسید

## کد نویسی برای بات
پروژه ای با زبان مورد نظر خود ایجاد کنید و کتابخانه هایی مورد نیاز برای **Rest API** را روی پروژه نصب یا Import کنید. 
برای مثال اگر از زبان برنامه نویسی سی شارپ استفاده می کنید باید **RestSharp** را نصب کنید و نحوه کار با آن را بلد باشید و اگر از پایتون استفاده می کنید باید کتابخانه **Request** را نصب و Import کنید.

**قبل از شروع به این نکات درباره API تلگرام توجه کنید.**

+ تلگرام به حروف بزرگ و کوچک در API حساس است
+ تلگرام فقط از **POST** و **GET** پشتیبانی می کند
+ همه درخواست ها باید کاملا با **UTF-8** باشند
+ تلگرام از هر 4 روش رایج ارسال درخواست **(application/json, multipart/form-data ,QueryString, application/x-www-form-urlencoded)** پشتیبانی می کند
**پیشنهاد:** من به شما پیشنهاد می کنم از QueryString یا application/json استفاده کنید.

### روش QueryString چیست؟
در این روش پارامتر های تابع که می خواهیم اجرا کنیم به عنوان QueryString در Url گذاشته می شوند مانند:

	https://test.ir/APIFunction?param1=inp1&param2=inp2

همانطور که در مثال بالا آشکار است هر چه بعد از **?** قرا ر می گیرد **Query String** است. 
پارامتر 1 یا **param1** اسم متغیر اول ماست و **inp1** ورودی متغیر **param1** است.
سپس پارامتر های ورودی با علامت **&** جدا شده اند. و پارمتر دوم یا **param2** و ورود آن قرار گرفته است.

### روش application/json
در این روش Url فقط به آدرس تابع اشاره دارد نه به ورود های آن مانند:

    https://test.ir/APIFunction

   در این روش پارامتر ها به عنوان Json در بدنه ارسال می شوند. مانند زیر 

    {
        "Body":{
            "param1":"inp1",
            "param2":"inp2",
    },

البته ارسال بدنه با توجه به کتابخانه که برای API استفاده می کنید. متفاوت مثلا برای **RestSharp** از Request.AddBody باید استفاده کنید.

## استاندارد های استفاده از API تلگرام
**آدرس پایه API:** 

    https://api.telegram.org/bot<token>/<FuncName>

**توکن:** به جای **<token>** توکنی را که از بات فادر گرفتید قرار دهید
**نام تابع:** تابعی که می خواهید فراخوانی کنید را به جای **<Funcname>** قرار دهید

**موفق بودن یا نا موفق بودن درخواست**
اگر درخواست شما **موفقیت آمیز** باشد با **OK:True**  مواجه می شوید و جواب درخواست را به عنوان **Result** به شما برگردانده می شود
**مثال:**

	{
	"ok":true,
	"result":[]
	}

اگر درخواست شما **ناموفق** باشد. **OK: False** می شود و شما پارامتر به عنوان **Result** نخواهید داشت همچنین **error_code** و **description** را به ترتیب برای شماره خطا و توصیف خطا دریافت خواهید کرد. 
**مثال: **

	{
	"ok":false,
	"error_code":404,
	"description":"Not Found" 
	}

**بروزرسانی بات:**
هر بار که پیامی برای بات ارسال می شود را می توان با **getUpdate** بدست آورد. برای بدست آوردن لیست آپدیت می توانید Url زیر را GET کنید

	https://api.telegram.org/bot<token>/getUpdates

این درخواست لیستی از Update ها بر می گرداند. 
برای مشاهده شئ Update به https://core.telegram.org/bots/api#update مراجعه کنید

**دریافت اطلاعات کلی بات:**
برای دریافت اطلاعات کلی از آدرس زیر استفاده کنید

    https://api.telegram.org/bot<token>/getMe

**جواب:**

    {
      "ok": true,
      "result": {
        "id": 6775339167,
        "is_bot": true,
        "first_name": "ForDocumentPack",
        "username": "ForDocumentPackBot",
        "can_join_groups": true,
        "can_read_all_group_messages": false,
        "supports_inline_queries": false
      }
    }

## ساخت پروژه ساده
می خواهیم یک پروژه کد نویسی کنیم که زمانی که بات روشن می شود یک پیام خوش آمد گویی ارسال کند.
برای این کار از طریق تابع **getUpdates** پیام هایی که بات داده شده است را مشاهده می کنیم مانند زیر:

	{
      "ok": true,
      "result": [
        {
          "update_id": 529754041,
          "message": {
            "message_id": 1,
            "from": {
              "id": 407692495,
              "is_bot": false,
              "first_name": "Mahdiyar",
              "last_name": "Abdollahi",
              "username": "Mdr_abdollahi",
              "language_code": "en"
            },
            "chat": {
              "id": 407692495,
              "first_name": "Mahdiyar",
              "last_name": "Abdollahi",
              "username": "Mdr_abdollahi",
              "type": "private"
            },
            "date": 1697995311,
            "text": "/start",
            "entities": [
              {
                "offset": 0,
                "length": 6,
                "type": "bot_command"
              }
            ]
          }
        }
      ]
    }

**نکته: get_updates را در حلقه بی نهایت بی اندازید تا همیشه بروزرسانی شود**
**نکته: بررسی کنید تا به کسانی که به آنها پاسخ داده اید دوباره پاسخ ندهید.**
**نکته: اگر به جای getUpdates از** [WebHooks](https://core.telegram.org/bots/api#getting-updates) **استفاده کنید نیاز به بررسی پاسخ های تکراری نیست**

برای ارسال پیام نیاز به **chat_id** داریم.

	result => message => chat => id

بعد از دریافت **chat_id** می توانیم با تابع **sendMessage** پیام برای کاربر ارسال کنید. 

	https://api.telegram.org/bot<token>/sendMessage

**نکته: حتما باید پارامتر chat_id و text ارسال شود**
**نکته: حتما باید بصورت POST ارسال شود و پارامتر ها به صورت application/json باشد**

شما می توانید تمامی تابع های API تلگرام را از سایت تلگرام مشاهده کنید -> https://core.telegram.org/bots/api
