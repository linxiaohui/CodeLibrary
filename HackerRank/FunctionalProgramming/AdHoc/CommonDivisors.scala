/*
 Given two integers, M and L, how many postive integers are there that are divisors to both numbers, M and L
*/

package FunctionalProgramming.Recursion
object CommonDivisors {

    def FindDivisors(X:Int, e:Int) : List[Int] = {
        if(e*e>X) {
            Nil
        }
        else if(X%e==0) {
                if(e*e==X) e::FindDivisors(X,e+1)
                else e::X/e::FindDivisors(X,e+1)
            }
            else {
                FindDivisors(X,e+1)
            }
    }

    def main(args:Array[String]) {
        val T=readInt
        (1 to T).foreach(_=>{
            val X=readLine().trim().split(" ").map(x=>x.toInt).toList
            val m=X(0)
            val l=X(1)
            val md=FindDivisors(m,1)
            val ld=FindDivisors(l,1)
            println(md.intersect(ld).length)

        })
    }
}
