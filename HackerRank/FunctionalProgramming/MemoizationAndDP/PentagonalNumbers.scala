/*
Pentagonal numbers are the number of dots that can be shown in a pentagonal pattern of dots
https://www.hackerrank.com/challenges/pentagonal-numbers
*/

package FunctionalProgramming.MemoizationAndDP
object PentagonalNumbers {
    def main(args: Array[String]) {
        val T=readInt
        (1 to T).foreach(_=>{
            val N=BigInt(readInt)
            println(N+3*N*(N-1)/2)
        })
    }
}