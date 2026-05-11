from django.contrib import admin

from .models import (
    Course,
    Discipline,
    Type_Framework,
    Type_Frameworks_Level,
    Type_Frameworks_Competency,
    Type_Frameworks_Competencies_Levels,
    Teacher,
    Discipline_Teacher,
    Project,
    Type_Technology,
    Discipline_Technology, 
    Project_Technology,
    Certification_Technology,
    Certification_Competency,
    FinalProject,
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

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    ordering = ("name",)
    search_fields = ("name",)

class Discipline_TeacherAdmin(admin.ModelAdmin):
    list_display = ("Discipline", "Teacher")
    ordering = ("Discipline", "Teacher")

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    ordering = ("name",)
    search_fields = ("name",)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('name',)

class DisciplineTechnologyAdmin(admin.ModelAdmin):
    list_display = ('Discipline', 'Technology')
    list_filter = ('Discipline', 'Technology')

class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ('Project', 'Technology')
    list_filter = ('Project', 'Technology')
    
class CertificationTechnologyAdmin(admin.ModelAdmin):
    list_display = ('Certification', 'Technology')
    list_filter = ('Certification', 'Technology')

class CertificationCompetencyAdmin(admin.ModelAdmin):
    list_display = ('Certification', 'Competency', 'Level')
    list_filter = ('Certification', 'Competency', 'Level')

class FinalProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'Course', 'year', 'students', 'supervisor', 'rating')
    search_fields = ('title', 'students', 'supervisor', 'keywords')
    list_filter = ('Course', 'year', 'rating')

admin.site.register(Course, CourseAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Type_Framework, Type_FrameworkAdmin)
admin.site.register(Type_Frameworks_Level, Type_Frameworks_LevelAdmin)
admin.site.register(Type_Frameworks_Competency, Type_Frameworks_CompetencyAdmin)
admin.site.register(Type_Frameworks_Competencies_Levels, Type_Frameworks_Competencies_LevelsAdmin)
#admin.site.register(Discipline_Teacher, Discipline_TeacherAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Type_Technology, TechnologyAdmin)
#admin.site.register(Discipline_Technology, DisciplineTechnologyAdmin)
#admin.site.register(Project_Technology, ProjectTechnologyAdmin)
admin.site.register(Certification_Technology, CertificationTechnologyAdmin)
admin.site.register(Certification_Competency, CertificationCompetencyAdmin)
admin.site.register(FinalProject, FinalProjectAdmin)