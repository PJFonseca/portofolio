from django.contrib import admin

from .models import (
    Course,
    Discipline,
    Type_Frameworks,
    Type_Frameworks_Levels,
    Type_Frameworks_Competencies,
    Type_Frameworks_Competencies_Levels,
)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "ects")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "courseid", "ects")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class Type_FrameworksAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class Type_Frameworks_LevelsAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "frameworkid", "value", "sort")
    ordering = ("frameworkid", "sort")
    search_fields = ("code", "name", "description")

class Type_Frameworks_CompetenciesAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "frameworkid")
    ordering = ("frameworkid", "code")
    search_fields = ("code", "name", "description", "guidance")

class Type_Frameworks_Competencies_LevelsAdmin(admin.ModelAdmin):
    list_display = ("competencyid", "levelid", "description")
    ordering = ("competencyid", "levelid")
    search_fields = ("description",)

admin.site.register(Course, CourseAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Type_Frameworks, Type_Frameworks_LevelsAdmin)
admin.site.register(Type_Frameworks_Levels, Type_Frameworks_LevelsAdmin)
admin.site.register(Type_Frameworks_Competencies, Type_Frameworks_CompetenciesAdmin)
admin.site.register(Type_Frameworks_Competencies_Levels, Type_Frameworks_Competencies_LevelsAdmin)