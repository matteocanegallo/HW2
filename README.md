# HW2
The perform file measure the time that two functions(quicksort and mergesort) take to add n random values to a list and put those values in the correct order.
The quicksort function choose a pivot to split the list in 2 sub-list:values smaller than the pivot, values greater than the pivot. Everytime the list is splitted another pivot is choosen and the  same process is repeated until each element is in the right position.
The mergesort function divide the list into two halves recursively until it cannot more be divided and then the singular elements of the are compared generating sorted sub-lists. Then these sub-lists are compared themselves until an unique list is created.
In the perform file 10 different lists with 1000 random elements are created, and then is measured the time to sort each list with the two different sorting function and then, the times taken from the functions to sort and the difference between them are printed.
The results show that for list up to 10000 elements the quicksort function is faster, but for lists of 100000 elements or more the mergesort is faster.
