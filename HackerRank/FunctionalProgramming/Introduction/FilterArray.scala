/*
Filter a given array of integers and output only those values that are less than a specified value X.
The output integers should be in the same sequence as they were in the input
*/

package FunctionalProgramming.Introduction;

object FilterArray {
    def f(delim:Int,arr:List[Int]):List[Int] = for(x<-arr; if x<delim) yield x
    def f2(delim:Int,arr:List[Int]):List[Int] = arr.filter(x=> if(x<delim) true else false)
    def main(args: Array[String]) {
        val arr=List(1,2,3,5,8,2,5,7,21,11,12,32)
        println(f(10,arr))
        println(f2(10,arr))
    }
}
