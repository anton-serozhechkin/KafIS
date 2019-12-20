from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from .models import *

class MemberResource(resources.ModelResource):
    last_name = Field(attribute='last_name', column_name='Прізвіще')
    first_name = Field(attribute='first_name', column_name="імя")
    middle_name = Field(attribute='middle_name', column_name='По батькові')
    year = Field(attribute='year', column_name='Рік навчання')
    academic_group_of_student = Field(
        column_name='Академічна група',
        attribute='academic_group_of_student',
        widget=ForeignKeyWidget(AcademicGroup, 'academic_group_code'))
    id_number = Field(attribute='id_number', column_name='Номер студентського квитка')
    

    class Meta:
        model = Member
        import_id_fields = ('id_number',)
        fields = ('last_name',
                  'first_name', 'middle_name',
                  'year', 'academic_group_of_student',
                  'id_number', )


class AcademicGroupResourse(resources.ModelResource):
    academic_group_code = Field(attribute='academic_group_code', column_name='Академічна група')
    class Meta:
        model = AcademicGroup
        import_id_fields = ('academic_group_code',)
        fields = ('academic_group_code', )
        exclude = ('last_name',
                  'first_name', 'middle_name',
                  'year', 'id_number', )
                