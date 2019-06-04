"""
排序 - 冒泡排序、选择排序、归并排序、快速排序
冒泡排序 - O(n ** 2)：两两比较，大的下沉
35, 97, 12, 68, 55, 73, 81, 40
35, 12, 68, 55, 73, 81, 40, [97]
12, 35, 55, 68, 73, 40, [81]
12, 35, 55, 68, 40, [73]
...
选择排序 - O(n ** 2)：每次从剩下元素中选择最小
-----------------------------------------
归并排序 - O(n * log_2 n) - 高级排序算法
35, 97, 12, 68, 55, 73, 81, 40
[35, 97, 12, 68], [55, 73, 81, 40]
[35, 97], [12, 68], [55, 73], [81, 40]
[35], [97], [12], [68], [55], [73], [81], [40]
[35, 97], [12, 68], [55, 73], [40, 81]
[12, 35, 68, 97], [40, 55, 73, 81]
[12, 35, 40, 55, 68, 73, 81, 97]
-----------------------------------------
快速排序 - 以枢轴为界将列表中的元素划分为两个部分，左边都比枢轴小，右边都比枢轴大
35, 97, 12, 68, 55, 73, 81, 40
35, 12, [40], 68, 55, 73, 81, 97
[12], 35, [40], 68, 55, 73, 81, [97]
[12], 35, [40], 55, [68], 73, 81, [97]
[12], 35, [40], 55, [68], 73, [81], [97]
"""


A = [35, 97, 12, 68, 55, 73, 81, 40]


def bubble_sort(array_list):
    index = 0
    while True:
        if not isinstance(array_list[index],int):
            print('Do not int model. Please retry')

        if index == 0:
            index = index + 1
            continue
        if array_list[index] < array_list[index - 1]:
            array_list[index -1 ] , array_list[index] = array_list[index] ,array_list[index -1 ]
            index = 0
            continue
        else:
            index = index + 1


        if index == len(array_list):
            break
    return array_list

def sort(items ,start , end):

    count = 0

    value = items[end]
    temp = items.copy()

    for index in range(start, end):
        if temp[index] > value :
            items.insert(end + 1,temp[index])
            del items[index-count]
            count =count + 1

    return end - count



def quick_sort(arrary_list,start,end):

    if start < end:
        pos = sort(arrary_list,start, end)
        quick_sort(arrary_list,start,pos -1)
        quick_sort(arrary_list,pos+1,end)




    return arrary_list







if __name__ == '__main__':
    print(quick_sort(A,0,7))








