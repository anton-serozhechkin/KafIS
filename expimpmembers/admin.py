from django.contrib import admin
from .models import *
from import_export import resources
from .resourses import *
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class MemberAdmin(ImportExportModelAdmin):
    list_display = ('last_name',
                    'first_name', 'middle_name',
                    'year', 'academic_group_of_student', )
    list_filter = ('year', )
    search_fields = ('first_name',
                     'middle_name',
                     'last_name', )
    resource_class = MemberResource


class AcademicGroupAdmin(ImportExportModelAdmin):
    list_display = ('academic_group_code', 'academic_group_faculty', )
    list_filter = ('academic_group_faculty', )
    resource_class = AcademicGroupResourse

 
class FacultyAdmin(admin.ModelAdmin):
    list_filter = ('name', )



admin.site.register(Member, MemberAdmin)
admin.site.register(AcademicGroup, AcademicGroupAdmin)
admin.site.register(Faculty, FacultyAdmin)