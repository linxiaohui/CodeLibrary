/*
ven a list of N positive integers, A = {a[1], a[2], ..., a[N]} and another integer S,
find whether there exists a non-empty subset of A whose sum is greater than or equal to S. 
 */

package FunctionalProgramming.Recursion
object SubsetSum {

    def FindG(L:List[Int], V:Int, depth:Int):Int = {
        if(L.length<=depth) -1
        else {
            if(L(depth)>=V) depth
            else FindG(L,V,depth+1)
        }
    }

    def main(args: Array[String]) {
        val N=readInt
        val A=readLine().trim.split(" ").map(_.toInt).toList
        val sum=A.sorted.reverse.foldLeft(List(0)) { case(x,y)=> x++List(x.last+y)}
        val T=readInt
        (1 to T).foreach(_=> {
            val S=readInt
            println(FindG(sum,S,1))
        })
    }
}
