/*
Given a list of N integers A = [a1, a2, ..., aN], 
find those integers which are repeated at least K times. In case no such element exists you have to print -1.
*/


package FunctionalProgramming.Recursion
object FilterElements {
    def main(args:Array[String]) {
        val T=readInt
        (1 to T).foreach(_=>{
            val X=readLine().trim().split(" ").map(x=>x.toInt).toList
            val N=X(0)
            val T=X(1)
            val S=readLine().trim().split(" ").map(x=>x.toInt).toList
            var m=new scala.collection.immutable.HashMap[Int,Int]
            S.foreach(d=>{
                if(m.contains(d))
                    m+=((d,m(d)+1))
                else
                    m+=((d,1))
            })
            var l=List[Int]()
            val o=S.filter(d=>{
                if(!l.contains(d) && m(d)>=T) {
                    l=d::l
                    true
                }
                else {
                    false
                }
            })
            o.foreach(d=>{
                print(d)
                print(" ")
            })
            if(o.length==0) {
                print(-1)
            }
            println
        })
    }
}
