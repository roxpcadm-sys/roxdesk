# Gera os ícones e logos do RoxDesk a partir das imagens da RoxPC.
# Uso: python roxdesk-marca.py   (rodar na pasta roxdesk)
import os
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
ROX = os.path.join(AQUI, '..', 'roxpc')
ICONE = os.path.join(ROX, 'servidor', 'public', 'icone-512.png')
LOGO = os.path.join(ROX, 'novo', 'img', 'logo-roxpc.png')            # texto escuro (tema claro)
LOGO_CLARO = os.path.join(ROX, 'novo', 'img', 'logo-roxpc-claro.png')  # texto claro (tema escuro)

ic = Image.open(ICONE).convert('RGBA')

def png(dest, lado):
    p = os.path.join(AQUI, dest)
    ic.resize((lado, lado), Image.LANCZOS).save(p)
    print('ok', dest, lado)

def png_mesmo_tamanho(dest):
    p = os.path.join(AQUI, dest)
    w, h = Image.open(p).size
    ic.resize((w, h), Image.LANCZOS).save(p)
    print('ok', dest, (w, h))

def ico(dest):
    p = os.path.join(AQUI, dest)
    ic.save(p, format='ICO', sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print('ok', dest)

def logo(orig, dest):
    im = Image.open(orig).convert('RGBA')
    alt = 120
    im = im.resize((round(im.width * alt / im.height), alt), Image.LANCZOS)
    im.save(os.path.join(AQUI, dest))
    print('ok', dest, im.size)

for f in ['res/32x32.png', 'res/64x64.png', 'res/128x128.png', 'res/128x128@2x.png', 'res/icon.png', 'res/mac-icon.png']:
    png_mesmo_tamanho(f)
for f in ['res/icon.ico', 'res/tray-icon.ico', 'flutter/windows/runner/resources/app_icon.ico']:
    ico(f)
png('flutter/assets/icon.png', 256)
logo(LOGO, 'flutter/assets/logo.png')
logo(LOGO_CLARO, 'flutter/assets/logo_dark.png')
