"""
Programming Languages.
Estimate: 20 mins. Start: 4:59pm
Actual: 32 mins. End: 5:31pm
"""


class ProgrammingLanguage:
    """Programming Language class"""

    def __init__(self, name, typing, reflection, year):
        """Initialise Programming Language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of data in Programming Language."""
        return f'{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}'

    def __repr__(self):
        """Return string of list object."""
        return str(self)

    def is_dynamic(self):
        """Return true/false if language is dynamic."""
        return self.typing == 'Dynamic'
