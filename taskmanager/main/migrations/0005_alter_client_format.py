# Generated by Django 4.0.3 on 2022-03-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_client_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='format',
            field=models.CharField(choices=[('f1', 'Очно'), ('f2', 'Заочно'), ('f3', 'Дистанционно'), ('f4', 'Слушатель'), ('f5', 'Докладчик')], max_length=5, verbose_name='Вид образования'),
        ),
    ]