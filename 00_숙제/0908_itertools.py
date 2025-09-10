from itertools import permutations

numbers = [1, 2, 3, 4]

permutations(numbers, 3)    # 순열

# ----------

from itertools import product

numbers = [1, 2, 3, 4]

product(numbers, repeat=3)  # 중복순열

# ----------

from itertools import combinations

numbers = [1, 2, 3, 4]

combinations(numbers, 3)    # 조합

# ----------

from itertools import combinations_with_replacement

numbers = [1, 2, 3, 4]

combinations_with_replacement(numbers, 3)   # 중복조합