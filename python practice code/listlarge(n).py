def largest_num(lst):
    largest=lst[0]
    for number in lst[1:]:
        if number>largest:
            largest=number
    return largest
        
numbers=[4,7,1,8,3]
print(largest_num(numbers))