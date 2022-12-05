class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        dif = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]


def test():
    sol = Solution()
    assert sol.buddyStrings("abc", "bac") is True
    assert sol.buddyStrings("ab", "ba") is True
    assert sol.buddyStrings("aaaaab", "aaaaba") is True
    assert sol.buddyStrings("abc", "aba") is False
    assert sol.buddyStrings("aa", "aa") is True
    assert sol.buddyStrings("ab", "ab") is False
    assert sol.buddyStrings("abcaa", "abcbb") is False

test()
