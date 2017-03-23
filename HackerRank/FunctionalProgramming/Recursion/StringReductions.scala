/*
Given a string, str=s1,s2…snstr=s1,s2…sn, consisting of nn lowercase English characters (a−za−z), 
remove all of the characters that occurred previously in the string. Formally, remove all characters, sisi, 
for:

∃j,sj=si∃j,sj=si and j<i
*/

package FunctionalProgramming.Recursion;
object StringReductions
 {
    def main(args: Array[String]) {
        val in = new java.util.Scanner (System.in);
        println(in.nextLine().foldLeft("")((x,y)=> if(x.contains(y)) x else x+y))
    }
}
