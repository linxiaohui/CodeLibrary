/*
A a working I/O template.
It includes scanning  2 integers from STDIN, calling a function, returning a value, and printing it to STDOUT.
*/

package FunctionalProgramming.Introduction;

object SolveMeFirstFP {
    def main(args: Array[String]) {
        println(io.Source.stdin.getLines().take(2).map(_.toInt).sum)
    }
}
