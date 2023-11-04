"""
Project Management
Estimate: 4 hours
start:
end:
Actual:
"""

import datetime

from prac_07.project import Project

NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENT_INDEX = 4

# load_file = input("Filename as name.txt:")
projects = []
with open("projects.txt", 'r') as in_file:
    # file format: Name	Start Date	Priority	Cost Estimate	Completion Percentage
    # don't want the first line so just read it
    in_file.readline()
    for line in in_file:
        project_parts = line.strip().split('\t')
        # want priority as int and cost as float and percent as int
        project_parts[PRIORITY_INDEX] = int(project_parts[PRIORITY_INDEX])
        project_parts[COST_INDEX] = float(project_parts[COST_INDEX])
        project_parts[PERCENT_INDEX] = int(project_parts[PERCENT_INDEX])
        # want date as date for project class to work
        project_parts[DATE_INDEX] = datetime.datetime.strptime(project_parts[DATE_INDEX], "%d/%m/%Y").date()
        project = Project(project_parts[NAME_INDEX], project_parts[DATE_INDEX], project_parts[PRIORITY_INDEX],
                          project_parts[COST_INDEX], project_parts[PERCENT_INDEX])
        projects.append(project)

print(projects)

# display projects
complete_projects = (project for project in projects if project.is_complete())
incomplete_projects = (project for project in projects if not project.is_complete())

print("Incomplete Projects")
for project in incomplete_projects:
    print(project)

print("Completed Projects")
for project in complete_projects:
    print(project)


# add new project
# print("Let's add a new project")
# name = input("Name: ")
# start_date = input("Start date (dd/mm/yy): ")
# priority = input("Priority: ")
# cost = input("Cost estimate: $")
# percent = input("Percent complete: ")
# project = Project(name, start_date, priority, cost, percent)
# projects.append(project)

# filter by dates
# date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
date_string = '30/9/2022'
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print("date")
for project in projects:
    if project.start_date > date:
        print(project)


