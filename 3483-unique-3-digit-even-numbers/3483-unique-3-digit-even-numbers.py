class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = Counter(digits)
        count = 0

        # Check all valid 3-digit even numbers
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            num_counts = Counter([d1, d2, d3])

        # Verify if all digits in num can be formed using given digits
            if all(digit_counts[d] >= num_counts[d] for d in num_counts):
                count += 1

        return count