import numpy as np
import matplotlib.pyplot as plt


# part one
for i in range(1, 7):
    f = open(f"../data/basis/figure{i}.txt", 'r')
    size = float(f.readline().strip())
    f.readline()  # read '#' sign
    img = []
    for line in f:
        img.append(list(map(int, line.strip().split())))

    img = np.array(img)
    pixels = np.where(img == 1)

    plt.imshow(img)
    plt.show()

    if img.max() == 0:
        print(f"image {i}, no image")
        continue

    # the furthest left point
    min_x = pixels[1].min()

    # the furthest right point
    max_x = pixels[1].max()

    pixel_dist = max_x - min_x
    # 0 1 1 1 0 - min_x = 1 | max_x = 3 | pixels = (3 - 1) + 1
    nominal_resolution = size / (pixel_dist+1)
    print(f"image {i}, nominal_resolution: {nominal_resolution}")
