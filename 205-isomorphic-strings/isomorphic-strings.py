class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in map_st:
                if map_st[ch1] != ch2:
                    return False
            else:
                map_st[ch1] = ch2
            if ch2 in map_ts:
                if map_ts[ch2] != ch1:
                    return False
            else:
                map_ts[ch2] = ch1
        return True
            