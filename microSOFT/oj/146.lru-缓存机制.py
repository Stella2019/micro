#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.27%)
# Likes:    1183
# Dislikes: 0
# Total Accepted:    133.8K
# Total Submissions: 258.8K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 
# 
# 
# 实现 LRUCache 类：
# 
# 
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 
# 
# 
# 
# 
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 最多调用 3 * 10^4 次 get 和 put
# 
# 
#### 思路: 哈希法

1. 确定需要使用的数据结构
   1. 根据题目要求,存储的数据需要保证顺序关系(逻辑层面) ===> 使用数组,链表等保证顺序关系
   2. 同时需要对数据进行频繁的增删, 时间复杂度 O(1) ==> 使用链表等
   3. 对数据进行读取时, 时间复杂度 O(1) ===> 使用哈希表
      最终采取双向链表 + 哈希表
      > 1. 双向链表按最后一次访问的时间的顺序进行排列, 链表头部为最近访问的节点
      > 2. 哈希表,以关键字为键,以链表节点的地址为值
2. put 操作
   通过哈希表, 查看传入的关键字对应的链表节点, 是否存在
   1. 如果存在,
      1. 将该链表节点的值更新
      2. 将该该链表节点调整至链表头部
   2. 如果不存在
      1. 如果链表容量未满,
         1. 新生成节点,
         2. 将该节点位置调整至链表头部
      2. 如果链表容量已满
         1. 删除尾部节点
         2. 新生成节点
         3. 将该节点位置调整至链表头部
      3. 将新生成的节点，按关键字为键，节点地址为值插入哈希表
3. get 操作
   通过哈希表, 查看传入的关键字对应的链表节点, 是否存在
   1. 节点存在
      1. 将该节点位置调整至链表头部
      2. 返回该节点的值
   2. 节点不存在, 返回 null


# @lc code=start
class LRUCache:
  def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

  def get(self, key):
    if key not in self.dic:
        return -1
    v = self.dic.pop(key) 
    self.dic[key] = v   # set key as the newest one
    return v

  def set(self, key, value):
    if key in self.dic:    
        self.dic.pop(key)
    else:
        if self.remain > 0:
            self.remain -= 1  
        else:  # self.dic is full
            self.dic.popitem(last=False) 
    self.dic[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

import collections
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
            
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
                
        self.cache[key] = value