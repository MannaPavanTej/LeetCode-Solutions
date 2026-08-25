class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        target = tickets[k]
        
        for i, count in enumerate(tickets):
            if i <= k:
                total_time += min(count, target)
            else:
                total_time += min(count, target - 1)
                
        return total_time