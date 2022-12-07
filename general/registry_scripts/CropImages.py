import os
import subprocess
import sys
import time

sys.argv.pop(0)

imgMagickPath = os.environ.get("IMAGEMAGICK_PATH") + "\\" if os.environ.get("IMAGEMAGICK_PATH") else ""
print(f"ImageMagick Directory = {imgMagickPath}")

for entry in sys.argv:
    if entry.endswith(".png"):
        # convert "!img!" -trim  "!img!"
        subprocess.call([f"{imgMagickPath}convert.exe", entry, '-trim', entry])
    # Give some time for the user to see the output before closing
    time.sleep(3)

