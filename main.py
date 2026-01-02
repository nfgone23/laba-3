# Запуск всех паттернов
import singleton
import factory_method
import abstract_factory
import builder

print("=== Все паттерны ===")

# Singleton
s1 = singleton.Singleton()
s2 = singleton.Singleton()
print(f"Singleton: {s1 is s2}")

# Factory Method
f = factory_method.Factory()
p = f.create("A")
print(f"Factory: {p.info()}")

# Abstract Factory
af = abstract_factory.WinFactory()
btn = af.create_button()
print(f"Abstract Factory: {btn.draw()}")

# Builder
pizza = (builder.PizzaBuilder()
        .set_size("средняя")
        .add_topping("сыр")
        .build())
print(f"Builder: {pizza}")
