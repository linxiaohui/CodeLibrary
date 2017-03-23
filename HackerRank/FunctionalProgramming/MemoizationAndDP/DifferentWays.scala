/*
 how many different team can be formed by selecting K out of N lemurs.
*/

package FunctionalProgramming.MemoizationAndDP
object DifferentWays {

    def main(args: Array[String]) {
        val T=readInt
        (1 to T).foreach(_=> {
            val l=readLine.trim.split(" ").map(_.toInt).toList
            val N=BigInt(l(0))
            val K=BigInt(l(1))
            println(((K+1 to N).product/(BigInt(1) to N-K).product)%(100000007))

        })

    }

}