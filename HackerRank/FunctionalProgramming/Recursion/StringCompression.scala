/*
a string compression algorithm:

    If a character, chch, occurs n(>1)n(>1) times in a row, then it will be represented by {ch}{n}{ch}{n}, where {x}{x} is the value of xx. For example, if the substring is a sequence of 44 'a' ("aaaa"), it will be represented as "a4".

    If a character, chch, occurs exactly one time in a row, then it will be simply represented as {ch}{ch}. For example, if the substring is "a", then it will be represented as "a".

*/

package FunctionalProgramming.Recursion
object StringCompression
 {
    def Compress(str:String):Tuple3[String,Char,Int] = {
        if(str.length<100)  {
            val in=str
            val out=in.foldLeft(("",in(0),0))((x,y)=> if(x._2==y) (x._1,x._2,x._3+1) else (x._1+x._2+{ if(x._3>1)x._3 else ""},y,1))
            out
        }
        else {
            val mid=str.length/2
            val o1=Compress(str.substring(0,mid))
            val o2=Compress(str.substring(mid))
            if(o2._1.length>0) {
                val c=o2._1(0)
                if(c!=o1._2) {
                    (o1._1+o1._2+{ if(o1._3>1) o1._3 else ""}+o2._1,o2._2, o2._3)      
                }
                else {
                     var i=1
                     var len=0
                     while(i<o2._1.length && o2._1(i)>='0' && o2._1(i)<='9') {i+=1}
                     if(i==1) {
                        len=1
                     }
                     else {
                        len=o2._1.substring(1,i).toInt
                     }
                     (o1._1+o1._2+{o1._3+len}+{if(i<o2._1.length)o2._1.substring(i)else""},o2._2,o2._3)
                }
            }
            else 
            {
                (o1._1+o1._2+{ if(o1._3>1) o1._3 else ""},o2._2, o2._3)
            }

        }
    }
    def main(args: Array[String]) {
        //val in = new java.util.Scanner (System.in).nextLine
        val in=readLine
        val out=Compress(in)
        print(out._1+out._2+{if(out._3>1) out._3 else ""})
    }
}
