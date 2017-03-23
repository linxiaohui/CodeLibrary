/*
Given a list, repeat each element in the list nn amount of times. 
*/

def f(num:Int,arr:List[Int]):List[Int] = arr.map(e=>((e+" ")*num).split(" ")).flatten.map(_.toInt)
