class TestStr:
    def strStr(self, haystack: str, needle: str) -> int:
        print(haystack.find(needle))
        return haystack.find(needle)

    def test_str(self):
        assert self.strStr("hello", "ll") == 2
        assert self.strStr("aaaaa", "bba") == -1
        assert self.strStr("aabbasdbba", "bba") == 2
