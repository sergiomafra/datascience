from collections import Counter
from matplotlib import pyplot as plt


# Data
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

# Plot
plt.bar(
    [x for x in histogram.keys()],
    histogram.values(),
    8)
plt.axis([-5, 105, 0, 5])

# Style
plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decil')
plt.ylabel('Number of Students')
plt.title('Distribution of Test 1 Grades')

# Render
plt.show()
