/*
For a given list with NN integers, return a new list removing the elements at odd positions.
*/

def f(arr:List[Int]):List[Int] = if(arr.size<=1) Nil else arr(1)::f(arr.tail.tail)