from matplotlib import pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 10, 20, 30, 40, 50]
y2 = [0, 15, 30, 45, 60, 75]

plt.figure()
plt.plot(x, y1, color='pink', linestyle='-', marker='o')
plt.plot(x, y2, color='gray', linestyle='-', marker='o')
plt.title('Two Lines on One Graph')
ax = plt.subplot()
ax.set_xlabel('Amazing X-axis')
ax.set_ylabel('Incredible Y-axis')
plt.legend(['a', 'b'], loc=4)
plt.show()