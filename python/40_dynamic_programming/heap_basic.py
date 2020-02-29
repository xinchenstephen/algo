#堆的基本操作
#堆是一个完全二叉树，插入和删除操作的时间复杂度都为LOG(n),堆排序操作
#堆一般用数组排序
import random
import numpy as np

class maxheap():
    def __init__(self,array):
        #从0开始计堆的数组
        self.heap = array
        self.size = len(self.heap)
        self.establish_heap()
        #为了数比较个数的
        # self.count = 0
    def establish_heap(self):
        #用无序数组建立堆
        n = len(self.heap)
        for i in range(n//2,-1,-1):
            self.siftdown(i)
    def siftdown(self,i):
        #将self.heap[i]沉到底
        #先设i为最大值
        maxindex = i
        if (self.left(i) < self.size) and (self.heap[maxindex] < self.heap[self.left(i)]):
            maxindex = self.left(i)
        if (self.right(i) < self.size) and (self.heap[maxindex] < self.heap[self.right(i)]):
            maxindex = self.right(i)
        if (maxindex != i):
            self.heap[i],self.heap[maxindex] = self.heap[maxindex],self.heap[i]
            # self.count += 1
            self.siftdown(maxindex)
    def siftup(self,i):
        #将self.heap[i]升上去
        while (i >0 and (self.heap[self.parent(i)] < self.heap[i])):
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)
    def parent(self,i):
        return (i - 1)//2
    def left(self,i):
        return 2*i + 1
    def right(self,i):
        return 2*i + 2
    def insert(self,val):
        self.size += 1
        self.heap.append(val)
        self.siftup(self.size - 1)
    def extractmax(self):
        minnum = self.heap[0]
        self.heap[0],self.heap[self.size - 1] = self.heap[self.size - 1],self.heap[0]
        del self.heap[self.size - 1]
        #要注意同时改变堆的size!
        self.size -= 1
        self.siftdown(0)
        return minnum
    def heap_sort(self):
        #做(a - 1)次交换
        a = self.size
        for i in range(a - 1):
            #交换最后一个和第一个
            self.heap[0],self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            # self.count += 1
            self.size -= 1
            self.siftdown(0)
        ############################要注意恢复现场！
        self.size = len(self.heap)
        return self.heap
    def __repr__(self):
        print(self.heap)
        return ""

class minheap():
    def __init__(self,array):
        #从0开始计堆的数组
        self.heap = array
        self.size = len(self.heap)
        self.establish_heap()
        #为了数比较个数的
        # self.count = 0
    def establish_heap(self):
        #用无序数组建立堆
        n = len(self.heap)
        for i in range(n//2,-1,-1):
            self.siftdown(i)
    def siftdown(self,i):
        #将self.heap[i]沉到底
        #先设i为最大值
        minindex = i
        if (self.left(i) < self.size) and (self.heap[minindex] > self.heap[self.left(i)]):
            minindex = self.left(i)
        if (self.right(i) < self.size) and (self.heap[minindex] > self.heap[self.right(i)]):
            minindex = self.right(i)
        if (minindex != i):
            self.heap[i],self.heap[minindex] = self.heap[minindex],self.heap[i]
            # self.count += 1
            self.siftdown(minindex)
    def siftup(self,i):
        #将self.heap[i]升上去
        while (i >0 and (self.heap[self.parent(i)] > self.heap[i])):
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)
    def parent(self,i):
        return (i - 1)//2
    def left(self,i):
        return 2*i + 1
    def right(self,i):
        return 2*i + 2
    def insert(self,val):
        self.size += 1
        self.heap.append(val)
        self.siftup(self.size - 1)
    def getmin(self):
        return self.heap[0]
    def extractmin(self):
        minnum = self.heap[0]
        self.heap[0],self.heap[self.size - 1] = self.heap[self.size - 1],self.heap[0]
        del self.heap[self.size - 1]
        #要注意同时改变堆的size!
        self.size -= 1
        self.siftdown(0)
        return minnum
    def heap_sort(self):
        #做(a - 1)次交换
        a = self.size
        for i in range(a - 1):
            #交换最后一个和第一个
            self.heap[0],self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            # self.count += 1
            self.size -= 1
            self.siftdown(0)
        ############################要注意恢复现场！
        self.size = len(self.heap)
        return self.heap[::-1]
    def __repr__(self):
        print(self.heap)
        return ""

nums = list(range(10))
random.shuffle(nums)
heap1 = minheap(nums)
print(heap1)
heap1.establish_heap()
print(heap1)
heap1.insert(18)
print(heap1)
print(heap1.heap_sort())
print(heap1.size)


# np.random.seed(1)
# array = np.random.randint(0,100,50)
# heap1 = heap(array)
# heap1.establish_heap()
# heap1.count = 0
# heap1.heap_sort()
# print(heap1.count)