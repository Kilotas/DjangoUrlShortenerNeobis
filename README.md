# URL Shortener

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/url-shortener.git
Перейдите в директорию проекта:
bash
Copy code
cd myproject
Создайте и активируйте виртуальное окружение:
bash
Copy code
python -m venv venv
.\venv\Scripts\activate  # для Windows
source venv/bin/activate  # для Linux/Mac
Установите зависимости:
bash
Copy code
pip install -r requirements.txt
Запуск

Примените миграции:
bash
Copy code
python manage.py migrate
Запустите сервер разработки:
bash
Copy code
python manage.py runserver
Приложение доступно по http://127.0.0.1:8000/.

Использование

/ - Главная страница с формой для сокращения URL.
/create - Обработка формы и создание короткой ссылки.
/<str:pk> - Переход по сокращенной ссылке.
/url/<str:uuid> - Редирект на оригинальный URL по UUID.
/url/stats/<str:uuid> - Получение статистики использования сокращенной ссылки.
Дополнительные настройки

В файле settings.py можно настроить различные параметры, такие как база данных, настройки безопасности и другие.
Лицензия

Этот проект распространяется под лицензией MIT.
