/*
Find the number of ways that a given integer, X,
can be expressed as the sum of the Nth power of unique, natural numbers. 
*/
package FunctionalProgramming.Recursion;

object TheSumsOfPowers {

    def FindMax(X:Int, N:Int, e:Int):Int = {
        if(Math.pow(e,N)>X)
        e
        else 
        FindMax(X,N,e+1) 
    }

    def RecursionWays(indx:Int, N:Int, L:List[Int]):Int = {
        if(L(indx)==N) 1
        else if(L(indx)>N) 0
        else {
            (indx+1 to L.length-1).map(RecursionWays(_, N-L(indx),L)).sum
        }
    }

    def numberOfWays(X:Int,N:Int):Int = {
        val MAX=FindMax(X,N,1)
        val seq=(1 to MAX).toList.map(Math.pow(_, N).toInt)
        (0 to MAX-1).map(RecursionWays(_, X, seq)).toList.sum
    }

    def main(args: Array[String]) {
       println(numberOfWays(readInt(),readInt()))
    }

}
