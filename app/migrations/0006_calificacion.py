# Generated by Django 2.2.24 on 2021-12-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211206_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.IntegerField(max_length=8)),
                ('fk_alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('fk_docente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.docente')),
            ],
        ),
    ]