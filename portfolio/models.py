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

    def __str__(self):
        return self.name

class Discipline(models.Model):
    # One Discipline exists in one course, I'm assuming every discipline is tailored for that course only
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#This is to include the SFIA framework
class Type_Framework(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type_Frameworks_Level(models.Model):
    Type_Framework = models.ForeignKey(Type_Framework, on_delete=models.CASCADE, related_name='levels')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    value = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    sort = models.IntegerField()

    def __str__(self):
        return self.name

class Type_Frameworks_Competency(models.Model):
    Type_Framework = models.ForeignKey(Type_Framework, on_delete=models.CASCADE, related_name='competencies')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    guidance = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type_Frameworks_Competencies_Levels(models.Model):
    Type_Frameworks_Competency = models.ForeignKey(Type_Frameworks_Competency, on_delete=models.CASCADE, related_name='type_frameworks_competency')
    Type_Frameworks_Level = models.ForeignKey(Type_Frameworks_Level, on_delete=models.CASCADE, related_name='type_frameworks_level')
    description = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    

class Teacher(models.Model):
    Discipline = models.ManyToManyField(Discipline, on_delete=models.CASCADE, related_name='disciplines')
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name