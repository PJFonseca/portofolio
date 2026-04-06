## Intro
This is a WIP project and the history will be on the commits

## Structure

The main entities (so far) are:

### Courses
#### Will store the courses that exist
  - ID
  - Code - A unique code within the couses, because I do not want to be doing code with IDs
  - Name
  - Description
  - ECTS
  - Background Color - This is to be able to create some visual help on the website
  - Text Color - This is to be able to create some visual help on the website
  - Icon - Using Fontawesome icons to look nicer

### Why so complicated Frameworks structure?
#### This is what companies are using to develop roles that people are in. This way they can map a competency vs a role and then check if the person has it and what course must be taken to achieve that competency.

### Type_Frameworks
#### It will store all frameworks that could be used
  - ID
  - Code - A unique code within the Frameworks, because I do not want to be doing code with IDs
  - Name
  - Description
  - Background Color - This is to be able to create some visual help on the website
  - Text Color - This is to be able to create some visual help on the website
  - Icon - Using Fonta~~~~wesome icons to look nicer

### Type_Frameworks_Competencies
#### What competencies does a certain framework provide. It will contain all of them
  - ID
  - Frameworkid
  - Code - A unique code within the Frameworks, because I do not want to be doing code with IDs
  - Name
  - Description
  - Guidance
  - Background Color - This is to be able to create some visual help on the website
  - Text Color - This is to be able to create some visual help on the website
  - Icon - Using Fontawesome icons to look nicer

### Type_Frameworks_Competencies
#### What competencies does a certain framework provide. It will contain all of them
  - ID
  - Frameworkid
  - Code - A unique code within the Frameworks, because I do not want to be doing code with IDs
  - Name
  - Description
  - Guidance
  - Background Color - This is to be able to create some visual help on the website
  - Text Color - This is to be able to create some visual help on the website
  - Icon - Using Fontawesome icons to look nicer

### Disciplines_Competencies
#### Will store what competencies the disciplines provides 
  - ID
  - DisciplineID
  - CompetencyID
  - LevelID
  - Start - When it started to be valid
  - End - When it ended

### Competencies
#### This will be using the SFIA framework, with levels and stuff

- Disciplines
- Projects
- Technologies
- Teachers
