# استخدم صورة Python المناسبة
FROM python:3.8-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى داخل الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تعيين المنفذ الذي سيتم استخدامه
EXPOSE 8000

# أمر التشغيل لتشغيل FastAPI باستخدام gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--bind", "0.0.0.0:8000"]
