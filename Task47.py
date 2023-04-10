from random import randint
def createArray(size):
    list_1 = [randint(-5, 9) for _ in range(size)]
    return list_1


def index(my_list):
    min_elem = int(input("input the first elements of the range: "))
    max_elem = int(input("input the second elements of the range: "))
    # for i in range(len(my_list)):
    # # if min_elem <= my_list[i] <= max_elem:
    # # print(i, end=" ")
    print([i for i in range(len(my_list)) if min_elem <= my_list[i] <= max_elem])


print()
num_size = int(input("input number of elements array: "))
my_list = createArray(num_size)
print(my_list)
index(my_list)