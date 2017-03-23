/*
Count the number of elements in an array without using count, size or length operators (or their equivalents)
*/

def f(arr:List[Int]):Int = arr.map(e=>1).reduce(_+_)