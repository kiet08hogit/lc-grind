class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right= len(numbers)-1
        left= 0
        while left <= right:
            compare = numbers[right] + numbers[left]
            if compare > target:
                right-=1
            elif compare < target:
                left+=1
            else:
                break
        return [left+1,right+1]
