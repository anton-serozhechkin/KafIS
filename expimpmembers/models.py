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
    academic_group_code = models.CharField(primary_key=True, max_length=50, verbose_name='Шифр навчальної групи')
    academic_group_faculty = models.ForeignKey('Faculty', models.DO_NOTHING, verbose_name='Факультет', null=True)

    def __str__(self):
        return self.academic_group_code

    class Meta:
        db_table = "Академічні групи"

class Member(models.Model):
    last_name = models.CharField('Прізвіще', max_length=50, default='')  
    first_name = models.CharField("ім'я", max_length=50, default='')
    middle_name = models.CharField('По батькові', max_length=50, default='', null=True)
    year = models.PositiveSmallIntegerField('Рік навчання', validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    academic_group_of_student = models.ForeignKey('AcademicGroup', on_delete=models.DO_NOTHING, verbose_name='Академічна група')
    id_number = models.CharField('Номер студентського квитка', max_length=50, primary_key=True, default='Невідомо')

    class Meta:
        db_table = "Студенти"

