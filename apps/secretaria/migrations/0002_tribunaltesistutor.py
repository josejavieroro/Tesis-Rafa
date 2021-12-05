# Generated by Django 2.2 on 2021-12-02 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TRibunalTesisTutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.secretaria.Tesis')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.secretaria.Profesor')),
            ],
        ),
    ]