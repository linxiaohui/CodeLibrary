/*
 super digit of an integer x:
  If x has only 1 digit, then its super digit is x.
  Otherwise, the super digit of x is equal to the super digit of the digit-sum of x. 
  Here, digit-sum of a number is defined as the sum of its digits.
*/
package FunctionalProgramming.Recursion

object SuperDigit  {

    def DigitSum(n:BigInt):BigInt = {
        if(n<10) {
            n
        }
        else {
            n%10+DigitSum(n/10)
        }
    }

    def SD(n:BigInt):BigInt = {
        if(n<10) {
            n
        }
        else {
            SD(DigitSum(n))
        }
    }

    def main(args: Array[String]) {
        val l=readLine.split(" ")
        val n=BigInt(l(0))
        val k=BigInt(l(1))
        println(SD(DigitSum(n)*k))
    }
}