import Library as Conv
from PIL import Image
import numpy as np
from pathlib import Path
import os
def main(text,qrcode):
	pixels = []
	bites = 160
	Black = (0,0,0)
	White = (255,255,255)

	#text = input("Escreve algo:\n")
	#qrcode = input("Nome do Binary code:")
	if qrcode == "":
		qrcode = "BinaryCode"
	check = True
	bin_text = Conv.convert_text_bin(text)
	print(len(bin_text))
	if len(bin_text) > (bites * bites):
		print("Texto Demasiado Grande")
		check = False
	#96 x 96
	
	if check:
		count_x = 0
		count_y = 0
		count = 0
		Line_pixel = []
		print("Image Generating \n")
		done = False
		dell = "01111111"
		count_dell = 0
		binario = 0
		while count_y < bites:
			Line_pixel.clear()
			while count_x < bites:
				try:
					if bin_text[count] == "1":
						Line_pixel.append(Black)
					else:
						Line_pixel.append(White)
				except:
					if not done:
						if dell[count_dell] == "1":
							Line_pixel.append(Black)
						else:
							Line_pixel.append(White)
						count_dell += 1
						if count_dell == 8:
							done = True
					else:
						if binario:
							Line_pixel.append(Black)
							binario = 0
						else:
							Line_pixel.append(White)
							binario = 1
				count += 1
				count_x += 1
			count_x = 0
			count_y += 1
			pixels.append(tuple(Line_pixel))

		print("Image Done")
		pixel_num = np.array(pixels, dtype=np.uint8)
		new_image = Image.fromarray(pixel_num)
		if not os.path.exists("BinaryCode"):
			os.makedirs("BinaryCode")
		new_image.save(Path("BinaryCode/" + qrcode + '.gif'))
	return True
