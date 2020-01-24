#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
Time Complexity is O(n) because the number of operations needed is directly related to the size of (n). As n increases, there will be (n) number of loops until the condition returns false and the loop ends.

b)
Time Complexity is O(log n). As (n) grows in size the amount of operations needed does NOT increase linearly with (n). This is a nested loop, J is set to 2x itself each loop, we basically cut away half of the problem each iteration.

c)
Time Complexity is O(n) because the number of operations needed is directly related to the size of n. We are performing a loop using recursion. With each loop we subtract 1 from bunnies, bringing us a step closer to our base case where we want to break out of the loop. Since we just decrease by one each time, we reach our base case in the same amount of steps as the number we pass in to the function.

## Exercise II

I would setup a for loop and iterate through the list(n-stories). we are trying to find f(floor egg isnt broken).
I would have a nested loop while we havent reached the top of n, inside loop would be while f isnt broken. once we reach the floor where f is broken, we can take n-1 story and that would be optimum height where we can drop an egg.

since it's a nested loop the complexity would be O(log n)
