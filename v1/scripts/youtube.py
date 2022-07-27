#python script
import pyperclip

def printIFrame(embedCode):
    print("<iframe width='700' height='394' src='", end="")
    print("https://www.youtube.com/embed/" + embedCode, end="")
    print("' title='YouTube video player' frameborder='0' allow='accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>", end="")

data = pyperclip.paste()
if "https://www.youtube.com/watch?v=" in data:
    embedCode = data.replace("https://www.youtube.com/watch?v=", "", 1)
    printIFrame(embedCode)
elif "https://youtu.be/" in data:
    embedCode = data.replace("https://youtu.be/", "", 1)
    printIFrame(embedCode)
elif "https://www.youtube.com/embed/" in data:
    embedCode = data.replace("https://www.youtube.com/embed/", "", 1)
    printIFrame(embedCode)
else:
    print("data invalid " + data, end="")