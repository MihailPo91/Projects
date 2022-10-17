class Solution(object):
    def twoSum(self, nums, target):
        first_idx = None
        second_idx = None
        if target == 0:
            to_return = []
            for n in range(len(nums)):
                if nums[n] == 0:
                    to_return.append(n)
            if to_return:
                return to_return
            else:
                for n in range(len(nums)):
                    if nums[n] < target:
                        first_idx = n
                        for m in range(n + 1, len(nums)):
                            if nums[n] + nums[m] == target:
                                second_idx = m
                                break
                        if first_idx is not None and second_idx is not None:
                            break
                return [first_idx, second_idx]

        for n in range(len(nums)):
            if nums[n] < target:
                first_idx = n
                for m in range(n+1, len(nums)):
                    if nums[n] + nums[m] == target:
                        second_idx = m
                        break
                if first_idx is not None and second_idx is not None:
                    break
            elif nums[n] == target:
                first_idx = n
                for m in range(n+1, len(nums)):
                    if nums[m] == 0:
                        second_idx = m
                        break
                if first_idx is not None and second_idx is not None:
                    break
            else:
                first_idx = n
                for m in range(n+1, len(nums)):
                    if nums[n] + nums[m] == target:
                        second_idx = m
                        break
                if first_idx is not None and second_idx is not None:
                    break

        return [first_idx, second_idx]


s = Solution()
print(s.twoSum([-1,-2,-3,-4,-5], -8))