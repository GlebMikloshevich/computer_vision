import numpy as np
import matplotlib.pyplot as plt


def read_img(path) -> np.array:
    f = open(path, 'r')
    f.readline()  # read '#' sign
    img = []
    for line in f:
        img.append(list(map(int, line.strip().split())))
    f.close()
    img = np.array(img)
    return img


img1 = read_img("../data/basis/img1.txt")
pixels1 = np.where(img1 == 1)

img2 = read_img("../data/basis/img2.txt")
pixels2 = np.where(img2 == 1)

img1_start_x = pixels1[1].min()
img1_start_y = pixels1[0].min()

img2_start_x = pixels2[1].min()
img2_start_y = pixels2[0].min()

print(f"y bias: {img1_start_y - img2_start_y}")
print(f"x bias: {img1_start_x - img2_start_x}")
