print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')
print()

def quick_sort (Numbers):
    if len(Numbers) > 1:
        pivot = Numbers.pop()
        left = []
        right = []

        for Value in Numbers:
            if pivot <= Value:
                right.append(Value)
            else:
                left.append(Value)

        return quick_sort(left) + [pivot] + quick_sort(right)

    else:
        return Numbers

Number_List = [71, 88, 76, 82, 52, 48, 10, 16, 30, 86]
Number_List = quick_sort(Number_List)
print("The result of the Quick sort is:", Number_List)