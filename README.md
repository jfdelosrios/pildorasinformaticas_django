# pildorasinformaticas_django
Solucionario del curso https://www.youtube.com/playlist?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB

dirección en github https://github.com/jfdelosrios/pildorasinformaticas_django.git

Este repositorio requiere crear el ambiente cuando es clonado. Correr script.sh para generar el ambiente.
./script.sh

# para correr servidor
python manage.py runserver

# para enviar
git push origin master

# para salir de (END)
presiona tecla "q"

# para clonar
git clone xxx
(donde xxx es la url del proyecto)

# correr un script desde git bash, 
https://stackoverflow.com/questions/36401147/running-sh-scripts-in-git-bash

# activar ambiente
source .env/Scripts/activate

# desactivar ambiente
deactivate

# correr servidor
python manage.py runserver

python manage.py shell


# actualizar base de datos

primero
python manage.py makemigrations

segundo
python manage.py migrate


//--------------------------

# Dudas

# comentatios

video 2:
- Cambió comando "manage.py help" por "python manage.py"

# ejecutar script para llenar la base de datos
 https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell

 Recuerde tener creada la base de datos con el mismo nombre registrada en el diccionario DATABASES de settings.py