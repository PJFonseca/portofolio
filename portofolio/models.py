from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

class Discipline(models.Model):
    # One Discipline exists in one course, I'm assuming every discipline is tailored for that course only
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

#This is to include the SFIA framework
class Type_Frameworks(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

class Type_Frameworks_Levels(models.Model):
    frameworkid = models.ForeignKey(Type_Frameworks, on_delete=models.CASCADE, related_name='frameworks')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    value = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    sort = models.IntegerField()

class Type_Frameworks_Competencies(models.Model):
    frameworkid = models.ForeignKey(Type_Frameworks, on_delete=models.CASCADE, related_name='frameworks')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    guidance = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

class Type_Frameworks_Competencies_Levels(models.Model):
    competencyid = models.ForeignKey(Type_Frameworks_Competencies, on_delete=models.CASCADE, related_name='type_frameworks_competencies')
    levelid = models.ForeignKey(Type_Frameworks_Levels, on_delete=models.CASCADE, related_name='type_frameworks_levels')
    description = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

