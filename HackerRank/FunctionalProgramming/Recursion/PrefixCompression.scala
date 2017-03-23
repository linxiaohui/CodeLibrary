/*
 given two strings, x and y,
 find the longest common prefix (p) of the two strings. 
 send substring p, x′ and y′, where x′ and y′ are the substring left after stripping p from them. 
*/
package FunctionalProgramming.Recursion
object PrefixCompression {

    /*prequire: x.length==y.length*/
    def FindPrefix(x:String, y:String):String = {
        if(x.length==1) {
            if(x==y) x else ""
        }
        else {
            val mid=x.length/2
            if(x.substring(0,mid)==y.substring(0,mid)) {
                x.substring(0,mid)+FindPrefix(x.substring(mid),y.substring(mid))
            }
            else {
                FindPrefix(x.substring(0,mid),y.substring(0,mid))
            }
        }
    }
    def main(args: Array[String]) {
        val x=readLine
        val y=readLine
        val m=List(x.length,y.length).min
        val comm=FindPrefix(x.substring(0,m),y.substring(0,m))
        println(comm.length+" "+comm)
        println(x.length-comm.length+" "+x.substring(comm.length))
        println(y.length-comm.length+" "+y.substring(comm.length))
    }
}
