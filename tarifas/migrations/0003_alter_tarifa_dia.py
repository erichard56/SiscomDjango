# Generated by Django 4.1.4 on 2023-02-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0002_alter_tarifa_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifa',
            name='dia',
            field=models.CharField(choices=[('0Do', '0 Domingo'), ('1Lu', '1 Lunes'), ('2Ma', '2 Martes'), ('3Mi', '3 Miércoles'), ('4Ju', '4 Jueves'), ('5Vi', '5 Viernes'), ('6Sa', '6 Sábado')], max_length=3),
        ),
    ]