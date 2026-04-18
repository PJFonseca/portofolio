import os
import json
from django.core.management.base import BaseCommand
from portfolio.models import Course, Discipline

class Command(BaseCommand):
    help = 'Import course and discipline data from JSON files'

    def handle(self, *args, **options):
        data_dir = os.path.join(os.path.dirname(__file__), '../../helpers/files')
        courses = {}
        
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if 'courseCode' not in data:
                    self.stdout.write(f'Skipping {filename}: no courseCode')
                    continue
                
                # Create or get course
                course_code = str(data['courseCode'])
                course_name = data['courseName']
                if course_code not in courses:
                    course, created = Course.objects.get_or_create(
                        code=course_code,
                        defaults={
                            'name': course_name,
                            'description': data.get('objectives', ''),
                            'ects': 0,  # Default, since course ects not specified
                            'background_color': '#ffffff',
                            'text_color': '#000000',
                            'icon': 'default.png'
                        }
                    )
                    courses[course_code] = course
                    if created:
                        self.stdout.write(f'Created course: {course_name}')
                else:
                    course = courses[course_code]
                
                # Create discipline
                discipline_code = data['curricularIUnitReadableCode']
                discipline_name = data['curricularUnitName']
                discipline, created = Discipline.objects.get_or_create(
                    code=discipline_code,
                    defaults={
                        'name': discipline_name,
                        'description': data.get('programme', ''),
                        'ects': data.get('ects', 0),
                        'background_color': '#ffffff',
                        'text_color': '#000000',
                        'icon': 'default.png',
                        'Course': course
                    }
                )
                if created:
                    self.stdout.write(f'Created discipline: {discipline_name}')
        
        self.stdout.write('Import completed.')