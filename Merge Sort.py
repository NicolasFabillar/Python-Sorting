print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')
print()

def merge_sort (Numbers):
    if len(Numbers) > 1:
        #Separates the list to left and right.
        left = Numbers[:len(Numbers)//2]
        right = Numbers[len(Numbers)//2:]

        #Repeats the process of Separation.
        merge_sort(left)
        merge_sort(right)

        #Merging
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Numbers[k] = left[i]
                i += 1
            else:
                Numbers[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            Numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            Numbers[k] = right[j]
            j += 1
            k += 1
        print(Numbers)


Number_List = [71, 88, 76, 82, 52, 48, 10, 16, 30, 86]
merge_sort(Number_List)
print("\nThe result of the Bubble sort is:", Number_List)
