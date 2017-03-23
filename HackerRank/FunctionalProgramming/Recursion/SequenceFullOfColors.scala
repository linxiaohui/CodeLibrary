/*
given a sequence of NN balls in 4 colors: red, green, yellow and blue. The sequence is full of colors if and only if all of the following conditions are true:

    There are as many red balls as green balls.
    There are as many yellow balls as blue balls.
    Difference between the number of red balls and green balls in every prefix of the sequence is at most 1.
    Difference between the number of yellow balls and blue balls in every prefix of the sequence is at most 1.

*/


package FunctionalProgramming.Recursion
object SequenceFullOfColors {

    def main(args:Array[String]) {
        val T=readInt
        (1 to T).foreach(_=>{
            val S=readLine
            var R=0
            var B=0
            var Y=0
            var G=0
            var ret=true
            S.foreach(c:Char=>{
                c match {
                    case 'R'=>R+=1
                    case 'B'=>B+=1
                    case 'Y'=>Y+=1
                    case 'G'=>G+=1
                }
                if (R-G>=2 || G-R>=2 || Y-B>=2 || B-Y>=2) ret=false
            })
            println(if(ret && R==G && Y==B) "True" else "False")

        })
    }
}