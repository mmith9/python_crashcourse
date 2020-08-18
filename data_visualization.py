import matplotlib.pyplot as plt

x_values=range(-1000,1000)
y_values=[x*x for x in x_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_values,y_values,s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()

