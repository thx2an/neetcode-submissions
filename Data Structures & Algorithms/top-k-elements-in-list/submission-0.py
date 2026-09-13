class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = {}
        for number in nums:
            if number in count_num:
                count_num[number] = count_num[number] + 1 
            else:
                count_num[number] = 1
        items = list(count_num.items())
        items.sort(
            key = lambda x: x[1],
            reverse = True
        )
        return [item[0] for item in items[:k]]

        
        