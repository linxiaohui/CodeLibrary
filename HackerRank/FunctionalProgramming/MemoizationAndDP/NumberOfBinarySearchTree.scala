/*
 given N nodes, how many different binary search tree can be created using all of them
*/

package FunctionalProgramming.MemoizationAndDP
object PentagonalNumbers {

    val limit=1000

    def Cat(n:Int,R:List[BigInt]):List[BigInt] = {
        if(n>limit) R
        else {
            val r = (0 to n-1).map(x=>R(x)*R(n-1-x)).reduce(_+_)
            Cat(n+1, R++List(r))
        }
    }

    def main(args: Array[String]) {
        val T=readInt
        val C=Cat(2, List(BigInt(1),BigInt(1)))
        (1 to T).foreach(_=>{
            val N=readInt
            println(C(N)%100000007)
        })
    }
}