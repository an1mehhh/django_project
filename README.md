# Команды для использования программы:
1. Перенос даннных из модели (models.py) в БД:
```sh
python manage.py makemigrations
```
2. Проверка целостности структуры БД:
```sh
python manage.py migrate
``` 
3. Добавление первоначальных данных из json:
```sh
python manage.py fill
```
4. Очистка БД:
```sh
python manage.py clear_db
```
