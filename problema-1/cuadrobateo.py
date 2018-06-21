import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# sphinx_gallery_thumbnail_number = 2
y = np.around(np.arange(4, .99, -3/10), 2)
x = np.arange(-1.5, 2.0, 0.5)


def LoadData():
    try:
        data = np.genfromtxt('TedWilliams.csv', delimiter=',')
    except Exception as e:
        print(e)
    finally:
        return data


def setInfo(ax, data):
    for i in range(len(y)):
        for j in range(len(x)):
            ax.text(j, i, data[i, j],
                    ha="center", va="center", color="w")
    ax.set_title("HeatMap")


def main():
    data = LoadData()
    fig, ax = plt.subplots(1, 1, figsize=(11, 7))
    ax.imshow(data)

    ax.set_xticks(np.arange(len(x)))
    ax.set_yticks(np.arange(len(y)))

    ax.set_xticklabels(x)
    ax.set_yticklabels(y)

    ax.set_xticks(np.arange(len(x)))
    ax.set_yticks(np.arange(len(y)))

    ax.set_xticklabels(x)
    ax.set_yticklabels(y)
    fig.tight_layout()
    setInfo(ax, data)
    plt.show()


if __name__ == '__main__':
    main()
