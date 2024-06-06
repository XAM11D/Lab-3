def task1(my_list):
    my_list.insert(1,-5)
    min_element=min(my_list)
    max_element=max(my_list)
    my_list.insert(2,[1,2,3])
    my_list.append("Прізвище ім'я")
    list_length=len(my_list)
    print ("my list", my_list)
    print("min element", min_element)
    print("max element", max_element)
    print("list length", list_length)

    return my_list, min_element, max_element, list_length


def task2(A, B, C):
    total_cost=sum([quantity * price for quantity, price in zip(B, C)])
    average_price=sum(C)/len(C)
    max_stocked_index=B.index(max(B))
    most_stocked_item=A[max_stocked_index]

    return total_cost, average_price, most_stocked_item


def task3():
    A1=[i for i in range(1, 26)]
    A2=[i for i in range (-25, 0)]

    return A1, A2


def task4(my_string):
    count_a= my_string.count('a')
    return count_a

def task5(my_string):
    modified_str= my_string.replace("GOOD", "NICE")
    word_count= len(my_string.split())
    return modified_str, word_count

def task6():
    list=[1,2,3,4,5]
    total_sum=sum(list)
    return total_sum


def task7(my_list):
    result=[num for num in my_list if num % 7 ==0 and num % 5 ==0]
    return result

