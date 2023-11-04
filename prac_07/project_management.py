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
MENU = ("- (L)oad projects \n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>>")
FILENAME = 'projects.txt'


def main():
    projects = process_incoming_records(FILENAME)
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'l':
            load_file = input("Filename as name.txt:")
            process_incoming_records()
        elif choice == 's':
            save_file = input("Filename as name.txt:")
            process_outgoing_records(projects, save_file)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            # filter_with_date(projects)
                pass
        elif choice == 'a':
            # add_project(projects)
            pass
        elif choice == 'u':
            pass
        choice = input(MENU).lower()
    process_outgoing_records(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent = input("Percent complete: ")
    project = Project(name, start_date, priority, cost, percent)
    projects.append(project)


def filter_with_date(projects):
    # filter by dates
    # date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
    # Test with:
    date_string = '30/9/2022'
    print("date")
    for project in projects:
        # compare
        # object_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        if datetime.strptime(project.start_date, "%d/%m/%Y").date() > datetime.strptime(date_string, "%d/%m/%Y").date():
            print(project)


def display_projects(projects):
    # display projects from whatever file was most recently loaded and processed
    print("Incomplete Projects")
    for project in projects:
        if not project.is_complete():
            print(project)
    print("Completed Projects")
    for project in projects:
        if project.is_complete():
            print(project)



def process_incoming_records(filename=FILENAME):
    # load_file = input("Filename as name.txt:")
    projects = []
    with open(filename, 'r') as in_file:
        # file format: Name	Start Date	Priority	Cost Estimate	Completion Percentage
        # don't want the first line so just read it
        in_file.readline()
        lines = in_file.readlines()
        # print(lines)
    for line in lines:
        project_parts = line.strip().split('\t')
        # want priority as int and cost as float and percent as int
        project_parts[PRIORITY_INDEX] = int(project_parts[PRIORITY_INDEX])
        project_parts[COST_INDEX] = float(project_parts[COST_INDEX])
        project_parts[PERCENT_INDEX] = int(project_parts[PERCENT_INDEX])
        # want date as date for project class to work
        # project_parts[DATE_INDEX] = datetime.datetime.strptime(project_parts[DATE_INDEX], "%d/%m/%Y").date()
        project = Project(project_parts[NAME_INDEX], project_parts[DATE_INDEX], project_parts[PRIORITY_INDEX],
                          project_parts[COST_INDEX], project_parts[PERCENT_INDEX])
        projects.append(project)
    return projects

def process_outgoing_records(projects, filename):
    lines = []
    with open(filename, 'w') as out_file:
        out_file.write('Name	Start Date	Priority	Cost Estimate	Completion Percentage\n')
    with open(filename, 'a') as out_file:
        for project in projects:
            # date was changed at some point to y-m-d so reformatting
            # reformatted_date = datetime.datetime.strptime(project[DATE_INDEX], "%d/%m/%Y").date()
            project_string = (f'{project.name}	{project.start_date}	{project.priority}	{project.cost_estimate}'
                              f'	{project.completion_percent}\n')
            out_file.write(project_string)






def run_tests():
    projects = process_incoming_records('projects.txt')
    print(projects)
    process_outgoing_records(projects, 'projects2.txt')





# main()
run_tests()