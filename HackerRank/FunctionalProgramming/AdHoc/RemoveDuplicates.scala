/*
given a string, str, of length N consisting of lowercase letters of alphabet,
remove all those characters from str which have already appeared in it, i.e., 
keep only first occurance of each letter
*/

package FunctionalProgramming.AdHoc;
object RemoveDuplicates {
    def main(args: Array[String]) {
        val in = readLine
        println(in.foldLeft("")((x,y)=>if(x.contains(y)) x else x+y))
    }
}
