File 1: customSort: The challenge was to write a function that sorts a list of dictionaries based on a specific key.For this challenge I created two different functions, one for an ascending sort and one for descending sort. For the ascending sort We begin by defining a function 'sort_dict_list' and assigning it two parameters 'dict_list' for the list of dictionaries and 'key' for the key values we'll use to sort the list. We use python's inbuilt sort function to return a sorted list based on the key value(an integer), we pass a list of dictionaries to test the function, the key value in the dictionaries is 'score' with reps integers of the students scores. to finish we define a variable to store the result of the function(the sorted list), we then print it to see the result. For the Desc order function we replicate what we have done above here, the only change we make is in the return function where we add an inbult reverse function and set it to true, this takes the sorted list(initially in ascending) and reverses the output, making it in descending order.

Problem Solved(customSort):
1. Write a function that sorts a list of dictionaries based on a specific key.

File 2: We were required to develop an algorithm that find the Kth largest element in an unsorted list, for this challenge we'll require a function 'find_kth_largest' with two parameters 'nums' to hold the unsorted list, and 'k' to hold the user input value for k, we use python's inbuilt sort function to first sort the list(it results in a list from smallest value to largest), after sorting we reverse the sorted list, reversing it makes the list start from the largest value to smallest, this step is very crucial as it's what we'll use to find the kth largest element, to find the kth latgest element we start by minusing the value of k to 1 (k-1), because list indexing starts from 0 not 1, we fininsh by returning the kth largest eleemnt from the newly sorted and reversed list, and then printing it to the console for the user to see the value of the kth largest element. 

Problem solved(Kth largest element):
1. Develop an algorithm to find the Kth largest element in an unsorted list.