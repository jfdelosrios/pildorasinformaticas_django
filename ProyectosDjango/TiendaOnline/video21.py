from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'jorge.de@correounivalle.edu.co',
    ['jfdelosrios@hotmail.com'],
    fail_silently=False,
)