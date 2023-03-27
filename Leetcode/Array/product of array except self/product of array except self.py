class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1

        for i in range(len(nums)):
            answer.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer