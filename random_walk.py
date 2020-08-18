from random import choice
class RandomWalk():
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        #All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_change=choice([-4,-3,-2,-1,0,1,2,3,4])
            y_change=choice([-4,-3,-2,-1,0,1,2,3,4])
            
            #dismiss empty moves
            if x_change*y_change==0:
                continue

            new_x=self.x_values[-1]+x_change
            new_y=self.y_values[-1]+y_change

            self.x_values.append(new_x)
            self.y_values.append(new_y)

import matplotlib.pyplot as plt

rw=RandomWalk(50_000)            
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()

point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()



