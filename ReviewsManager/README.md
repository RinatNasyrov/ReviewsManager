# ReviewApp
Django-приложение для отправки/чтения отзывов
## QuickStart
```
git clone https://github.com/RinatNasyrov/ReviewsManager.git
cd ReviewsManager

python -m venv venv
venv/Scripts/activate
python -m pip install -U pip

pip install -r requirements.txt
```
Локальный запуск:
```
python manage.py runserver
```
## Using REST API
Получение списка отзывов в JSON-формате GET-запростом:
```
/api/v1/get_list
```
Отправка списка обзоров в JSON-формате POST-запросом:
```
/api/v1/post_reviews
```