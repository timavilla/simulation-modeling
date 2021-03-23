class tAbstractIntegrator:
    t0 = 0
    tk = 0
    h = 0
    def oneStep(self, spacecraft, vector):
        raise NotImplementedError()    

class tEuler(tAbstractIntegrator):
    def __init__(self, t0, tk, h):
        self.t0 = t0
        self.tk = tk
        self.h = h
    def oneStep(self, spacecraft, vector):
        spacecraft.funcs(1, vector)
        for i in vector:
            vector[i] += self.h * spacecraft.rightParts[i]
    
class tRungeKutta(tAbstractIntegrator):
    k0 = []
    k1 = []
    k2 = []
    k3 = []
    def __init__(self, t0, tk, h):
        self.t0 = t0
        self.tk = tk
        self.h = h
    def oneStep(self, spacecraft, vector):
        spacecraft.funcs(1, vector)            #k0
        self.k0 = spacecraft.rightParts
        list1 = [0, 0, 0, 0, 0, 0]

        for i in range (len(vector)):                 #k1
            list1[i] = vector[i] + self.h/2*self.k0[i]
        spacecraft.funcs(1, list1)
        self.k1 = spacecraft.rightParts

        for i in range (len(vector)):                 #k2
            list1[i] = vector[i] + self.h/2*self.k1[i]
        spacecraft.funcs(1, list1)
        self.k2 = spacecraft.rightParts

        for i in range (len(vector)):                 #k3
            list1[i] = vector[i] + self.h*self.k2[i]
        spacecraft.funcs(1, list1)
        self.k3 = spacecraft.rightParts
    
        for i in range (len(vector)):
            vector[i] = vector[i] + (self.h/6) * (self.k0[i] + 2*self.k1[i] + 2*self.k2[i] + self.k3[i])