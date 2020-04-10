# Generated by Django 3.0.4 on 2020-03-20 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('buc', 'Bucharest'), ('ias', 'Iași'), ('clu', 'Cluj-Napoca')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_enrolled', models.DateField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
        ),
    ]
