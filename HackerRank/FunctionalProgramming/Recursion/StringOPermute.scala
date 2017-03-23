/*
given a string str of length L where L is even, 
swap the characters at position ii and i+1i+1, where i∈i∈{0,2,..,L−20,2,..,L−2}. 
*/

package FunctionalProgramming.Recursion
object StringOPermute {

    def OPermute(in:String):String = {
        if(in.length==2) in.last.toString+in.head.toString
        else {
            val half=in.length/2
            val first=in.substring(0,half)
            val second=in.substring(half)
            if(half%2==0)  {
                OPermute(first)+OPermute(second)
            }
            else {
                OPermute(first.init)+second.head+first.last+OPermute(second.tail)
            }
        }
    }

    def main(args:Array[String]) {
        val N=readInt
        (1 to N).foreach(_=> {
            val l=readLine

            println(OPermute(l))
        })
    }
}
