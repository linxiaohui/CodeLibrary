/*
Given a list of N integers A = [a1, a2, ..., aN], 
find those integers which are repeated at least K times. In case no such element exists you have to print -1.
*/


package FunctionalProgramming.Recursion
object FilterElements {

    def Filterer(l:List[Int], m:Map[Int,Int], k:Int, e:List[Int]):List[Int] ={
        if(l.length>0) {
            val first=l.head
            if(m(first)>=k && !e.contains(first)) {
                first::Filterer(l.tail, m, k, first::e)
            }
            else {
                Filterer(l.tail, m, k, e)
            }
        }
        else {
            Nil
        }
    }
    def main(args:Array[String]) {
        val T=readInt
        (1 to T).foreach((z:Int)=>{
            //readInt() reads the whole line and try to parse the integer from it
            //val N=readInt
            //val T=readInt
            val X=readLine().trim().split(" ").map(x=>x.toInt).toList
            val N=X(0)
            val T=X(1)
            val S=readLine().trim().split(" ").map(x=>x.toInt).toList
            //val m=S.map((d:Int)=>(d,1)).groupBy(_._1).map { case(x,y)=>(x,y.length) }
            //val m=S.map(_=>(_,1)).groupBy(_._1).map { case(x,y)=>(x,y.length) }: ERROR
            val m=S.map((_,1)).groupBy(_._1).map { case(x,y)=>(x,y.length) }
            val o=Filterer(S,m,T,List[Int]())
            if(o.length==0) {
                println(-1)
            }
            else {
                println(o.map(_.toString).mkString(" "))
            }
        })
    }
}
