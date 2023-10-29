# آموزش اجرای سرور بات تلگرام 
در این سند قصد داریم که سرور بات تلگرام را به  صورت لوکال بالا بیاوریم. توجه داشته باشید که شما می توانید از سرور های پیشفرض تلگرام به آدرس **api.telegram.org** استفاده کنید اما اگر قصد دارید که از قابلیت های ویژه مانند اتصال webhook لوکال استفاده نیاز به این سند دارید.
[کاربرد های سرور لوکال تلگرام](https://github.com/tdlib/telegram-bot-api#usage)

**این آموزش فقط برای سیستم های بر پایه Ubuntu 22.04 تست شده است**

## مرحله اول: نصب وابستگی ها
یک سری نرم افزار ها و پکیج ها را باید قبل از اجرای سرور نصب کرد
**اوپن اس اس ال - Open SSL**

	sudo apt-get install libssl-dev

**کامپایلر سی پلاس پلاس نسخه 14 ما از g++ 14 استفاده خواهیم کرد**

    sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    sudo apt update
    sudo apt install g++

**زی لیب - zlib**

	sudo apt install zlib1g

**جی پرف - gperf**

	sudo apt install gperf

**سی میک - cmake**

	sudo apt install cmake

## مرحله دوم: نصب
برای نصب دستورات زیر را در ترمینال وارد کنید

	git clone --recursive https://github.com/tdlib/telegram-bot-api.git
    cd telegram-bot-api
    mkdir build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release ..
    cmake --build . --target install

```
