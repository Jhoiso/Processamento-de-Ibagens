from PIL import Image

def pega_cores(imagem):
    imagem = Image.open(imagem)
    colors = imagem.getcolors(imagem.size[0] * imagem.size[1])
    for pixel in colors:
        print (pixel)

if __name__ == "__main__":
    pega_cores("img.png")