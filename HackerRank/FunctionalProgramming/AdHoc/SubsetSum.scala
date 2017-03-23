/*
given a list of N positive integers, A = {a[1], a[2], ..., a[N]} and another integer S,
find whether there exists a non-empty subset of A whose sum is greater than or equal to S. 
 */

package FunctionalProgramming.AddHoc
object SubsetSum {

    def FindG(L:Array[Int], V:Int, depth:Int):Int = {
        val t=L.takeWhile(_<V)
        if(t.length==L.length) -1
        else t.length
    }

    def BinFind(L:Array[BigInt], V:BigInt, beg:Int, end:Int):Int = {
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
        val A=readLine().trim.split(" ").map(_.toInt)
        val sum=A.sorted.reverse.scanLeft(0:BigInt)((x,y)=>x+y)
        val T=readInt
        (1 to T).foreach(_=> {
            val S=BigInt(readLine)
            //println(FindG(sum,S,1))
            println(BinFind(sum, S, 0, sum.length-1))
        })
    }
}
