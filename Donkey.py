from Horseshoe import Horseshoe
class Donkey(Horseshoe):
    def __init__(self,age,land_of_origin,no_legs):
            super().__init__(age,land_of_origin,no_legs,breed="donkey")
    def __str__(self):
        return super().__str__()