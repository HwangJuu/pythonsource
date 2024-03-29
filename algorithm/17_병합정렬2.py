print()
# 하나의 리스트로 작성
def merge_sort(list1):

    # 리스트 구하기
    size = len(list1)

    # 종료 조건
    if size <= 1:  # 하나만 있으면 정렬할 필요 없음
        return list1

    # 분해 작업
    mid = size // 2  # 중간 구하기

    g1 = list1[:mid]
    g2 = list1[mid:]

    merge_sort(g1)
    merge_sort(g2)

    # 병합 작업
    # 변수 사용
    i1, i2, ia = 0, 0, 0

    # 두 그룹에 자료가 남아 있을 때까지
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            list1[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            list1[ia] = g2[i2]
            i2 += 1
            ia += 1

    # 남아 있는 자료 결과에 추가
    while i1 < len(g1):
        list1[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        list1[ia] = g2[i2]
        i2 += 1
        ia += 1


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    merge_sort(list1)
    print("병합 정렬 : ", list1)


print()
