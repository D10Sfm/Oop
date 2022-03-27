from Horseshoe import Horseshoe
class Horse(Horseshoe):
    def __init__(self,age,land_of_origin,no_legs):
            super().__init__(age,land_of_origin,no_legs,breed="horse")
    def __str__(self):
        return super().__str__()
