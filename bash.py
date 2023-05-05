import os

res = ""
while res != "y":
    vol = float(input("Enter brightness value (.1 - 1):\n"))
    if vol > 0.1:
        os.system(f"xrandr --output HDMI-0 --brightness {vol}")
        res = input((f"brightness set to {vol}, it's well (y/n)"))
    else:
        print("value too low")
