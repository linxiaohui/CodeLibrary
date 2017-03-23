/*
Least Common 
 */

package FunctionalProgramming.AddHoc
object JumpingBunnies  {

    def GCD(a:BigInt,b:BigInt):BigInt = {
        if(a>b) {
            if(a%b==0) b
            else GCD(a%b,b)
        }
        else {
            if(b%a==0) a
            else GCD(b%a,a)
        }
    }

    def LCM(a:BigInt,b:BigInt):BigInt = {
        a*b/GCD(a,b)
    }

    def main(args: Array[String]) {
        val N=readInt
        val A=readLine().trim.split(" ").map(BigInt(_))
        println(A.foldLeft(BigInt(1))((x,y)=>LCM(x,y)))
    }
}