class Pizza:
    def __init__(self):
        self.size = ""
        self.toppings = []
    
    def __str__(self):
        return f"Пицца {self.size}: {', '.join(self.toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza

# Использование
pizza = (PizzaBuilder()
        .set_size("большая")
        .add_topping("сыр")
        .add_topping("грибы")
        .build())
print(pizza)  # Пицца большая: сыр, грибы
