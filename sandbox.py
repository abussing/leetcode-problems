

from typing import Optional, List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        
        leftptr = 0
        rightptr = 1

        ourdict = {s[leftptr]: leftptr}
        currentlen = 1
        maxlen = currentlen

        while rightptr < len(s):
            char = s[rightptr]
            if char in ourdict and ourdict[char] >= leftptr:
                currentlen -= ourdict[char] - leftptr
                leftptr = ourdict[char] + 1
            else:
                currentlen += 1

            maxlen = max(currentlen, maxlen)
            
            ourdict[char] = rightptr
            
            rightptr += 1

        return maxlen
        
    
what = Solution().lengthOfLongestSubstring(s="abcacdba")


what

