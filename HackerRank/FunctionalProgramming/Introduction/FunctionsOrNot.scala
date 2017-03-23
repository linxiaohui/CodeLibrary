/*
given a set of unique (x,y) ordered pairs constituting a relation. 
The x-values form the domain, and the y-values form the range to which they map. 
For each of these relations, identify whether they may possibly represent a valid function or not. 
*/

package FunctionalProgramming.Introduction;
object FunctionsOrNot {

    def main(args: Array[String]) {
        val T=readInt()
        for(i<-(1 to T)) {
            val N=readInt()
            val l=(1 to N).map(x=>readLine().split(" ").map(_.toInt))
            val r=l.foldLeft((true,List[Array[Int]]()))((x,y)=>(x._1&&(if(x._2.map(t=>t(0)).contains(y(0))&& !x._2.contains(y)) false else true),y::x._2))
            println(if(r._1) "YES" else "NO")
        }
    }
}