print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')
print()


def bubble_sort (Numbers):
    iter = 1
    for i in range(len(Numbers)-1, 0, -1):
        for j in range(i):
            if Numbers[j] > Numbers[j + 1]:
                Numbers[j], Numbers[j+1] = Numbers[j+1], Numbers[j]

        print("After", iter, "iteration(s), the sequence is:", Numbers)
        iter += 1

Number_List = [71, 88, 76, 82, 52, 48, 10, 16, 30, 86]
bubble_sort(Number_List)

print("\nThe result of the Bubble sort is:", Number_List)