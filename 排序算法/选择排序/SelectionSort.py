from typing import List

class Solution:
    def SelectionSort(self, Nums: List[int], N: int) -> List[int]:
        for i in range(N-1):
            MinPosition = i
            for j in range(i+1, N):
                if Nums[j] < Nums[MinPosition]:
                    MinPosition = j
            Nums[i], Nums[MinPosition] = Nums[MinPosition], Nums[i]

        return Nums


if __name__ == "__main__":
    Nums = [29, 10, 14, 37, 13]
    N = len(Nums)
    sort = Solution()
    #实例化

    NumsSort = sort.SelectionSort(Nums, N)
    print(NumsSort)
