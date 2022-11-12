# Import the modules you need
import matplotlib.pyplot as plt
from scipy import stats

# Create the arrays that represent the values of the x and y axis
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Draw a scatter plot y versus x
plt.scatter(x, y)
plt.show()

# Execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)
print ("slope =", slope, "\nIntercept =", intercept)

# Create a function that uses the slope and intercept values to return a new value
# This new value represents where on the y-axis the corresponding x value will be placed
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis
mymodel = list(map(myfunc, x))

"""
Each line execute the following actions:
1. Draw the original scatter plot
2. Draw the line of linear regression
3. Display the diagram
"""
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
