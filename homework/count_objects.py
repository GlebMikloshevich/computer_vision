import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
import tqdm

plt.figure(figsize=(50, 50))
img = np.load("../data/ps.npy")

inner_mask = np.array([[0, 1], [1, 1]])
outer_outer = np.array([[0, 0], [0, 1]])


def count_objects(image: np.array) -> tuple:
    outer = 0
    inner = 0
    for y in range(0, image.shape[0] - 1):
        for x in range(0, image.shape[1] - 1):
            sub = image[y:y+2, x:x+2]
            if match(sub, inner_mask):
                inner += 1
            elif match(sub, outer_outer):
                outer += 1
    return outer, inner


def match(a: np.array, mask: np.array) -> bool:
    if np.all(a == mask):
        return True
    return False


def euler(labeled, label):
    pos = np.where(labeled == label)

    y_min = pos[0].min()
    y_max = pos[0].max()

    x_min = pos[1].min()
    x_max = pos[1].max()

    new_image = np.zeros((y_max-y_min+2) * (x_max-x_min+2))
    new_image = new_image.reshape((y_max-y_min+2, x_max-x_min+2))
    new_image[1:y_max-y_min+1, 1:x_max-x_min+1] = labeled[y_min:y_max, x_min:x_max]
    pos = np.where(new_image == label)
    new_image[pos] = 1

    x, v = count_objects(new_image)
    return (x, v)


def count_object(labeled):
    dict = {}
    for i in tqdm.tqdm(range(1, labeled.max() + 1)):
        fig = euler(labeled, i)
        if fig in dict:
            dict[fig] += 1
        else:
            dict[fig] = 1
    return dict


labeled = label(img)
objects = count_object(labeled)
print(f"there are {labeled.max()} objects")
i = 0
for value in objects.values():
    print(f"type {i} object: {value}")
    i += 1
