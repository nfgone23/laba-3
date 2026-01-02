class Button:
    def draw(self):
        return "Кнопка"

class WinButton(Button):
    def draw(self):
        return "Win кнопка"

class MacButton(Button):
    def draw(self):
        return "Mac кнопка"

class Factory:
    def create_button(self):
        return Button()

class WinFactory(Factory):
    def create_button(self):
        return WinButton()

class MacFactory(Factory):
    def create_button(self):
        return MacButton()

# Использование
factory = WinFactory()
btn = factory.create_button()
print(btn.draw())  # Win кнопка
