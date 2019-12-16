from matplotlib import pyplot as plt


# Data
test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

# Plot
plt.scatter(test_1_grades, test_2_grades)
# Uncomment the line bellow to correct axis
# plt.axis('equal')

# Style
plt.title('Axis are not compatible')
plt.xlabel('test 1 grades')
plt.ylabel('test 2 grades')

# Render
plt.show()
