import Library as Conv
from PIL import Image
import numpy as np
from pathlib import Path

def main(path):
    #path = input("Caminho da Imagem:\n")
    try:
        if path == "":
            path = "BinaryCode.gif"
        path = Path(path)
        img = Image.open(path).convert("RGB")
        pix = img.load()
        largura, altura = img.size
        l = 0
        a = 0
        code = ""
        while l < largura:
            while a < altura:
                if pix[a,l] == (255,255,255):
                    code += "0"
                else:
                    code += "1"
                a += 1
            a = 0
            l += 1
        print(Conv.convert_bin_text(code))
        return True
    except:
        return False

