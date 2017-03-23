Array Of N Elements

/*
Create an array of N amount of integers
*/
def f(num:Int) : List[Int] = ("1 "*num).split(" ").map(_.toInt).toList

def f2(num:Int):List[Int] = (1 to num).toList