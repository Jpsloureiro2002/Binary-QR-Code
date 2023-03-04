# Binary-QR-Code
Generator and decompiler of a binary image, with basic cryptography, and with the compiler with in built commands.

# What you need
- You must first install PILLOW, TKINTER, CTYPES

pip install tkinter<br>
pip install pillow<br>
pip install ctypes

# How it works:
- Generates a 160x160 .gif image with the conversion of characters in ASCII to binary that will be reperesented by white(0) and black(1) pixels
- Decompile the image back to text
- The decompiler can also Compile commands for example if at the beginning of the text is file:[py] it will create a file output_0.py
- All characters have an 8 bit binary match which can be re-arranged to "encrypt" the output
- The characters that are not included are special characters like [&, ?, $] - (represent actions like tab, null_space, and newline), [characters with ',`,^,~], [!,£,€,§,|].
- The Library file contains the conversion dictionary where you can add new characters or change the code corresponding to the characters.

# How to run it:
- There are 2 Files called Decode.py and Generate.py, they are two files with visual support that you can use them in a more friendly way, run with python for now.

# Future improvements:
- Fix some bugs
- Clean up the Code
- Make the 2 executables into one
- Add more characters
- Improve file creation code

# Example
<h2>File Example</h2>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/Example/File_py_ex.jpg)

<h5>Image output</h5>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/BinaryCode/File_py_Ex.gif)

<h2>Popup Example</h2>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/Example/Msg-pop_example.jpg)

<h5>Image output</h5>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/BinaryCode/Popup_Ex.gif)

<h2>Open .exe Files Example</h2>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/Example/exe-open_ex.jpg)

<h2>URL Example</h2>

![Not Found](https://raw.githubusercontent.com/Jpsloureiro2002/Binary-QR-Code/main/App/Example/url_ex.jpg)
