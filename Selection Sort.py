print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')

def sort_number (Numbers):
    for i in range(9):
        min_pos = i

        #Finds the position of the minimum value.
        for j in range(i, 10):
            if Numbers[min_pos] > Numbers[j]:
                min_pos = j

        #Perform the swapping.
        Numbers[min_pos], Numbers[i] = Numbers[i], Numbers[min_pos]

        #Prints the number list after the swap.
        print("After",i + 1, "iteration(s), the sequence is:",Numbers)

Number_List = [71, 88, 76, 82, 52, 48, 10, 16, 30, 86]
sort_number(Number_List)

print("\nThe result of the Selection sort is:", Number_List)