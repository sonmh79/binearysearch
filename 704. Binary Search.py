class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. 이진 검색 재귀 풀이
        def binarysearch(left,right):
            if left <= right:
                mid = left + (right-left)//2  # overflow를 피하면서 정확한 중간값 구하기
                
                if nums[mid] > target:
                    return binarysearch(left,mid-1)
                elif nums[mid] < target:
                    return binarysearch(mid+1,right)
                else:
                    return mid
            else:
                return -1   
        return binarysearch(0,len(nums)-1)
        
        # 2. bisect 이진 검색 모듈
            index = bisect.bisect_left(nums,target)
            if index < len(nums) and nums[index] == target:
                return index
            else:
                return -1
            
                    
                
