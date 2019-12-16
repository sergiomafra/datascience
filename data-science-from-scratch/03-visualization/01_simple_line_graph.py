from matplotlib import pyplot as plt


# Data to plot
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Plot and style the graphic
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.plot(years, gdp, color='red', marker='o', linestyle='solid')
plt.title('GDP Nominal')
plt.ylabel('Billions of $')
plt.xlabel('Years')

# Show the graphic
plt.show()
