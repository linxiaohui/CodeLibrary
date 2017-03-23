/*
 given two strings, x and y,
 find the longest common prefix (p) of the two strings. 
 send substring p, x′ and y′, where x′ and y′ are the substring left after stripping p from them. 
*/
package FunctionalProgramming.Recursion
object PrefixCompression {

    def FindPrefix(x:String, y:String):String = {
        if(x.length>0 && y.length>0 && x.head==y.head) {
            x.head+FindPrefix(x.tail,y.tail)
        }
        else {
            ""
        }
    }
    def main(args: Array[String]) {
        val x=readLine
        val y=readLine
        val comm=FindPrefix(x,y)
        println(comm.length+" "+comm)
        println(x.length-comm.length+" "+x.substring(comm.length))
        println(y.length-comm.length+" "+y.substring(comm.length))
    }
}
