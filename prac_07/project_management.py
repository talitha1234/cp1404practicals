"""
Project Management
Estimate: 4 hours
Actual: 6.75 hours
"""

from datetime import datetime

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
    """"Manages a list of projects from a file."""
    projects = process_incoming_records(FILENAME)
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'l':
            filename = get_valid_string("Filename as name.txt")
            projects = process_incoming_records(filename)
        elif choice == 's':
            filename = get_valid_string("Filename as name.txt")
            process_outgoing_records(projects, filename)
        elif choice == 'd':
            prioritised_projects = sorted(projects)
            display_incompleted_projects(prioritised_projects)
            display_completed_projects(prioritised_projects)
        elif choice == 'f':
            date_string = get_valid_date("Show projects that start after date (dd/mm/yyyy)")
            display_projects_after_date(date_string, projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            """Update project with percent completed."""
            display_numbered_projects(projects)
            is_project_number = False
            while not is_project_number:
                try:
                    project_choice = get_valid_integer("Project choice")
                    print(projects[project_choice])
                    is_project_number = True
                except IndexError:
                    print("This is not a project number.")
            new_percentage = get_valid_integer("New percentage")
            while new_percentage > 100:
                print("Not a valid percentage.")
                new_percentage = get_valid_integer("New percentage")
            projects[project_choice].completion_percent = new_percentage
        else:
            print("Invalid Choice.")
        choice = input(MENU).lower()
    process_outgoing_records(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def display_incompleted_projects(prioritised_projects):
    completed_projects = []
    print("Incomplete Projects")
    for project in prioritised_projects:
        if not project.is_complete():
            print(project)

def display_completed_projects(prioritised_projects):
    completed_projects = []
    print("Incomplete Projects")
    for project in prioritised_projects:
        if project.is_complete():
            print(project)


def display_numbered_projects(projects):
    """Display the projects numbered starting at 0."""
    for i, project in enumerate(projects, 0):
        print(f'{i} {project}')


def display_projects_after_date(date_string, projects):
    """Display projects after date of given string."""
    for project in projects:
        if date_string > project:
            print(project)


def get_valid_date(message):
    "Validate date string in the form dd/mm/yyy"
    is_valid_date = False
    while not is_valid_date:
        try:
            date_string = input(f'{message}:')
            # this doesn't change date_string, it just checks if the date is the
            # correct format so it can be used by class
            datetime.strptime(date_string, "%d/%m/%Y")
            is_valid_date = True
        except ValueError:
            print("Not a valid date.")
    return date_string


def add_project(projects):
    """Add a new project to list of projects."""
    print("Let's add a new project")
    name = get_valid_string("Name")
    start_date = get_valid_date("Start date (dd/mm/yyyy)")
    priority = get_valid_integer("Priority")
    cost = get_valid_cost("Cost estimate")
    percent = get_valid_integer("Percent complete")
    while percent > 100:
        print("Not a valid percentage.")
        percent = get_valid_integer("Percent complete")

    project = Project(name, start_date, priority, cost, percent)
    projects.append(project)


def display_projects(projects):
    """Display incomplete and completed projects"""
    # display projects from whatever file was most recently loaded and processed
    print("Incomplete Projects")
    for project in projects:
        if not project.is_complete():
            print(project)
    print("Completed Projects")
    for project in projects:
        if project.is_complete():
            print(project)


def process_incoming_records(filename):
    """Format incoming records of projects."""
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
        datetime.strptime(project_parts[DATE_INDEX], "%d/%m/%Y")
        project = Project(project_parts[NAME_INDEX], project_parts[DATE_INDEX], project_parts[PRIORITY_INDEX],
                          project_parts[COST_INDEX], project_parts[PERCENT_INDEX])
        projects.append(project)
    return projects


def process_outgoing_records(projects, filename):
    """Format outgoing records of projects for file."""
    with open(filename, 'w') as out_file:
        out_file.write('Name	Start Date	Priority	Cost Estimate	Completion Percentage')
    with open(filename, 'a') as out_file:
        for project in projects:
            project_string = (
                f'\n{project.name}	{project.start_date}	{project.priority}	{project.cost_estimate}'
                f'	{project.completion_percent}')
            out_file.write(project_string)


def get_valid_integer(message):
    """Get a positive integer number."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(f'{message}:'))
            while number < 0:
                print(f"{message} must be not be < 0.")
                number = int(input(f'{message}:'))
            is_valid_number = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return number


def get_valid_cost(message):
    """Get a positive float number."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(f'{message}: $'))
            while number < 0:
                print(f"{message} must not be < 0.")
                number = float(input(f'{message}: $'))
            is_valid_number = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return number


def get_valid_string(message):
    """Get a string value."""
    string = input(f"{message}:")
    while string == '':
        print("Input can not be blank")
        string = input(f"{message}:")
    return string


main()
