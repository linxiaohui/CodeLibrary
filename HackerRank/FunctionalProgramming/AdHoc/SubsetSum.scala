/*
ven a list of N positive integers, A = {a[1], a[2], ..., a[N]} and another integer S,
find whether there exists a non-empty subset of A whose sum is greater than or equal to S. 
 */

package FunctionalProgramming.Recursion
object SubsetSum {

    def FindG(L:List[Int], V:Int, depth:Int):Int = {
        val t=L.takeWhile(_<V)
        if(t.length==L.length) -1
        else t.length
    }

    def BinFind(L:List[Int], V:Int, beg:Int, end:Int):Int = {
        if(L(end)<V) {
            -1
        }
        else {
            if(beg==end) {
                beg
            }
            else if(beg+1==end) {
                if(L(beg)>=V) beg
                else end
            }
            else {
                val mid=(beg+end)/2
                if(L(mid)<V) BinFind(L, V, mid, end)
                else BinFind(L, V, beg, mid)
            }
        }
    }

    def main(args: Array[String]) {
        val N=readInt
        val A=readLine().trim.split(" ").map(_.toInt).toList
        val sum=A.sorted.reverse.foldLeft(List(0)) { case(x,y)=> x++List(x.last+y)}
        val T=readInt
        (1 to T).foreach(_=> {
            val S=readInt
            //println(FindG(sum,S,1))
            println(BinFind(sum, S, 0, sum.length-1))
        })
    }
}
