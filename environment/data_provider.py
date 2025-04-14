import random

class BasicDataSource:
    """
    A basic data source that provides simple facts or numbers for citizens to learn.
    This will simulate basic learning opportunities within the environment.
    """

    def __init__(self):
        self.data = [
            "fact1: The sky is blue.",
            "fact2: Water is wet.",
            "fact3: Fire is hot.",
            "fact4: The Earth revolves around the Sun.",
            "fact5: 2 + 2 equals 4.",
            "fact6: Birds can fly.",
            "fact7: Fish live in water.",
            "fact8: Humans need oxygen to breathe.",
            "fact9: The moon orbits the Earth.",
            "fact10: Sunlight is a source of energy."
        ]
    
    def get_random_fact(self):
        """
        Return a random fact from the data source for the citizens to learn.
        """
        return random.choice(self.data)
