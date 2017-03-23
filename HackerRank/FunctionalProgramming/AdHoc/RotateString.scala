/*
 display all nn rotations of string S. 
*/

package FunctionalProgramming.AdHoc;
object RotateString {

    def Rotates(s:String, n:Int):Unit = {
        if(n>0) {
            print(s.tail+s.head+" ")
            Rotates(s.tail+s.head,n-1)
        }
    }
    def main(args: Array[String]) {
        val T=readInt()
        for(i<-(1 to T)) {
            val S=readLine
            Rotates(S,S.length)
            println
        }
    }
}

