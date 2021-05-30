# Generated by Django 3.2 on 2021-05-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210530_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='background_image',
            field=models.ImageField(blank=True, help_text='Imagem do fundo da pagina (1920x1080 ou 16:9)', null=True, upload_to='background'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='cover_image',
            field=models.ImageField(blank=True, help_text='Imagem do card (560x170)', null=True, upload_to='cover'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Imagem de perfil (170x170 ou 1:1)', null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, help_text='Imagem do projeto (225x225 ou 1:1)', null=True, upload_to='projects'),
        ),
    ]
