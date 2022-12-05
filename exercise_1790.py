def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    dif = [(a, b) for a, b in zip(s1, s2) if a != b]
    return len(dif) == 2 and dif[0] == dif[1][::-1]


def test():
    assert areAlmostEqual("bank", "kanb") is True
    assert areAlmostEqual("attack", "defend") is False
    assert areAlmostEqual("kelb", "kelb") is True

test()