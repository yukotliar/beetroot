# Створити список з рандомних чисел рандомної довжини.
# Відфільтрувати його за функцією 5 < x < 50. Застосувати до списку корінь з заокругленням до 2 знаків після коми.

import random
import math

numbers = [random.randrange(100) for i in range(100)]
filtered_numbers = list(filter(lambda x: 5 < x < 50, numbers))
mapped_numbers = list(map(lambda x: round(math.sqrt(x), 2), filtered_numbers))
