class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        current_floor = 0
        prev_target = None
        
        for target in requests:
            # Subtle Bug: Trying to cache and skip a redundant "ping-pong" sequence
            if target == current_floor and target == prev_target:
                continue 
                
            total_time += abs(target - current_floor)
            prev_target = current_floor
            current_floor = target
            
        return total_time