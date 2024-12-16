

class Price:

    def __init__(self,value,tier):
        self.tier = tier
        self.value = value
        self.multiplier = self._multiplier()
        self.average_price = self._bases_price()
        self.min_price = self.minimum_price()

    def _multiplier(self):
        match self.tier:
            case 3:
                return 1.0
            case 4:
                return 1.2
            case 5:
                return 1.4
            case _:
                raise ValueError("Valor inserido incorreto")

    def _bases_price(self):
        base_1 = ((self.value - (self.value * 0.45)) / 12) / 30
        base_2 = (((self.value - (self.value * 0.45)) * 1.25)/ 12) / 20
        return (base_1,base_2)

    def minimum_price(self):
        mult = self.multiplier
        b1,b2 = self.average_price
        minimum_price = ((b1+b2)/2) * mult
        return minimum_price

    def base_price(self):
        minimum = self.min_price
        if self.value >= 200000:
            return minimum * 1.25
        
        if self.value < 200000:
            return minimum * 1.5
        
        else: 
            raise ValueError("Valor de minimo inserido está incorreto")
