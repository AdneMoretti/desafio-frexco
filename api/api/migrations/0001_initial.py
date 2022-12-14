# Generated by Django 4.1.3 on 2022-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('senha', models.CharField(blank=True, help_text='senha do usuário', max_length=255)),
                ('dataNascimento', models.DateField(help_text='Data de nascimento do usuário')),
            ],
        ),
    ]
