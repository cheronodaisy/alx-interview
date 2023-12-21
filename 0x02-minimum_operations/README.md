0. Minimum Operations
In a text file, there is a single character, H. Your text editor can 
execute only two operations in this file: Copy All and Paste. Given a 
number n, write a method that calculates the fewest number of operations 
needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

The solution works by iteratively performing copy-and-paste operations 
based on certain conditions until the desired count of 'H's (n) is achieved in the file. 
It's a simulation-based rather than a dynamic programming one, 
computing the operations directly to reach the desired count. 
