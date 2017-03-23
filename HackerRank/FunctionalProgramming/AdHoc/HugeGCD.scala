/*
Given  N smaller integers whose product is A, and M integers with product B
compute the greatest common divisor of the two positive integers 10**9+7
 */
package FunctionalProgramming.AddHoc
object HugeGCD {

    def HGCD(A:BigInt, B:BigInt):BigInt = {
        if(A>B) {
            if(A%B==0) B
            else {
                HGCD(A%B, B)
            }
        }
        else {
            if(B%A==0) A
            else HGCD(B%A, A)
        }
    }

    def main(args: Array[String]) {
        val N=readInt
        val AL=readLine().trim.split(" ").map(_.toInt)
        val M=readInt
        val BL=readLine().trim.split(" ").map(_.toInt)
        val A=AL.foldLeft(1:BigInt)(_*_)
        val B=BL.foldLeft(1:BigInt)(_*_)
        println(HGCD(A,B)%(1000000007))
    }
}
