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

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

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

        project = Project(project_parts[NAME_INDEX], project_parts[DATE_INDEX], project_parts[PRIORITY_INDEX],
                          project_parts[COST_INDEX], project_parts[PERCENT_INDEX])
        projects.append(project)

print(projects)