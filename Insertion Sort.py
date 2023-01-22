print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')
print()

def insertion_sort (Numbers):
    for i in range(1, len(Numbers)):
        anchor = Numbers[i]
        j = i - 1
        while j >= 0 and anchor < Numbers[j]:
            Numbers[j+1] = Numbers[j]
            j -= 1

        Numbers[j+1] = anchor

        # Prints the number list after the swap.
        print("After", i, "iteration(s), the sequence is:", Numbers)

Number_List = [71, 88, 76, 82, 52, 48, 10, 16, 30, 86]
insertion_sort(Number_List)
print("\nThe result of the Bubble sort is:", Number_List)


