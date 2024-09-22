import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import scienceplots

# Use the science plots style
plt.style.use(["science", "ieee", "grid"])

matplotlib.rcParams.update({"font.size": 16})

# Create figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))
fig.subplots_adjust(wspace=0.5)

# Define a circle
circle_radius = 5
circle_center = (0, 0)

# Plot 1: Regions where phi < 0 and phi > 0
circle1 = plt.Circle(circle_center, circle_radius + 0.25, color="blue", fill=False)
ax1.add_artist(circle1)
ax1.text(-5, 7, r"$\phi < 0$", fontsize=30, ha="center", va="center")
ax1.text(0, 0, r"$\phi > 0$", fontsize=30, ha="center", va="center")
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.set_aspect("equal")
ax1.grid(True, which="major", color="k", linestyle="-", alpha=0.1)
ax1.grid(True, which="minor", color="k", linestyle="--", alpha=0.05)
ax1.minorticks_on()
ax1.set_axisbelow(True)
ax1.grid(True)

# Plot 2: Filled circle with 1s inside and 0s outside
for y in np.arange(-10, 10, 2):
    if y == -10:
        continue

    for x in np.arange(-10, 10, 2):
        if x == -10:
            continue

        if (x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2 <= circle_radius**2:
            ax2.text(x, y, r"\textbf{1}", fontsize=12, ha="center", va="center")
        else:
            ax2.text(x, y, "0", fontsize=12, ha="center", va="center")
circle2 = plt.Circle(circle_center, circle_radius + 0.25, color="blue", fill=False)
ax2.add_artist(circle2)
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_aspect("equal")
ax2.axis("on")
ax2.grid(True, which="major", color="k", linestyle="-", alpha=0.1)
ax2.grid(True, which="minor", color="k", linestyle="--", alpha=0.05)
ax2.minorticks_on()
ax2.grid(True)

# Plot 3: Circle with 1s on the border and 0s elsewhere
for y in np.arange(-10, 10, 2):
    if y == -10:
        continue

    for x in np.arange(-10, 10, 2):
        if x == -10:
            continue

        if abs((x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2 - circle_radius**2) <= 10:
            if x < -2.5 and y < -2.5:
                ax3.text(x, y, "0", fontsize=12, ha="center", va="center")
                continue
            if x < -2.5 and y > 2.5:
                ax3.text(x, y, "0", fontsize=12, ha="center", va="center")
                continue
            if x > 2.5 and y > 2.5:
                ax3.text(x, y, "0", fontsize=12, ha="center", va="center")
                continue
            if x > 2.5 and y < -2.5:
                ax3.text(x, y, "0", fontsize=12, ha="center", va="center")
                continue

            ax3.text(x, y, r"\textbf{1}", fontsize=12, ha="center", va="center")
        else:
            ax3.text(x, y, "0", fontsize=12, ha="center", va="center")
circle3 = plt.Circle(circle_center, circle_radius + 0.25, color="blue", fill=False)
ax3.add_artist(circle3)
ax3.set_xlim(-10, 10)
ax3.set_ylim(-10, 10)
ax3.set_aspect("equal")
ax3.axis("on")
ax3.grid(True, which="major", color="k", linestyle="-", alpha=0.1)
ax3.grid(True, which="minor", color="k", linestyle="--", alpha=0.05)
ax3.minorticks_on()
ax3.grid(True)

# Add borders around subplots
for ax in [ax1, ax2, ax3]:
    for spine in ax.spines.values():
        spine.set_edgecolor("black")
        spine.set_linewidth(1.5)

# Add arrows between plots
fig.text(0.36, 0.5, r"$\overset{H(\phi)}{\longrightarrow}$", ha="center", va="center", fontsize=40)
fig.text(
    0.65, 0.5, r"$\overset{\nabla H(\phi)}{\longrightarrow}$", ha="center", va="center", fontsize=40
)

# Show the plot
# Set the grid to be below plot elements
plt.gca().set_axisbelow(True)

# Adjust layout for a tight fit
fig.savefig("heaviside-and-phi-illustration.png", bbox_inches="tight", dpi=300)