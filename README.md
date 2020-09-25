# D7.8
Module D7 homework


#### Как развернуть проект:
1. Создаем новый каталог виртуального окружения:
```
    python -m venv <Имя каталога>
```
2. Стянуть репозиторий к себе:
```
    git clone https://github.com/eternityxxxx/D7.8.git
```
3. Активируем виртуальное окружения:
```
    <Имя каталога>/Scripts/activate
```
4. Установить зависимости из requirements.txt:
```
    pip install -r requirements.txt
```
5. При создании файла с фикстурой возникли проблемы с кодировкой, поэтому:
###### Сразу запускаем сервер с клонированной из репозитория БД
```
    cd 'my_library'
    python manage.py runserver
```
