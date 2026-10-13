class Fraction:

    def __init__(self, num:int, den:int):
        self.num=num
        self.den=den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
        num = self.num*other.den + other.num*self.den
        den = self.den*other.den
        return Fraction(num,den)

    def __sub__(self,other):
        num = self.num*other.den - other.num*self.den
        den = self.den*other.den
        return Fraction(num,den)

    def __mul__(self,other):
        num = self.num*other.num
        den = self.den*other.den
        return Fraction(num,den)

    def __truediv__(self,other):
        num = self.num*other.den
        den = self.den*other.num
        return Fraction(num,den)

    def __gt__(self,other):
        return self.num*self.den > other.num*other.den

    def __lt__(self,other):
        return self.num*self.den < other.num*other.den

    def __le__(self,other):
        return self.num*self.den <= other.num*other.den

    def __ge__(self,other):
        return self.num*self.den >= other.num*other.den

    def __eq__(self,other):
        return self.num*self.den == other.num*other.den

    def __ne__(self,other):
        return self.num*self.den != other.num*other.den


