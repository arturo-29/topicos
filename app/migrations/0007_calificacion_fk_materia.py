# Generated by Django 2.2.24 on 2021-12-06 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='fk_materia',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.materia'),
            preserve_default=False,
        ),
    ]
