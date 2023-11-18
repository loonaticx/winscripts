import os
import subprocess
import sys
import time

sys.argv.pop(0)

imgMagickPath = os.environ.get("IMAGEMAGICK_PATH") + "\\" if os.environ.get("IMAGEMAGICK_PATH") else ""
print(f"ImageMagick Directory = {imgMagickPath}")

"""
convert -background transparent "favicon.png" -define icon:auto-resize=16,24,32,48,64,72,96,128,256 "favicon.ico"

"""

pargs = [
    '-background',
    'transparent',
    'entryname',
    '-define',
    'icon:auto-resize=16,24,32,48,64,72,96,128,256',
    'entryout'
]

for entry in sys.argv:
    if entry.endswith(".png"):
        pargs[2] = entry
        entryOut = entry.replace('.png', '.ico')
        pargs[-1] = entryOut
        subprocess.call([f"{imgMagickPath}convert.exe", *pargs])
    # Give some time for the user to see the output before closing
    time.sleep(3)

