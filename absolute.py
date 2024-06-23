from PIL import Image, ImageDraw, ImageFont



def resizer(width, height, length):
    w = int(width/length)
    h = int(height/length)
    size = (w, h)
    return size

def abcinema(text:str):
    nome = text[:8]

    absolute = ImageFont.truetype("normal.ttf", 15)
    font = ImageFont.truetype("normal.ttf", 60)
    ft = Image.open("ab.jpg")
    w, h = ft.size


    eu = ft.resize(resizer(w,h, 2))
    des = ImageDraw.Draw(eu)
    des.text((int(w/8), 250), nome, fill="white", font=font)
    des.text((int(w/5), 226), "Absolute", fill="white", font=absolute)

    foto = "foto.png"
    eu.save(foto)

    return foto


text = "Cinema"
print(abcinema(text))
