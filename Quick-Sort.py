def quick_sort(array):
    if len(array) == 0: #Basic check for list with zero element
        return array #Return Array
    elif len(array) == 1:
        return array #Return Array (smallest solution)
    pivot = array[len(array) // 2]  #chose middle or any other element
    print("Pivot Value", pivot) #Basic Check Print
    smaller = [] #for smaller values than the pivot value
    equal = [] #for pivot value and equal values
    larger = [] #for larger vales than the pivot value
    
    print("Smaller Than Pivot List:", smaller) #Initial list sate; for understanding
    print("Pivot/Equal List:", equal) #Initial list sate; for understanding
    print("Larger Than Pivot List:",larger) #Initial list sate; for understanding
    print("Input Array Initial Sate:",array) #Initial list sate; for understanding
    
    for element in array: #for each element in array check conditions
        if element < pivot: #if value of element < pivot value
            smaller.append(element) #append smaller list with the element
        elif element == pivot: #if value of element equal(==) to pivot value
            equal.append(element) #append the equal list with the element
        else:                       #other case is if value of element is greater than > pivot value
            larger.append(element) #append the larger list with the element
        print("Smaller List State After Iteration",smaller)
        print("Pivot/Equal List State After Iteration", equal)
        print("Larger List State After Iteration", larger,"\n")
    print("----Recursive Call----")
    return quick_sort(smaller) + equal + quick_sort(larger) #recursive call


my_array = [7, 4, 10, 8, 3, 1]
x=quick_sort(my_array)
print("---SORTED LIST/ARRAY---","\n",x)
"""
Real World Example (Generated By Chatgpt)
Initial Deck: Let's start with an unsorted deck of cards:

[8 ♠, 3 ♥, 10 ♣, 2 ♦, 7 ♠, 5 ♣, 9 ♦, 4 ♥, 6 ♦, 1 ♠]

Choosing a Pivot: We select a pivot element from the deck. In this example, let's choose the middle card as the pivot:

Pivot: 7 ♠

Partitioning the Deck: We partition the deck based on the pivot, placing cards smaller than the pivot to the left and cards greater than the pivot to the right:

[3 ♥, 2 ♦, 5 ♣, 4 ♥, 6 ♦, 1 ♠] [7 ♠] [8 ♠, 10 ♣, 9 ♦]

Note that the pivot itself is in the correct sorted position.

Recursive Calls: We recursively apply the Quicksort algorithm to the two partitions on the left and right of the pivot.

Left Partition: [3 ♥, 2 ♦, 5 ♣, 4 ♥, 6 ♦, 1 ♠]

Pivot: 3 ♥
Partition: [2 ♦, 1 ♠] [3 ♥] [5 ♣, 4 ♥, 6 ♦]
Right Partition: [8 ♠, 10 ♣, 9 ♦]

Pivot: 8 ♠
Partition: [8 ♠] [10 ♣, 9 ♦]
Continuing Recursion: We continue applying the Quicksort algorithm recursively to the partitions until we reach single-card partitions (which are already sorted).

Left Partition: [2 ♦, 1 ♠]

Both cards are already sorted.
Right Partition: [5 ♣, 4 ♥, 6 ♦]

Pivot: 5 ♣
Partition: [4 ♥] [5 ♣] [6 ♦]
Right Partition: [10 ♣, 9 ♦]

Both cards are already sorted.
Final Sorted Deck: Once all the recursive calls are completed, we combine the sorted partitions:

[1 ♠, 2 ♦, 3 ♥, 4 ♥, 5 ♣, 6 ♦, 7 ♠, 8 ♠, 9 ♦, 10 ♣]


"""