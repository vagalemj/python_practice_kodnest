'''
Question: What is list slicing?
Aanswer: method to extract a subset of elements from a list

Syntax: list[start:stop:step]
- start: index of the first element to include in the subset
- stop: index of the first element to exclude from the subset
- step: increment between elements in the subset

reverse List : list[start:stop:step] = list[start:stop:step][::-1]

'''

# example for list slicing
my_list = [1, 2, 3, 4, 5, 6]
sub_list1 = my_list[::]
print(sub_list1)  # Output: [2, 3, 4]

sub_list2 = my_list[1:4]
print(sub_list2)  # Output: [2, 3, 4]

sub_list3 = my_list[1:]
print(sub_list3)  # Output: [2, 3, 4, 5]

sub_list4 = my_list.reverse()
print(sub_list4)  # Output: None

sub_list5 = my_list[::-1]
print(sub_list5)  # Output: [6, 5, 4, 3, 2, 1]

sub_list5 = my_list[-1]
print(sub_list5)  # Output: 6

