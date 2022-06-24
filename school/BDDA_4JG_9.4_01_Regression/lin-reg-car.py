from scipy import stats
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f'Anstieg: {slope}, Konstanter Faktor: {intercept}'
      f'Relationsfaktor R: {r}, p: {p}, std_err: {std_err}')


def linear_func(var_x):
    return slope * var_x + intercept


my_model = list(map(linear_func, x))
print(my_model)

plt.scatter(x, y)
plt.plot(x, my_model)
plt.xlabel('Car Age')
plt.ylabel('Speed [mph]')
plt.show()

print(f'Berechne v für ein Auto ')


