"""
Project
Estimate: 4 hours
start: 5:15pm
end:
Actual:
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate=0.0, completion_percent=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __repr__(self):
        return str(f'{self.name}, start: {self.start_date}, priority {self.priority}, '
                   f'estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percent}%')

    def __lt__(self, other):
        return self.start_date < other.start_date

    def is_complete(self):
        return self.completion_percent == 100


def project_tests():
    first_project = Project('Build Car Park', '12/09/2021', 2, 600000.0, 95)
    print(first_project)
    second_project = Project('Mow Lawn', '31/10/2022', 3, 3.0, 0)
    #TODO figure out how to make the start_date a date and not a string so that this comparison will work
    # print(first_project < second_project)

# project_tests()
