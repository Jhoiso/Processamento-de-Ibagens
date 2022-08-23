from ast import If
import io 
import os
from turtle import width
import requests
import numpy as np
import PySimpleGUI as sg
from PIL  import Image
sg.theme("Dark")

def main():
    
#---------------------------------------------Funções de carregar imagem-------------------------------------------------
    def carregaUrl():
        #https://casa.abril.com.br/wp-content/uploads/2021/05/Descubra-os-significados-de-cada-flor-pintrest-13.jpg
        image = value["-LINK-"] 
        image=Image.open(requests.get(url=image, stream=True).raw) 
        bio = io.BytesIO()
        image.save(bio, format="PNG")  
        window["-IMAGE-"].update(data=bio.getvalue(), size=(500,500)) 
        return image
        
    def carregaImagem():
        filename = value["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(filename)
            image.thumbnail((500,500))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue(), size=(500,500))
            return image

#---------------------------------------------Funções de reconhecer a ação da CBX-----------------------------------------
    def carregaCombo(combo, image):
        if combo == "Thumbnail":
            image.thumbnail((75, 75))
            image.save("thumbnail.jpg")

        if combo == "Reduzir qualidade":
            image.resize((500,500))
            image.save("qruim.jpg")

        if combo == ".JPG":
            image.save("img.jpg")
        
        if combo == ".PNG":
            image.save("img.png")

#-----------------------------------------------------Criação do layout-----------------------------------------------------
    layout =[
        [
            sg.Text("Endereço da Imagem: "),
            sg.Input(size=(25,1), key="-FILE-"),
            sg.FileBrowse(file_types=[("JPEG (*jpg)", "*.jpg"), ("Todos os arquivos" , "*.*")]),
            sg.Button("Carregar Imagem"),
            sg.Combo(["Thumbnail", ".JPG", "Reduzir qualidade", ".PNG"], key="-COMBO-"),
        ],
        [sg.Image(key="-IMAGE-", size=(500,500))],
        [   sg.Text("Endereço URL: "),
            sg.Input(size=(25,1), key="-LINK-"),
            sg.Button("Carregar URL"),
            sg.Button("ENTER")
        ]
    ]


#---------------------------------------------------Criação da janela--------------------------------------------------------
    window = sg.Window("Gerenciador de Imagens", layout=layout)
    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
       
        if event == "Carregar Imagem":
            image = carregaImagem()

        if event == "Carregar URL":
            image =carregaUrl()

        combo = value["-COMBO-"]
        if event == "ENTER":
            carregaCombo(combo, image)

    window.close()                

#------main-----
if __name__ == "__main__":
    main()