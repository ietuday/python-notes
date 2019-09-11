def selectionSort(list):
    for i in range(len(list) - 1):
        minimum = i
        for j in range(i + 1, len(List)):
            if(List[j] < List[minimum]):
                minimum = j
        if(minimum != j):
            List[i], List[minimum] = List[minimum], List[i]
    return List


if __name__ == '__main__':
    List = [3,4,2,6,5,7,1,9]
    print('Sorted List:',selectionSort(List))
