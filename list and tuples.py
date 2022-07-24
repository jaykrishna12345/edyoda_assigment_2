lst = [(9,5),(28,7),(45,2),(73,1),(61,3),(41,8),(16,9),(23,6),(11,10),(32,4)]    # Taking some random non-empty tuple in a list
number = lst                                                                     # Assigning the values of the list to another variable

for i in range(len(number)):                                                     # Defining the range of i in number
    for j in range(i, len(number)):                                              # Defining the range of j
        if number[j][1] < number[i][1]:                                          # Comparing the last element of each tuple inside the list
            number[i], number[j] = number[j], number[i]                          # Swaping the values

print(number)
