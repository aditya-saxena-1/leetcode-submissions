class Solution(object):
    def sortedSquares(self, nums):
        neg = []
        pos = []
        res = []
        i = j = 0

        #2 sub arrays
        for num in nums:
            if num < 0:
                neg.append(num)
            if num >= 0:
                pos.append(num)

        #Case 1: no negative element
        if len(neg) == 0:
            return [x*x for x in pos]

        #Case 2: no positive element
        if len(pos) == 0:
            arr = neg[::-1]
            return [x*x for x in arr]

        #Case 3: both elements
        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]

        while i < len(neg) and j < len(pos):
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        
        while i < len(neg):
            res.append(neg[i])
            i += 1
        
        while j < len(pos):
            res.append(pos[j])
            j += 1
        
        return res