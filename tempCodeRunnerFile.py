i = 0
        j = 1
        k = 2
        tam = len(nums)
        while i < tam-2:
            numsi = nums[i]
            numsj = nums[j]
            numsk = nums[k]
            if numsi < numsj < numsk:
                return True
            if k < tam-1:
                k+=1
            elif j < k:
                j += 1
            else:
                i += 1
                k = i + 2
                j = i + 1
        return False