from scipy import stats
import matplotlib.pyplot as plt

x = [156.3, 158.9, 160.8, 179.6, 156.6, 165.1, 165.9, 156.7, 167.8, 160.8]
y = [47.1, 46.8, 49.3, 53.2, 47.7, 49.0, 50.6, 47.1, 51.7, 47.8]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f'Anstieg: {slope}, Konstanter Faktor: {intercept}'
      f'Relationsfaktor R: {r}, p: {p}, std_err: {std_err}')


def linear_func(var_x):
    return slope * var_x + intercept


def get_ring_size(b_height):
    result = linear_func(b_height)
    print(f'If Body height {b_height}cm, then ring size: {linear_func(b_height)}')
    plt.scatter(b_height, result, marker='o', color='red')


my_model = list(map(linear_func, x))
print(my_model)

get_ring_size(150)
get_ring_size(190)

plt.scatter(x, y)
plt.plot(x, my_model)
plt.xlabel('Body Height')
plt.ylabel('Ring size')
plt.show()


