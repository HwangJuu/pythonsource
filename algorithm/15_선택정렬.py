print()
# 선택 정렬 : 정렬 알고리즘 중 쉬운 방법

# 이중 for문 사용 - 특정 위치부터 자료 값 중 최솟값의 위치를 찾은 후
# 정렬을 원하는 자리와 교환
# 정렬할 때 대부분 이중 for문을 사용
# 오름차순
def selection_sort1(list1):
    size = len(list1)

    for i in range(0, size - 1):  # 0,1,2,3 자리까지만 정렬
        # 최솟값에 대한 변수
        min_idx = i
        for j in range(i + 1, size):
            if list1[j] < list1[min_idx]:
                min_idx = j
        # for문 종료 후 최솟값의 위치를 확인
        # 찾은 최솟값과 정렬 위치를 교환
        list1[i], list1[min_idx] = list1[min_idx], list1[i]


# 내림차순
def selection_sort2(list1):
    size = len(list1)

    for i in range(0, size - 1):
        max_idx = i
        for j in range(i + 1, size):
            if list1[j] > list1[max_idx]:
                max_idx = j
        list1[i], list1[max_idx] = list1[max_idx], list1[i]


if __name__ == "__main__":
    list1 = [35, 9, 2, 85, 17]

    print("오름차순")
    selection_sort1(list1)
    print("선택 정렬 : ", list1)
    print()
    print("내림차순")
    selection_sort2(list1)
    print("선택 정렬 : ", list1)

print()
