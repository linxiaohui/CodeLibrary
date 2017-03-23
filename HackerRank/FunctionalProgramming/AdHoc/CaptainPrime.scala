/*

*/
package FunctionalProgramming.Recursion

object CaptainPrime {

    val limit=1000000

    def GenPrime(P:Set[Int], C:Set[Int], n:Int):Set[Int] = {
        if(n<=limit) {
            if(C.contains(n)) {
                GenPrime(P,C,n+2)
            }
            else {
                val C2=C|(2 to limit/n).map(_*n).toSet
                GenPrime(P+n,C2,n+2)
            }
        }
        else {
            P
        }
    }

    def Split(V:Int, Base:Int, R:List[List[Int]]):List[List[Int]] = {
        if(V<Base) {
            R
        }
        else {
            val R2=List((V%Base)::R(0), (V/Base)::R(1))
            Split(V, Base*10, R2)
        }
    }

    def CP(V:Int,p:Set[Int]):String = {
        val S=Split(V,10,List(List[Int](),List[Int]()))
        val l=S(0)
        val r=S(1)
        if(p.contains(V)) {
            val L=l.forall(p.contains(_))
            val R=r.forall(p.contains(_))
            if(L&&R) {
                "CENTRAL"
            }
            else if(L) {
                "LEFT"
            }
            else if(R) {
                "RIGHT"
            }
            else {
               "DEAD" 
            }

        }
        else {
            "DEAD"
        }
    }

    def main(args:Array[String]) {
        val T=readInt
        val p=GenPrime(Set(2),Set(4),3)
        (1 to T).foreach(_=> {
            val V=readInt
            println(CP(V,p))
        })
    }
}