/*
find the differences between each list
*/

package FunctionalProgramming.AdHoc;
object  MissingNumbers {

    def main(args:Array[String]) {
        val n=readInt
        val A=readLine().trim.split(" ").map(_.toInt).toList
        val m=readInt
        val B=readLine().trim.split(" ").map(_.toInt).toList
        val diff=(B diff A).distinct
        println(diff.sorted.map(_.toString) mkString " ")

    }
}