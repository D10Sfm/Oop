from Predators import Predators
class Tiger(Predators):
    def __init__(self,age,land_of_origin,no_legs):
            super().__init__(age,land_of_origin,no_legs,breed="tiger")
    def __str__(self):
        return super().__str__()