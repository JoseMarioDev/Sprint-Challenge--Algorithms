#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
Time Complexity is linear, O(n), because the number of operations needed is directly related to the size of (n). As n increases, there will be (n) number of loops until the condition returns false and the loop ends. The graph of this curve is a straight line.

b)

Time complexity is log-linear, O(nlog n). The for-loop is O(n), the while log is O(log n). You compute the total run time by multiplying the two together for O(nlog n). the graph of this line is slightly sloping.

c)
Time Complexity is O(n) because the number of operations needed is directly related to the size of n. We are performing a loop using recursion. With each loop we subtract 1 from bunnies, bringing us a step closer to our base case where we want to break out of the loop. Since we just decrease by one each time, we reach our base case in the same amount of steps as the number we pass in to the function.

## Exercise II

I would start from the middle floor and drop the egg. if the egg breaks, I would move to the midpoint between that floor and the first floor. I would drop another egg and see if it breaks. I would repeat this until I find the floor where it breaks.

if the egg doesnt break, I would move to the midpoint between the middle floor and the ceiling. drop an egg and see if it breaks. I would repeat this until I find the floor where the egg breaks.

this would be a divide and conquer approach. Time complexity would be O(log n)
