from django.db import models

class User(models.Model):      
    login = models.CharField(
        unique=True,
        max_length=255
    )
    senha = models.CharField(
        unique=True,
        blank=True,
        max_length=255,
        help_text="senha do usuário"
    )
    dataNascimento = models.DateTimeField(
        help_text="Data de nascimento do usuário"
    )
