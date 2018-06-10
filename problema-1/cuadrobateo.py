import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2

vegetables = [x + (3/11) for x in range(0, 11)]
farmers = [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5]

harvest = np.array([[0.300, 0.320, 0.320, 0.350, 0.330, 0.315, 0.310],
                    [0.310, 0.340, 0.340, 0.350, 0.340, 0.340, 0.320],
                    [0.310, 0.340, 0.340, 0.350, 0.340, 0.340, 0.320],
                    [0.340, 0.380, 0.380, 0.400, 0.390, 0.390, 0.320],
                    [0.360, 0.390, 0.390, 0.400, 0.390, 0.390, 0.320],
                    [0.360, 0.390, 0.390, 0.400, 0.380, 0.380, 0.310],
                    [0.320, 0.340, 0.340, 0.330, 0.300, 0.300, 0.280],
                    [0.320, 0.340, 0.340, 0.330, 0.275, 0.270, 0.260],
                    [0.280, 0.300, 0.300, 0.300, 0.260, 0.250, 0.250],
                    [0.270, 0.290, 0.300, 0.300, 0.250, 0.240, 0.240],
                    [0.350, 0.270, 0.270, 0.260, 0.240, 0.240, 0.230]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))

# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Harvest of local farmers (in tons/year)")
# fig.tight_layout()
plt.show()
