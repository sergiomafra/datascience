from matplotlib import pyplot as plt


# Data
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Plot
plt.scatter(friends, minutes)

# Style
for label, friend_count, minute_count, in zip(labels, friends, minutes):
    plt.annotate(
        label,
        xy=(friend_count, minute_count),
        xytext=(5, -5),
        textcoords='offset points')
plt.title('Daily Minutes vs. Number of Friends')
plt.xlabel('Number of Friends')
plt.ylabel('daily minutes spent on website')

# Render
plt.show()
