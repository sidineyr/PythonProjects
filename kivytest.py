import kivy
from kivy.app import App
from kivy.uix.button import Button

# Configurar a aplicação Kivy
kivy.require('2.0.0')


class MyButtonApp(App):
    def build(self):
        # Criar um botão
        button = Button(text='Clique em mim!',
                        size_hint=(0.5, 0.5),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Definir uma função de callback para o botão
        button.bind(on_press=self.on_button_press)

        # Retornar o botão como o widget principal da aplicação
        return button

    def on_button_press(self, instance):
        # Função de callback para lidar com o evento de pressionar o botão
        print('Botão pressionado!')


# Inicializar e executar a aplicação
if __name__ == '__main__':
    MyButtonApp().run()
