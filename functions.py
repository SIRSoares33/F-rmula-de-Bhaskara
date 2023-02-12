from body_txt import body_txt
import os

class Functions:
    
    def bhaskara(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c

        self.delta = self.b ** 2 - (4 * self.a * self.c)
        
        if self.delta < 0:
            return f"Delta Negativo (D = {self.delta})"
        
        self.division = 2 * self.a
        
        self.raiz_delta = pow(self.delta, 1/2)

        self.x1 = -self.b + self.raiz_delta
        self.x1 /= self.division
        
        self.x2 = -self.b - self.raiz_delta
        self.x2 /= self.division

        return f"X1 = {self.x1}, X2 = {self.x2}"

    def step(self, a, b,c):
        try:
            os.remove("Passo a passo.txt")
            body_txt(a,b,c, self.delta, self.raiz_delta, self.division, self.x1, self.x2)
        except:
            body_txt(a,b, c, self.delta, self.raiz_delta, self.division, self.x1, self.x2)




functions = Functions()
