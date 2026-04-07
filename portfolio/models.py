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
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    photo = models.ImageField(null=True, blank=True, upload_to="media/photos/")

    def __str__(self):
        return self.name
    
class Discipline_Teacher(models.Model):
    Discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='discipline_teachers')
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='discipline_teachers')

class Project(models.Model):
    Discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='projects')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    interest_level = models.IntegerField(default=3)
    logo = models.ImageField(null=True, blank=True, upload_to="media/technologies/")
    link = models.CharField(max_length=2000)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Discipline_Technology(models.Model):
    Discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='discipline_technologies')
    Technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='discipline_technologies')

class Project_Technology(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_technologies')
    Technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='project_technologies')