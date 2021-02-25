"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
"""
## 思路
#先遍历第一个数组，将其存到hashtable中，然后遍历第二个数组，如果在hashtable中存在就 push 到 ret，然后清空 hashtable，最后返回 ret 即可。
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        result = []
        for i in nums2:
            if i in lookup:
                result += i,
                lookup.discard(i)
        return result

#O(M + N)|O(MIN(M,N))



class Solution:
  def intersection(self, nums1, nums2):
    results = {}
    for num in nums1:
      if num in nums2 and num not in results:
        results[num] = 1
    return list(results.keys())

  def intersection2(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [x for x in set1 if x in set2]

  def intersection3(self, nums1, nums2):
    hash = {}
    duplicates = {}
    for i in nums1:
      hash[i] = 1
    for i in nums2:
      if i in hash:
        duplicates[i] = 1

    return tuple(duplicates.keys())

print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)


Python Code:

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited, result = {}, []
        for num in nums1:
            visited[num] = num
        for num in nums2:
            if num in visited:
                result.append(num)
                visited.pop(num)
        return result

    # 另一种解法：利用 Python 中的集合进行计算
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
```
**复杂度分析**
- 时间复杂度：$$O(N)$$
- 空间复杂度：$$O(N)$$