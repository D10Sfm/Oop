from Horseshoe import Horseshoe
class Donkeys(Horseshoe):
    def __init__(self,age,family,land_of_origin,no_legs,gender,breed):
        if super().breed == "donkey":
            super().__init__(age,family, land_of_origin, no_legs, gender, breed)
    def __str__(self):
        return super().__str__()