class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. 투 포인터
        
        left, right =0, len(numbers)-1  
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
                
        # 2 .이진 검색 속도 개선
        for i,v in enumerate(numbers):
            expected = target - v
            #bisect 왼쪽 범위 제한으로 속도 개선
            e = bisect.bisect_left(numbers,expected,i+1)
            if e < len(numbers) and numbers[e] == expected :
                return i+1,e+1
            
