/*
ingling two strings, P=p1p2…pnP=p1p2…pn and Q=q1q2…qnQ=q1q2…qn, both of length nn, will result in the creation of a new string RR of length 2×n2×n. It will have the following structure:

R=p1q1p2q2…pnqn
*/


package FunctionalProgramming.Recursion
object StringMingling {
    def main(args: Array[String]) {
        val P=readLine
        val Q=readLine
        print(P.zip(Q).map({case(x,y)=>x.toString+y}).mkString)
    }
}
