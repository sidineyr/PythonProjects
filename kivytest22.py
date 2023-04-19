import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Configurar a aplicação Kivy
kivy.require('2.0.0')


class IMCCalculatorApp(App):
    def build(self):
        # Criar o layout da aplicação
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Adicionar o rótulo de título
        title_label = Label(text='Calculadora de IMC',
                            font_size=24,
                            bold=True)
        layout.add_widget(title_label)

        # Adicionar a entrada de peso
        weight_input = TextInput(hint_text='Peso (kg)')
        layout.add_widget(weight_input)

        # Adicionar a entrada de altura
        height_input = TextInput(hint_text='Altura (m)')
        layout.add_widget(height_input)

        # Adicionar o rótulo de resultado
        result_label = Label(text='', font_size=24)
        layout.add_widget(result_label)

        # Adicionar o botão de cálculo
        calculate_button = Button(text='Calcular', size_hint=(1, 0.5))
        calculate_button.bind(on_press=lambda x: self.calculate_imc(weight_input.text, height_input.text, result_label))
        layout.add_widget(calculate_button)

        # Retornar o layout como o widget principal da aplicação
        return layout

    def calculate_imc(self, weight, height, result_label):
        try:
            # Converter os inputs de peso e altura para float
            weight = float(weight)
            height = float(height)

            # Calcular o IMC
            imc = weight / (height ** 2)

            # Exibir o resultado no rótulo de resultado
            result_label.text = f'Seu IMC é: {imc:.2f}'
        except ValueError:
            # Lidar com erros de conversão de tipo
            result_label.text = 'Erro: Peso e altura devem ser números'


# Inicializar e executar a aplicação
if __name__ == '__main__':
    IMCCalculatorApp().run()
