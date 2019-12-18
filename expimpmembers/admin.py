from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export.fields import Field


class MemberResource(resources.ModelResource):
    last_name = Field(attribute='last_name', column_name='Прізвіще')
    first_name = Field(attribute='first_name', column_name="імя")
    middle_name = Field(attribute='middle_name', column_name='По батькові')
    year = Field(attribute='year', column_name='Рік навчання')
    academic_group = Field(attribute='academic_group', column_name='Академічна група')
    id_number = Field(attribute='id_number', column_name='Номер студентського квитка')

    class Meta:
        model = Member
        import_id_fields = ('last_name',)
        fields = ('last_name',
                  'first_name', 'middle_name',
                  'year', 'academic_group',
                  'id_number', )
    
        
class MemberAdmin(ImportExportModelAdmin):
    list_display = ('last_name',
                    'first_name', 'middle_name',
                    'year', 'academic_group', )
    list_filter = ('year', )
    search_fields = ('first_name',
                     'middle_name',
                     'last_name', )
    resource_class = MemberResource


admin.site.register(Member, MemberAdmin)
admin.site.register(Faculty)
admin.site.register(AcademicGroup)

