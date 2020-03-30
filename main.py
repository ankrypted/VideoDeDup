import os
import sys
import shutil
from PIL import Image
from collections import defaultdict


# Function to get Hamming Distance between two strings
def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        return 100
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))


# Function to check if a file is of supported format or not
def isImageFile(f):
    return f.lower().endswith(('.png', '.jpg', '.jpeg'))


# Function to get the hash value of an image
def getSoftHash(f):
    img = Image.open(f)
    img = img.resize((8, 8), Image.ANTIALIAS)
    img = img.convert("L")

    pixels = list(img.getdata())
    avg = sum(pixels) / len(pixels)

    bits = "".join(map(lambda pixel: '1' if pixel < avg else '0', pixels));
    hexadecimal = int(bits, 2).__format__('016x').upper()

    return hexadecimal


# Included command line arguments
if len(sys.argv) != 3:
    print ("Error !!! Correct usage : python ini.py <Directory for images> <Directory for uniques>")
    exit()

# Removing "/" from the end of the source directory
if sys.argv[1].endswith('/'):
    sys.argv[1] = sys.argv[1][:-1]

# Adding "/" at the end of the destination directory
if sys.argv[2].endswith('/') == 0:
    sys.argv[2] += "/"

hash_value = {}
hash_value1 = {}

X = 1
Y = 1
for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        f = root + "/" + file
        x = f
        if not isImageFile(x):
            continue
        hash_value[X] = getSoftHash(f)
        X += 1

for root, dirs, files in os.walk(sys.argv[2]):
    for file1 in files:
        f1 = root + "/" + file1
        x1 = f1
        if not isImageFile(x1):
            continue
        hash_value1[Y] = getSoftHash(f1)
        Y += 1

# print("hey")

flag = 1
length = len(hash_value)
length1 = len(hash_value1)

if length != length1 :
    print("Video Files are not the same")
else :
    print (length)
    for h in range(1, length):
        # for h1 in hash_value1:
        print(hash_value[h], hash_value1[h])
        if hash_value[h] != hash_value1[h]:
            flag = 0
            break
        if flag == 0:
            break

    if flag == 0:
        print("Video Files are not the same")
    else :
        print("Video Files are the same")


