from collections import Counter

def frequencySort(s: str) -> str:
    char_list = [char * count for char, count in Counter(s).items()]
    char_list.sort(reverse=True, key=lambda a: len(a))
    return "".join(char_list)

def test():
    assert frequencySort("tree") == "eert" or frequencySort("tree") == "eetr"
    assert frequencySort("cccaaa") == "aaaccc" or frequencySort("cccaaa") == "cccaaa"
    assert frequencySort("Aabb") == "bbAa" or frequencySort("Aabb") == "bbaA"

test()

