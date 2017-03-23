 /*
given a list. Return the sum of odd elements from the given list.
 */

 def f(arr:List[Int]):Int = arr.filter(e=> e%2!=0).sum