from django.contrib import admin
from .models import (
    Course,
    Discipline,
    Type_Framework,
    Type_Frameworks_Level,
    Type_Frameworks_Competency,
    Type_Frameworks_Competencies_Levels,
)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "ects")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "Course", "ects")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class Type_FrameworkAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    ordering = ("code", "name")
    search_fields = ("code", "name", "description")

class Type_Frameworks_LevelAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "Type_Framework", "value", "sort")
    ordering = ("Type_Framework", "sort")
    search_fields = ("code", "name", "description")

class Type_Frameworks_CompetencyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "Type_Framework")
    ordering = ("Type_Framework", "code")
    search_fields = ("code", "name", "description", "guidance")

class Type_Frameworks_Competencies_LevelsAdmin(admin.ModelAdmin):
    list_display = ("Type_Frameworks_Competency", "Type_Frameworks_Level", "description")
    ordering = ("Type_Frameworks_Competency", "Type_Frameworks_Level")
    search_fields = ("description",)

admin.site.register(Course, CourseAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Type_Framework, Type_FrameworkAdmin)
admin.site.register(Type_Frameworks_Level, Type_Frameworks_LevelAdmin)
admin.site.register(Type_Frameworks_Competency, Type_Frameworks_CompetencyAdmin)
admin.site.register(Type_Frameworks_Competencies_Levels, Type_Frameworks_Competencies_LevelsAdmin)