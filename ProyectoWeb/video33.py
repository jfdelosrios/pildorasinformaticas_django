from django.contrib.auth.models import User

User.objects.create_superuser(username='juand', email ='cursos@pildorasinformaticas.es', password='123456')