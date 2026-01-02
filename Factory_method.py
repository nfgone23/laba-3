class Product:
    def info(self):
        return "Продукт"

class ProductA(Product):
    def info(self):
        return "Продукт A"

class ProductB(Product):
    def info(self):
        return "Продукт B"

class Factory:
    def create(self, type):
        if type == "A":
            return ProductA()
        return ProductB()

# Использование
f = Factory()
p = f.create("A")
print(p.info())  # Продукт A
