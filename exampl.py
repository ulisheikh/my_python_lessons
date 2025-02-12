# ==============================
#  KIVY TUGMALARI, WIDJETLAR VA FUNKSIYALARI
# ==============================

# 1. App.run()
# Dastur bajarilishini boshlaydi.
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text="Hello World")

    def on_start(self):
        print("App is starting!")

    def on_stop(self):
        print("App is stopping!")

if __name__ == '__main__':
    MyApp().run()


# 2. Button(text, background_color, size_hint)
# Tugma yaratish.
from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        return Button(text="Click Me!", background_color=(0.1, 0.5, 0.1, 1), size_hint=(0.3, 0.3))

if __name__ == '__main__':
    MyApp().run()


# 3. Label(text, color, font_size)
# Yozuv yaratish.
from kivy.uix.label import Label
from kivy.app import App

class MyApp(App):
    def build(self):
        return Label(text="Hello Kivy!", color=(0, 1, 0, 1), font_size=32)

if __name__ == '__main__':
    MyApp().run()


# 4. BoxLayout(orientation, padding, spacing)
# BoxLayout yaratish.
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        layout.add_widget(Button(text='Button 1'))
        layout.add_widget(Button(text='Button 2'))
        return layout

if __name__ == '__main__':
    MyApp().run()


# 5. GridLayout(cols, rows)
# GridLayout yaratish.
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=3, rows=2)
        layout.add_widget(Button(text='Button 1'))
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Button(text='Button 3'))
        return layout

if __name__ == '__main__':
    MyApp().run()


# 6. FloatLayout()
# Erkin joylashgan elementlar uchun layout.
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        btn = Button(text='Click Me', size_hint=(None, None), size=(200, 100), pos=(100, 100))
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MyApp().run()


# 7. Slider(min, max, value)
# Slider yaratish.
from kivy.uix.slider import Slider
from kivy.app import App

class MyApp(App):
    def build(self):
        slider = Slider(min=0, max=100, value=50)
        return slider

if __name__ == '__main__':
    MyApp().run()


# 8. TextInput(text, multiline, password)
# Foydalanuvchi matn kiritishi uchun input maydoni yaratish.
from kivy.uix.textinput import TextInput
from kivy.app import App

class MyApp(App):
    def build(self):
        input_field = TextInput(text='', multiline=False, password=False)
        return input_field

if __name__ == '__main__':
    MyApp().run()


# 9. ColorPicker()
# Rang tanlagich widgeti.
from kivy.uix.colorpicker import ColorPicker
from kivy.app import App

class MyApp(App):
    def build(self):
        return ColorPicker()

if __name__ == '__main__':
    MyApp().run()


# 10. CheckBox(active, group)
# Checkbox yaratish.
from kivy.uix.checkbox import CheckBox
from kivy.app import App

class MyApp(App):
    def build(self):
        checkbox = CheckBox(active=True, group='group1')
        return checkbox

if __name__ == '__main__':
    MyApp().run()


# 11. Switch(active)
# Yoqish/ o'chirish tugmasi (switch).
from kivy.uix.switch import Switch
from kivy.app import App

class MyApp(App):
    def build(self):
        switch = Switch(active=True)
        return switch

if __name__ == '__main__':
    MyApp().run()


# 12. ProgressBar(value, max)
# Progress bar yaratish.
from kivy.uix.progressbar import ProgressBar
from kivy.app import App

class MyApp(App):
    def build(self):
        progress = ProgressBar(value=50, max=100)
        return progress

if __name__ == '__main__':
    MyApp().run()


# 13. Popup(title, content, size_hint)
# Popup oynasini yaratish.
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App

class MyApp(App):
    def build(self):
        popup = Popup(title="Popup Title", content=Label(text="This is a popup message"), size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    MyApp().run()


# 14. Image(source)
# Rasmni ko'rsatish.
from kivy.uix.image import Image
from kivy.app import App

class MyApp(App):
    def build(self):
        return Image(source="image.jpg")

if __name__ == '__main__':
    MyApp().run()


# 15. Canvas()
# Rasm chizish uchun canvas yaratish.
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.app import App

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Line(points=[100, 100, 400, 400], width=2)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()


# 16. Line(points, width)
# Chiziq chizish.
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.app import App

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Line(points=[50, 50, 200, 200], width=2)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()


# 17. Rectangle(size, pos)
# To'rtburchak chizish.
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.app import App

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(size=(100, 100), pos=(100, 100))

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()


# 18. Ellipse(size, pos)
# Ellips chizish.
from kivy.graphics import Ellipse
from kivy.uix.widget import Widget
from kivy.app import App

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Ellipse(size=(100, 100), pos=(100, 100))

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()


# 19. TextInput.bind(on_text_validate)
# Matnni tekshirish uchun inputga bog'lash.
from kivy.uix.textinput import TextInput
from kivy.app import App

class MyApp(App):
    def build(self):
        input_field = TextInput()
        input_field.bind(on_text_validate=self.on_text_validate)
        return input_field

    def on_text_validate(self, instance):
        print("Text input validated!")

if __name__ == '__main__':
    MyApp().run()


# 20. Label.bind(on_touch_down)
# Matnga tegish hodisasi bilan bog'lash.
from kivy.uix.label import Label
from kivy.app import App

class MyApp(App):
    def build(self):
        label = Label(text="Click me!")
        label.bind(on_touch_down=self.on_touch)
        return label

    def on_touch(self, instance, touch):
        print("Label touched!")

if __name__ == '__main__':
    MyApp().run()
