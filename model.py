import math

gravConst = 398603000000000.0

class tDynamicModel:
    rightParts = [0, 0, 0, 0, 0, 0]
    def funcs(self, current_time, vector):
        raise NotImplementedError()

class SpaceCraft(tDynamicModel):
    def funcs(self, current_time, vector):
        radius = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
        for i in range(3):
            self.rightParts[i] = vector[i+3]
            self.rightParts[i+3] = -gravConst*vector[i] / radius**3