import os

for file in os.scandir("color/"):
    os.remove(file)
for file in os.scandir("pc/"):
    os.remove(file)
for file in os.scandir("trns_color/"):
    os.remove(file)
for file in os.scandir("fin_pc/"):
    os.remove(file)
for file in os.scandir("rt/"):
    os.remove(file)
print("Removed all!")