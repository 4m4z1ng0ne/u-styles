# U-Styles - Интернет-магазин одежды

Современный интернет-магазин одежды, построенный на Django с красивым и адаптивным интерфейсом.

## 🚀 Особенности

- **Каталог товаров** с фильтрацией по категориям и пагинацией
- **Система корзины** с добавлением/удалением товаров
- **Регистрация и авторизация** пользователей
- **Подтверждение email** при регистрации
- **Создание заказов** с переносом товаров из корзины
- **Профиль пользователя** с возможностью редактирования
- **OAuth авторизация** через GitHub и Google
- **Админ-панель** Django для управления
- **Адаптивный дизайн** с Bootstrap 5
- **Кэширование** для улучшения производительности

## 🛠️ Технологии

- **Backend:** Django 4.2.16
- **Frontend:** Bootstrap 5, FontAwesome
- **База данных:** SQLite (настроена для PostgreSQL)
- **Кэширование:** Redis (опционально)
- **Email:** SMTP через Yandex
- **OAuth:** django-allauth

## 📦 Установка

### 1. Клонирование репозитория

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

Скопируйте файл `env.example` в `.env` и заполните необходимые переменные:

```bash
cp env.example .env
```

Отредактируйте `.env` файл:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

# Email Settings
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

Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/

## 📁 Структура проекта

```
u-styles/
├── common/                 # Общие компоненты
├── media/                  # Медиафайлы (изображения)
├── orders/                 # Приложение заказов
│   ├── migrations/         # Миграции БД
│   ├── templates/          # Шаблоны заказов
│   ├── forms.py           # Формы заказов
│   ├── models.py          # Модели заказов
│   └── views.py           # Представления заказов
├── products/              # Приложение товаров
│   ├── fixtures/          # Тестовые данные
│   ├── migrations/        # Миграции БД
│   ├── templates/         # Шаблоны товаров
│   ├── models.py         # Модели товаров
│   └── views.py          # Представления товаров
├── static/               # Статические файлы (CSS, JS, изображения)
├── store/                # Основные настройки Django
│   ├── settings.py       # Настройки проекта
│   └── urls.py          # Главные URL-маршруты
├── users/                # Приложение пользователей
│   ├── migrations/       # Миграции БД
│   ├── templates/        # Шаблоны пользователей
│   ├── forms.py         # Формы пользователей
│   ├── models.py        # Модели пользователей
│   └── views.py         # Представления пользователей
├── .gitignore           # Игнорируемые файлы Git
├── env.example          # Пример переменных окружения
├── manage.py            # Управляющий скрипт Django
├── README.md            # Документация проекта
└── requirments.txt      # Зависимости Python
```

## 🔧 Настройка для продакшена

### 1. Настройка базы данных PostgreSQL

```env
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 2. Настройка Redis (опционально)

```env
REDIS_URL=redis://127.0.0.1:6379/1
```

Раскомментируйте настройки кэширования в `settings.py`.

### 3. Настройка статических файлов

```bash
python manage.py collectstatic
```

### 4. Настройка безопасности

- Установите `DEBUG=False` в `.env`
- Настройте `ALLOWED_HOSTS` для вашего домена
- Используйте HTTPS в продакшене

## 🎨 Интерфейс

- **Главная страница** с приветствием и переходом в каталог
- **Каталог товаров** с сеткой товаров и фильтрацией
- **Корзина** с возможностью изменения количества
- **Профиль пользователя** с редактированием данных
- **Страница заказов** с историей покупок
- **Админ-панель** для управления контентом

## 📱 Адаптивность

Проект полностью адаптивен и корректно отображается на:
- Десктопах
- Планшетах
- Мобильных устройствах

## 🔐 Безопасность

- Все чувствительные данные вынесены в переменные окружения
- Используется CSRF защита
- Настроена валидация паролей
- Подтверждение email при регистрации

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.

## 📞 Контакты

Если у вас есть вопросы или предложения, создайте issue в репозитории.

---

**U-Styles** - покупайте крутые вещи для себя и близких! 🛍️
