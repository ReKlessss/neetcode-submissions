class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        most_frequent = []

        for i in nums:
            counts[i] += 1

        for key, val in counts.items():
            buckets[val].append(key)

        for num_list in reversed(buckets):
            for num in num_list:
                most_frequent.append(num)
                if len(most_frequent) == k:
                    return most_frequent

        return []