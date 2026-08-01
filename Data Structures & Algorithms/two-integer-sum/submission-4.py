class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        out=[0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    output.append(i)
                    output.append(j)
                    return output
        return []