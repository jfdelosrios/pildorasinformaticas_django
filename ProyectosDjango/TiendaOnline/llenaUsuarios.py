from django.contrib.auth.models import User

User.objects.create_superuser(username='juand', email ='cursos@pildorasinformaticas.es', password='123456')

# Staff status dice si le permite o no loguear
User.objects.create_user(username='juan2', password='123456789')