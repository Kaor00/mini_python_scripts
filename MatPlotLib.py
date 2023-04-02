import matplotlib.pyplot as plt
import numpy

data = numpy.array([60, 30, 10, 10])
languages = ['Python', 'JavaScript', 'C#', 'C++']
myexplode = [0.1, 0, 0, 0]
plt.pie(data, labels=languages, explode=myexplode, shadow=True)

plt.show()
