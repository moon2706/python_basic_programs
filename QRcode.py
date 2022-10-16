import pyqrcode
from pyqrcode import QRCode

# strings which represent the QR Code
s="https://github.com/rishikesh-p2706/CowsAndBullsGame"
#s="Hii nice to see you guys"

#Generate QR Code
url=pyqrcode.create(s)

# Create and save the png fie naming "myqr.png"
url.svg("mygame.svg",scale=8)
url.png("mygame.png",scale=8)