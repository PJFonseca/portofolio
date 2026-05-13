from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    # One Discipline exists in one course, I'm assuming every discipline is tailored for that course only
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='disciplines')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    ects = models.IntegerField()
    finalgrade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#This is to include the SFIA framework
class Type_Framework(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type_Frameworks_Level(models.Model):
    Type_Framework = models.ForeignKey(Type_Framework, on_delete=models.CASCADE, related_name='Type_Frameworks_Levels')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    value = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    sort = models.IntegerField()

    def __str__(self):
        return self.name

class Type_Frameworks_Competency(models.Model):
    Type_Framework = models.ForeignKey(Type_Framework, on_delete=models.CASCADE, related_name='Type_Frameworks_Competencies')
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    guidance = models.TextField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type_Frameworks_Competencies_Levels(models.Model):
    Type_Frameworks_Competency = models.ForeignKey(Type_Frameworks_Competency, on_delete=models.CASCADE, related_name='type_frameworks_competencies_levels')
    Type_Frameworks_Level = models.ForeignKey(Type_Frameworks_Level, on_delete=models.CASCADE, related_name='type_frameworks_competencies_levels')
    description = models.TextField(blank=True, default='')
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
    description = models.TextField(blank=True, default='')
    date_completed = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Certification(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    date_start = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Type_Technology(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    interest_level = models.IntegerField(default=3)
    logo = models.ImageField(null=True, blank=True, upload_to="media/technologies/")
    link = models.CharField(max_length=2000)
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FinalProject(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='final_projects')
    title = models.CharField(max_length=500)
    summary = models.TextField()
    year = models.IntegerField()
    students = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    supervisor = models.CharField(max_length=200)
    report_link = models.CharField(max_length=2000, null=True, blank=True)
    keywords = models.CharField(max_length=500, null=True, blank=True)
    areas = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=2000, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    background_color = models.CharField(max_length=20, default='')
    text_color = models.CharField(max_length=20, default='')
    icon = models.CharField(max_length=100, default='')


class Discipline_Technology(models.Model):
    Discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='discipline_technologies')
    Technology = models.ForeignKey(Type_Technology, on_delete=models.CASCADE, related_name='discipline_technologies')

class Project_Technology(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_technologies')
    Technology = models.ForeignKey(Type_Technology, on_delete=models.CASCADE, related_name='project_technologies')

class Certification_Technology(models.Model):
    Certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='certification_technologies')
    Technology = models.ForeignKey(Type_Technology, on_delete=models.CASCADE, related_name='certification_technologies')


class Certification_Competency(models.Model):
    Certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='certification_competencies')
    Competency = models.ForeignKey(Type_Frameworks_Competency, on_delete=models.RESTRICT, related_name='certification_competencies')
    Level = models.ForeignKey(Type_Frameworks_Competencies_Levels, on_delete=models.RESTRICT, related_name='certification_competencies')
