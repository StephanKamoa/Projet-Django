# Generated by Django 5.0 on 2024-01-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_competence_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Projet title')),
                ('image', models.ImageField(upload_to='projets')),
            ],
        ),
        migrations.DeleteModel(
            name='RecentWork',
        ),
    ]
