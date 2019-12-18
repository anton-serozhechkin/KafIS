from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from enum import Enum, unique

class Faculty(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='Назва факультету', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Факультет'

    
class AcademicGroup(models.Model):
    academic_group_code = models.CharField(max_length=25, unique=True, verbose_name='Шифр навчальної групи', null=True)
    academic_group_faculty = models.ForeignKey('Faculty', models.CASCADE, verbose_name='Факультет')

    def __str__(self):
        return self.academic_group_code

    class Meta:
        db_table = "Академічні групи"

class Member(models.Model):
    last_name = models.CharField('Прізвіще', max_length=50, default='')  
    first_name = models.CharField("ім'я", max_length=50, default='')
    middle_name = models.CharField('По батькові', max_length=50, default='', null=True)
    year = models.PositiveSmallIntegerField('Рік навчання', validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    #academic_group = models.OneToManyField('AcademicGroup', null=True, verbose_name='Академічна група')
    academic_group = models.CharField('Академічна група', null=True, max_length=50)
    id_number = models.CharField('Номер студентського квитка', max_length=50, null=True)

    class Meta:
        db_table = "Студенти"