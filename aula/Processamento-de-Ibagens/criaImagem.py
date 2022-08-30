from email.mime import image
from PIL import Image
from PIL import ImageColor

def cria_imagem(fileName, size):
    imagem = Image.new("RGBA", size)
    cor1 = ImageColor.getcolor("white", "RGBA")
    cor2 = ImageColor.getcolor("black", "RGBA")
    cor = cor2
    i = 0

    for y in range(size[1]):
        for x in range(size[0]):
            if i == 99:
                cor = cor2 if cor1 == cor else cor1
                i = 0 
            imagem.putpixel((x,y), cor)
            i += 1
    imagem.save(fileName)




if __name__ == "__main__":
    cria_imagem("imagem.png", (100, 100))
