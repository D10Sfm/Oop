from Horseshoe import Horseshoe
class Horses(Horseshoe):
    def __init__(self,age,family,land_of_origin,no_legs,gender,breed):
        if super().breed == "horse":
            super().__init__(age,family, land_of_origin, no_legs, gender, breed)
    def __str__(self):
        return super().__str__()
