from functions import functions
import PySimpleGUI as sg

class Interface:
    def __init__(self):
        theme = sg.theme("Reddit")

        layout = [
        
        [sg.Text("Fórmula de Bhaskara")],
        [sg.Text("Valor de A:"), sg.Input(key="a", size=(5,0))],
        [sg.Text("Valor de B:"), sg.Input(key="b", size=(5,0))],
        [sg.Text("Valor de C:"), sg.Input(key="c", size=(5,0))],
        [sg.Button("Confirmar")],
        [sg.Text(" ", size=(0,1), key="result")],
        [sg.Text(" ", size=(0,1), key="step")]
        ]

        self.window = sg.Window("Fórmula de Bhaskara", layout)

    def begin(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break
            if event == "Confirmar":
                try:
                    self.a = float(values["a"])
                    self.b = float(values["b"])
                    self.c = float(values["c"])
                    
                    result = functions.bhaskara(self.a, self.b,self.c)
                    functions.step(self.a, self.b, self.c)
                    
                    
                    self.window["result"].update(f"O resultado é {result}")
                    self.window["step"].update("Veja o passo a passo no arquivo txt na pasta do projeto.")
                except:
                    self.window["result"].update("Digite apenas números.")

obj_class = Interface()
obj_class.begin()