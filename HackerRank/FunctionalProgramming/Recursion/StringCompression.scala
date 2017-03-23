/*
a string compression algorithm:

    If a character, chch, occurs n(>1)n(>1) times in a row, then it will be represented by {ch}{n}{ch}{n}, where {x}{x} is the value of xx. For example, if the substring is a sequence of 44 'a' ("aaaa"), it will be represented as "a4".

    If a character, chch, occurs exactly one time in a row, then it will be simply represented as {ch}{ch}. For example, if the substring is "a", then it will be represented as "a".

*/

package FunctionalProgramming.Recursion
object StringCompression
 {
    def main(args: Array[String]) {
        //val in = new java.util.Scanner (System.in).nextLine
        val in=readLine
        val out=in.foldLeft(("",in(0),0))((x,y)=> if(x._2==y) (x._1,x._2,x._3+1) else (x._1+x._2+{ if(x._3>1)x._3 else ""},y,1))
        println(out._1+out._2+{if(out._3>1) out._3 else ""})
    }
}
