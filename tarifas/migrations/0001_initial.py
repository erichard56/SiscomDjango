# Generated by Django 4.1.4 on 2023-02-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(choices=[('ACAP', 'A Capital'), ('AMTE', 'A MonteGrande')], default='ACAP', max_length=4)),
                ('dia', models.CharField(choices=[('Do', 'Domingo'), ('Lu', 'Lunes'), ('Ma', 'Martes'), ('Mi', 'Miércoles'), ('Ju', 'Jueves'), ('Vi', 'Viernes'), ('Sa', 'Sábado')], max_length=2)),
                ('horaDesde', models.TimeField()),
                ('horaHasta', models.TimeField()),
            ],
        ),
    ]
