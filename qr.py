import qrcode

image=qrcode.make('https://github.com/arijit2002')
image.save('qrcode.png')
