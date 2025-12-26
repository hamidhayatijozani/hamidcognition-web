# 🧠 HamidCognition Platform

پلتفرم زنده و هوشمند برای تحلیل و پیش‌بینی بازار فارکس با استفاده از موتور شناختی P/S/T.

## ویژگی‌ها

- **موتور شناختی واقعی**: مبتنی بر معماری P/S/T (Power/Synchronicity/Tenacity)
- **داده‌های زنده**: دریافت قیمت لحظه‌ای EUR/USD از طریق yfinance
- **پیش‌بینی هوشمند**: پیش‌بینی قیمت برای ۵، ۱۰ و ۱۵ دقیقه آینده
- **داشبورد تعاملی**: رابط کاربری زیبا و زنده با به‌روزرسانی خودکار
- **تحلیل فازی**: نمایش وضعیت شناختی (RUPTURE_IMMINENT, SYNTHESIS_PEAK, UNSTABLE_CREATIVITY)

## نصب و اجرا

### روش ۱: اجرای محلی

```bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای برنامه
python app.py
```

سپس به آدرس `http://127.0.0.1:5000` بروید.

### روش ۲: Deploy روی Diploi

1. این repo را fork کنید یا clone کنید
2. به [diploi.com](https://diploi.com) بروید و با GitHub وارد شوید
3. یک پروژه جدید بسازید و Flask stack را انتخاب کنید
4. این repository را متصل کنید
5. Diploi به صورت خودکار پروژه را build و deploy می‌کند

### روش ۳: Deploy روی Render.com

1. به [render.com](https://render.com) بروید
2. New → Web Service را انتخاب کنید
3. این repository را متصل کنید
4. تنظیمات:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

### روش ۴: Deploy روی Railway.app

1. به [railway.app](https://railway.app) بروید
2. New Project → Deploy from GitHub را انتخاب کنید
3. این repository را انتخاب کنید
4. Railway به صورت خودکار تنظیمات را تشخیص می‌دهد

## ساختار پروژه

```
hamidcognition-web/
├── app.py                  # سرور اصلی Flask + موتور شناختی
├── templates/
│   └── dashboard.html      # داشبورد تعاملی
├── static/                 # فایل‌های استاتیک (در صورت نیاز)
├── requirements.txt        # وابستگی‌های پایتون
└── README.md              # این فایل
```

## معماری موتور شناختی

موتور HamidCognition بر اساس سه پارامتر اصلی کار می‌کند:

- **P (Power/Penetration)**: قدرت نفوذ و تأثیرگذاری
- **S (Synchronicity/Sensitivity)**: همزمانی و حساسیت به تغییرات
- **T (Tenacity/Stability)**: پایداری و مقاومت در برابر تغییرات

این پارامترها با توجه به فشار بازار (pressure) و نوآوری (novelty) به‌روزرسانی می‌شوند و فازهای مختلف شناختی را تولید می‌کنند.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## توسعه‌دهنده

ساخته شده توسط **Hamid** با ❤️
