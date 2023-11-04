"""
Project
Estimate: 4 hours
start: 11pm
end:
Actual: 45 + 10 + 120 + 20 + 120
"""
from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percent=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __repr__(self):
        return (f'{self.name}, start: {self.start_date}, priority {self.priority},'
                f' estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percent}% ')



    def __lt__(self, other):
        return datetime.strptime(self.start_date, "%d/%m/%Y") > datetime.strptime(other, "%d/%m/%Y")

    def is_complete(self):
        return self.completion_percent == 100



def project_tests():
    first_project = Project('Build Car Park', '12/09/2021', 2, 600000.0, 95)
    print(first_project)
    second_project = Project('Mow Lawn', '31/10/2022', 3, 3.0, 0)
    # print(first_project < '31/10/2022')

# project_tests()
