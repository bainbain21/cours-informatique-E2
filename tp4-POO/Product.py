class Product:
    def __init__(self, code: str, name: str, priceET: float):
        self.code = code
        self.name = name
        self.priceET = priceET

    def get_price_it(self, tax: float) -> float:
        return self.priceET * (1 + tax)
