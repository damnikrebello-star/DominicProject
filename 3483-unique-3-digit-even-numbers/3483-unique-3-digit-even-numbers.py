from collections import Counter
from typing import List


class Solution:

  def totalNumbers(self, digits: List[int]) -> int:
    counts = Counter(digits)
    valid_count = 0

    for num in range(100, 1000, 2):
      d1 = num // 100
      d2 = (num // 10) % 10
      d3 = num % 10

      needed = Counter([d1, d2, d3])

      if all(counts[d] >= count for d, count in needed.items()):
        valid_count += 1

    return valid_count