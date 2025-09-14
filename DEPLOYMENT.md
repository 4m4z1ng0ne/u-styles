# Инструкции по развертыванию U-Styles

## 🚀 Быстрый старт

### 1. Клонирование и настройка

```bash
git clone https://github.com/yourusername/u-styles.git
cd u-styles
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirments.txt
```

### 4. Настройка переменных окружения

Создайте файл `.env` в корне проекта на основе `env.example`:

```bash
cp env.example .env
```

Заполните `.env` файл своими данными:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

# Email Settings (замените на свои данные)
EMAIL_HOST_USER=your-email@yandex.ru
EMAIL_HOST_PASSWORD=your-email-password

# OAuth Settings (опционально)
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 5. Применение миграций

```bash
python manage.py migrate
```

### 6. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 7. Загрузка тестовых данных (опционально)

```bash
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/product.json
```

### 8. Запуск сервера

```bash
python manage.py runserver
```

## 🔧 Настройка для продакшена

### 1. Настройка базы данных PostgreSQL

Установите PostgreSQL и создайте базу данных:

```sql
CREATE DATABASE u_styles;
CREATE USER u_styles_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE u_styles TO u_styles_user;
```

Обновите `.env`:

```env
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=u_styles
DATABASE_USER=u_styles_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 2. Настройка Redis (опционально)

Установите Redis:

```bash
# Ubuntu/Debian
sudo apt-get install redis-server

# Windows
# Скачайте Redis с официального сайта
```

Обновите `.env`:

```env
REDIS_URL=redis://127.0.0.1:6379/1
```

Раскомментируйте настройки кэширования в `store/settings.py`.

### 3. Настройка статических файлов

```bash
python manage.py collectstatic
```

### 4. Настройка безопасности

Обновите `.env` для продакшена:

```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-production-secret-key
```

### 5. Настройка веб-сервера (Nginx + Gunicorn)

Установите Gunicorn:

```bash
pip install gunicorn
```

Создайте файл `gunicorn.conf.py`:

```python
bind = "127.0.0.1:8000"
workers = 3
user = "www-data"
group = "www-data"
daemon = True
pidfile = "/var/run/gunicorn.pid"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
```

Настройте Nginx:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/project;
    }

    location /media/ {
        root /path/to/your/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## 🔐 Настройка OAuth

### GitHub OAuth

1. Перейдите в GitHub Settings > Developer settings > OAuth Apps
2. Создайте новое приложение
3. Укажите Authorization callback URL: `http://yourdomain.com/accounts/github/login/callback/`
4. Скопируйте Client ID и Client Secret в `.env`

### Google OAuth

1. Перейдите в Google Cloud Console
2. Создайте новый проект или выберите существующий
3. Включите Google+ API
4. Создайте OAuth 2.0 credentials
5. Укажите Authorized redirect URIs: `http://yourdomain.com/accounts/google/login/callback/`
6. Скопируйте Client ID и Client Secret в `.env`

## 📧 Настройка email

### Yandex SMTP

1. Включите двухфакторную аутентификацию
2. Создайте пароль приложения
3. Используйте этот пароль в `EMAIL_HOST_PASSWORD`

### Другие SMTP провайдеры

Обновите настройки в `.env`:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_SSL=False
EMAIL_USE_TLS=True
```

## 🐳 Docker (опционально)

Создайте `Dockerfile`:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY . .
CMD ["gunicorn", "store.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Создайте `docker-compose.yml`:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: u_styles
      POSTGRES_USER: u_styles_user
      POSTGRES_PASSWORD: your_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:6-alpine

volumes:
  postgres_data:
```

Запуск:

```bash
docker-compose up -d
```

## 🔍 Мониторинг и логи

### Настройка логирования

Добавьте в `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

## ✅ Проверка развертывания

1. Проверьте доступность сайта
2. Протестируйте регистрацию пользователя
3. Проверьте отправку email
4. Протестируйте создание заказа
5. Проверьте админ-панель

## 🆘 Решение проблем

### Ошибка подключения к базе данных

- Проверьте настройки в `.env`
- Убедитесь, что PostgreSQL запущен
- Проверьте права доступа пользователя

### Ошибки статических файлов

- Выполните `python manage.py collectstatic`
- Проверьте настройки `STATIC_ROOT` и `STATIC_URL`
- Убедитесь, что Nginx правильно настроен

### Проблемы с email

- Проверьте настройки SMTP в `.env`
- Убедитесь, что пароль приложения правильный
- Проверьте настройки файрвола

---

**Удачного развертывания!** 🚀
