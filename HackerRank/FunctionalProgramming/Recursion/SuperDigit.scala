/*
 super digit of an integer x:
  If x has only 1 digit, then its super digit is x.
  Otherwise, the super digit of x is equal to the super digit of the digit-sum of x. 
  Here, digit-sum of a number is defined as the sum of its digits.
*/
package FunctionalProgramming.Recursion

object SuperDigit  {

    def DigitSum(n:String):String = {
        if(n.length==1) {
            n
        }
        else {
            n.foldLeft(0)((x,y)=>x+y.toString.toInt).toString
        }
    }

    def SD(n:String):String = {
        if(n.length==1) {
            n
        }
        else {
            SD(DigitSum(n))
        }
    }

    def main(args: Array[String]) {
        val l=readLine.split(" ")
        val n=l(0)
        val k=l(1)
        println(SD((SD(n).toInt*k.toInt).toString))
    }
}