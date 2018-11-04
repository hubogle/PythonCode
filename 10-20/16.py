# -*- coding: utf-8 -*-
# File  : 16.py
# Author: HuWenBo
# Date  : 2018/11/4
# 016：最接近的三数之和
class Solution:
    def threeSumClosest(self, nums, target):
        """
        双指针，来进行判断。
        当nums[i] + nums[n-1] + nums[n-2] < target：大于当前nums[i]和最大
        当nums[i] + nums[i+1] + nums[i+2] > target：小于当前nums[i]和最小
        也就是nums[i] + nums[i+1] + nums[i+2] < target < nums[i] + nums[n-1] + nums[n-2]
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        result = []
        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1
            if num + nums[r] + nums[r - 1] < target:
                result.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l + 1] > target:
                result.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:  # 不断调整l和r进行判断
                    result.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        print(target)
                        return target
        result.sort(key=lambda x: abs(x - target))
        return result[0]


if __name__ == '__main__':
    solution = Solution()
    solution.threeSumClosest([-1, 2, 1, -4, 1, 3, 2, 5, 4, 3, 2, 9, 4], 7)

"""
        
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1
						
            # different with others' solution
						
            if num+nums[r]+nums[r-1] < target:
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
                closest.append(num+nums[l]+nums[l+1])
            else:
                while l < r:
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1
                    elif num+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        return target
                    
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]
            
"""
