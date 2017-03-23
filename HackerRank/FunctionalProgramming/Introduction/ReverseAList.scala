/*
given a list of NN elements. Reverse the list without using the reverse function.
*/

def f(arr:List[Int]):List[Int] = if(arr.length==0) Nil else f(arr.tail)::arr.head::Nil