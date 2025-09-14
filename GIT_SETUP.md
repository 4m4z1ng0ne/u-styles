# Инструкции по настройке Git и загрузке в GitHub

## 🚀 Первоначальная настройка Git

### 1. Инициализация репозитория

```bash
cd u-styles
git init
```

### 2. Настройка пользователя Git (если не настроено)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Добавление файлов в репозиторий

```bash
git add .
```

### 4. Первый коммит

```bash
git commit -m "Initial commit: U-Styles Django e-commerce project"
```

## 📤 Загрузка в GitHub

### 1. Создание репозитория на GitHub

1. Перейдите на https://github.com
2. Нажмите "New repository"
3. Введите название: `u-styles`
4. Добавьте описание: "Django e-commerce store for clothing"
5. Выберите "Public" или "Private"
6. **НЕ** инициализируйте с README, .gitignore или лицензией
7. Нажмите "Create repository"

### 2. Подключение локального репозитория к GitHub

```bash
git remote add origin https://github.com/yourusername/u-styles.git
```

### 3. Загрузка кода

```bash
git branch -M main
git push -u origin main
```

## 🔄 Ежедневная работа с Git

### Добавление изменений

```bash
# Проверить статус
git status

# Добавить все изменения
git add .

# Или добавить конкретные файлы
git add filename.py

# Создать коммит
git commit -m "Описание изменений"

# Отправить на GitHub
git push
```

### Создание веток для новых функций

```bash
# Создать и переключиться на новую ветку
git checkout -b feature/new-feature

# Внести изменения и закоммитить
git add .
git commit -m "Add new feature"

# Отправить ветку на GitHub
git push -u origin feature/new-feature

# Создать Pull Request на GitHub
```

### Синхронизация с удаленным репозиторием

```bash
# Получить последние изменения
git pull origin main

# Или если работаете в ветке
git pull origin feature/new-feature
```

## 📋 Полезные команды Git

### Просмотр истории

```bash
# Краткая история коммитов
git log --oneline

# Подробная история
git log

# История конкретного файла
git log -- filename.py
```

### Отмена изменений

```bash
# Отменить изменения в рабочей директории
git checkout -- filename.py

# Отменить последний коммит (сохранив изменения)
git reset --soft HEAD~1

# Отменить последний коммит (удалив изменения)
git reset --hard HEAD~1
```

### Работа с ветками

```bash
# Показать все ветки
git branch -a

# Переключиться на ветку
git checkout branch-name

# Удалить локальную ветку
git branch -d branch-name

# Удалить удаленную ветку
git push origin --delete branch-name
```

## 🔒 Безопасность

### Важные файлы, которые НЕ должны попасть в Git

Убедитесь, что в `.gitignore` есть:

```
.env
*.log
__pycache__/
*.pyc
db.sqlite3
media/
staticfiles/
```

### Проверка перед коммитом

```bash
# Проверить, что будет добавлено в коммит
git status

# Просмотреть изменения
git diff

# Просмотреть изменения в staged файлах
git diff --cached
```

## 🏷️ Теги и релизы

### Создание тега

```bash
# Создать аннотированный тег
git tag -a v1.0.0 -m "Release version 1.0.0"

# Отправить тег на GitHub
git push origin v1.0.0
```

### Создание релиза на GitHub

1. Перейдите в раздел "Releases"
2. Нажмите "Create a new release"
3. Выберите тег
4. Добавьте описание релиза
5. Прикрепите файлы (опционально)
6. Нажмите "Publish release"

## 🤝 Совместная работа

### Fork и Pull Request

1. **Fork** репозитория на GitHub
2. Клонируйте свой fork:
   ```bash
   git clone https://github.com/yourusername/u-styles.git
   ```
3. Добавьте оригинальный репозиторий как upstream:
   ```bash
   git remote add upstream https://github.com/originalowner/u-styles.git
   ```
4. Создайте ветку для изменений
5. Внесите изменения и создайте Pull Request

### Синхронизация с upstream

```bash
# Получить изменения из оригинального репозитория
git fetch upstream

# Переключиться на main ветку
git checkout main

# Слить изменения
git merge upstream/main

# Отправить обновления в свой fork
git push origin main
```

## 📝 Хорошие практики

### Сообщения коммитов

Используйте понятные сообщения:

```bash
# Хорошо
git commit -m "Add user authentication system"
git commit -m "Fix bug in shopping cart calculation"
git commit -m "Update README with installation instructions"

# Плохо
git commit -m "fix"
git commit -m "changes"
git commit -m "update"
```

### Частота коммитов

- Делайте коммиты часто (каждые 1-2 часа работы)
- Каждый коммит должен содержать логически завершенное изменение
- Не коммитьте сломанный код

### Структура веток

- `main` - стабильная версия
- `develop` - ветка разработки
- `feature/feature-name` - новые функции
- `bugfix/bug-description` - исправления багов
- `hotfix/urgent-fix` - критические исправления

## 🆘 Решение проблем

### Конфликты при слиянии

```bash
# Если возникли конфликты при pull
git status  # посмотреть конфликтующие файлы
# Отредактировать файлы, разрешив конфликты
git add resolved-file.py
git commit -m "Resolve merge conflicts"
```

### Отмена последнего push

```bash
# Осторожно! Это перезапишет историю
git reset --hard HEAD~1
git push --force origin main
```

### Восстановление удаленных файлов

```bash
# Восстановить файл из последнего коммита
git checkout HEAD -- filename.py

# Восстановить файл из конкретного коммита
git checkout commit-hash -- filename.py
```

---

**Удачной работы с Git!** 🚀
