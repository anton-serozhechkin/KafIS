# Generated by Django 2.2.8 on 2019-12-20 17:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicGroup',
            fields=[
                ('academic_group_code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Шифр навчальної групи')),
            ],
            options={
                'db_table': 'Академічні групи',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, null=True, verbose_name='Назва факультету')),
            ],
            options={
                'db_table': 'Факультет',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Прізвіще')),
                ('first_name', models.CharField(default='', max_length=50, verbose_name="ім'я")),
                ('middle_name', models.CharField(default='', max_length=50, null=True, verbose_name='По батькові')),
                ('year', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Рік навчання')),
                ('id_number', models.CharField(default='Невідомо', max_length=50, primary_key=True, serialize=False, verbose_name='Номер студентського квитка')),
                ('academic_group_of_student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='expimpmembers.AcademicGroup', verbose_name='Академічна група')),
            ],
            options={
                'db_table': 'Студенти',
            },
        ),
        migrations.AddField(
            model_name='academicgroup',
            name='academic_group_faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expimpmembers.Faculty', verbose_name='Факультет'),
        ),
    ]
