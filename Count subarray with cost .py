
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        max_dq = deque()
        min_dq = deque()

        for right in range(n):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            while left <= right:
                curr_max = nums[max_dq[0]]
                curr_min = nums[min_dq[0]]
                cost = (curr_max - curr_min) * (right - left + 1)
                
                if cost <= k:
                    break
                
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            
            ans += (right - left + 1)
            
        return ans
        