comandos para iniciar django

.\env\Scripts\activate

python manage.py runserver


si no funciona colocar lo siguiente 

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

***DOCKER***

docker-compose exec web python manage.py createsuperuser

3. Las migraciones
Cuando hagas cambios en tus modelos (models.py), ahora tendrás que ejecutar las migraciones a través de Docker. En lugar de solo python manage.py migrate, usarás:

Bash

"docker-compose exec web python manage.py migrate"