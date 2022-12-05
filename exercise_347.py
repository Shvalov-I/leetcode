from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    print(freq)
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    print(count)
    for n, c in count.items():
        freq[c].append(n)
    print(freq)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def test():
    assert topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert topKFrequent(nums=[1], k=1) == [1]
    assert topKFrequent(nums=[3, 0, 1, 0], k=1) == [0]
    assert topKFrequent([4, 1, -1, 2, -1, 2, 3], 2) == [-1, 2]


# test()
print(topKFrequent(nums=[3, 0, 1, 0], k=1))
print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
