#题目地址：https://time.geekbang.org/column/article/74788
#几种算法
#第一种：暴力回溯
from typing import List
least = float("inf")
def yh_triangle(level,levelnum,num,yhlist):
    #level表示现在是访问第几层
    #levelnum表示现在是对这一层的第几个元素进行访问
    #num是指到这里走的路径长度
    #yhlist是储存的杨辉三角的数组
    global least
    if (level == len(yhlist) - 1):
        if num < least:
            least = num
            return
    else:
        #访问下一层的数组，只能访问levelnum和levelnum+1
        yh_triangle(level+1,levelnum,num + yhlist[level + 1][levelnum],yhlist)
        yh_triangle(level+1,levelnum + 1, num + yhlist[level+1][levelnum + 1],yhlist)
#动态规划，从下到上的办法
def yh_triangle(yhlist):
    n = len(yhlist)
    res = [[0]*i for i in range(1,n+1)]
    #对第0层的元素先赋值
    res[0][0] = yhlist[0][0]
    for j in range(1,n):
        #对每一层而言，第一个和最后一个元素特殊对待
        for i in range(j+1):
            if (i == 0):
                res[j][i] = res[j - 1][i] + yhlist[j][i]
            elif (i == j):
                res[j][i] = res[j - 1][i - 1] + yhlist[j][i]
            else:
                res[j][i] = min(res[j - 1][i - 1] + yhlist[j][i], res[j - 1][i] + yhlist[j][i])
    print(res)
    return min(res[-1])
def yh_triangle_bottom_up(nums) -> int:
    assert len(nums) > 0
    n = len(nums)
    memo = nums[-1].copy()

    for i in range(n-1, 0, -1):
        for j in range(i):
            memo[j] = min(memo[j] + nums[i-1][j], memo[j+1] + nums[i-1][j])
    return memo[0]


if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    # yh_triangle(0,0,3,nums)
    # print(least)
    print(yh_triangle(nums))
    # print(yh_triangle_space_optimization(nums))
    print(yh_triangle_bottom_up(nums))
