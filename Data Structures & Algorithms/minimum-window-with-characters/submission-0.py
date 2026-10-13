class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need={}
        for ch in t:
            if ch not in need:
                need[ch]=0
            need[ch]+=1
        window={}
        have=0
        need_count=len(need)
        left=0
        min_len=float("inf")
        result=""
        for right in range(len(s)):
            ch = s[right]
            if ch in need:
                if ch not in window:
                    window[ch] = 0
                window[ch] += 1

                if window[ch] == need[ch]:
                    have += 1

            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_ch = s[left]

                if left_ch in need:
                    if window[left_ch] == need[left_ch]:
                        have -= 1
                    window[left_ch] -= 1

                left += 1

        return result
        #Time and space is O(mod(s)+ mod(t)) respectively