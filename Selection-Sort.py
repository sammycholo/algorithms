###SELECTION SORT###
#1 We start with an unsorted array X = [7, 4, 10, 8, 3, 1]. Initially, our sorted array is empty, represented by [None].

#2A Finding the smallest value:
#2B We find the smallest value in the unsorted array, which is 1. We swap it with the value at X[0] (7). Now, our sorted subarray becomes [1], and the unsorted subarray becomes [4, 10, 8, 3, 7].

#3AFinding the next smallest value:
#3BNext, we find the smallest value in the unsorted subarray, which is 3. We swap it with the value at X[0] in the unsorted subarray. Now, our sorted subarray becomes [1, 3], and the unsorted subarray becomes [10, 8, 4, 7].

#4A Finding the next smallest value:
#4B We continue this process and find the smallest value in the unsorted subarray, which is 4. We swap it with the value at X[0] in the unsorted subarray. Now, our sorted subarray becomes [1, 3, 4], and the unsorted subarray becomes [10, 8, 7].

#5A Finding the next smallest value:
#5B Again, we find the smallest value in the unsorted subarray, which is 7. We swap it with the value at X[0] in the unsorted subarray. Now, our sorted subarray becomes [1, 3, 4, 7], and the unsorted subarray becomes [10, 8].

#6A Finding the next smallest value:
#6B We find the smallest value in the remaining unsorted subarray, which is 8. We swap it with the value at X[0] in the unsorted subarray. Now, our sorted subarray becomes [1, 3, 4, 7, 8], and the unsorted subarray becomes [10].

#7A Finding the final smallest value:
#7B Finally, we find the smallest value in the last unsorted subarray, which is 10. We swap it with the value at X[0] in the unsorted subarray. Now, our sorted subarray becomes [1, 3, 4, 7, 8, 10], and the unsorted subarray becomes empty.

#8 The sorting process is complete, and we have the sorted array [1, 3, 4, 7, 8, 10].
""""
Real World Example (Generated by ChatGPT)
A real-world example of selection sort can be sorting a deck of playing cards. Let's say you have a messy deck of cards with different ranks and suits that you want to sort in ascending order.

To apply selection sort to this scenario:

1.Start with the unsorted deck of cards.
2.Find the card with the smallest rank (e.g., Ace of Spades) from the unsorted portion of the deck.
3.Swap this card with the card at the beginning of the unsorted portion (e.g., the card at the top of the deck).
4.Now, the first card in the deck is in its correct position.
5.Repeat steps 2 to 4, but this time considering the remaining unsorted portion of the deck.
6.Find the card with the smallest rank from the remaining unsorted portion.
7Swap it with the card following the previously sorted cards.
8.Repeat this process until all the cards are sorted.
9.By following these steps, you are essentially performing a selection sort on the deck of cards. Each iteration selects the card with the smallest rank from the remaining unsorted portion and places it in the correct position in the sorted portion.

This real-world example demonstrates how selection sort works by repeatedly finding the minimum element and swapping it with the appropriate position, just like how you would sort a deck of playing cards by selecting the smallest card and placing it in its correct spot.
"""
#Code With Comments
def selection_sort(array): #function defination
    print("orignal array :", array) #printing original array to check
    for index in range(len(array)): #outer loop means for every element in array#
        min_index = index 		#index of smallest value
        for j in range(index,len(array)): #inner loop for comparison; index w index+1 to len(array)
            if array[min_index] > array[j]: #if array’s smallest value is greater than next val then tha
                min_index = j		#updates smallest value 
                j = j+1			#increments
        array[min_index], array[index] = array[index], array[min_index] #swapping smallest with the first element of the unsorted sub array
        print("After Pass#",index+1," ", array) #check; prints array after every pass
            
            
arr1 = [7,4,10,8,3,1] #array test 1
arr2 = [7,7,10,8,3,3,1] #array test 2
arr3 = [1,2,3,4,6,5] #array test 3
x = selection_sort(arr1) #function call 1
x = selection_sort(arr2) #function call 2
x = selection_sort(arr3) #function call 3

#Follow Me On LinkedIn @realsammye and Twitter @realsammye
