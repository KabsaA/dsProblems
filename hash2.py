




def twoSum(nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """

      dict = {}
      for i,num in enumerate(nums):
          if target - num in seen:
              return [seen[target-num],i]
          elif num not in seen:
              seen[num] = i







      # for i in range(len(nums)):
      #     for j in range(i+1,len(nums)):
      #         sum = nums[i] + nums[j]
      #         if sum == target:
      #             return [i,j]


nums = [7,3,2,4]
target = 11
print(twoSum(nums,target))
