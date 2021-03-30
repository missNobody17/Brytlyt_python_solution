"""
This program compares two queries, if they are in the same class,
it prints True, if not prints False
"""


def check_queries(q1, q2):
    arr1 = q1.split("\n")  # input to compare split by new line
    arr2 = q2.split("\n")  # second input to compare
    count = 0  # number of the same expressions
    print("comparing ", end=' ')
    print(arr1, end=' ')
    print("and", end=' ')
    print(arr2)
    for i in range(len(arr1)):
        if len(arr1) != len(arr2):  # check if a1 and a2 have the same length
            break
        if arr1[i] == arr2[i]:  # check if both are the same
            count += 1
        elif arr1[i].startswith("MAX") and arr2[i].startswith("MAX"):  # if they are not check if the word starts with 'max'
            count += 1
        elif arr1[i].startswith("col") and arr2[i].startswith("col"):  # if they are not check if the word starts with 'col'
            count += 1
    if count == len(arr1):  # if lengths are the same print true
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    a1 = 'SELECT\nMAX(col_1)\nFROM\ntable'
    a2 = 'SELECT\nMAX(col_1 + 1)\nFROM\ntable'
    a3 = 'SELECT\nMAX(col_2)'
    a4 = 'SELECT\nMAX(col_1)\nFROM\ntable\nGROUP_BY\ncol_2'
    a5 = 'SELECT\nMAX(col_1 + 1)\nFROM\ntable\nGROUP_BY\ncol_3'
    a6 = 'SELECT MAX(col_1 + 2)\nFROM\ntable\nGROUP_BY\ncol_2'
    a7 = 'SELECT\nMAX(col_1)\nFROM\ntable\nGROUP_BY\ncol_3'
    check_queries(a1, a2)
    check_queries(a2, a3)
    check_queries(a4, a5)
    check_queries(a5, a6)
    check_queries(a4, a7)


