/*
find the differences between each list
*/

package FunctionalProgramming.AdHoc;
object  MissingNumbers {

    def FindDiff(ma:Map[Int,Int], mb:Map[Int,Int], e:List[Int]):List[Int] = {
        //println(mb.size)
        if(mb.size>0) {
            val m=mb.max._1
            println(m)
            if(mb(m)>ma(m) && !e.contains(m)) {
                m::FindDiff(ma, mb- m, m::e)
            }
            else {
                FindDiff(ma, mb- m, m::e)
            }

        }
        else {
            Nil
        }
    }
    def main(args:Array[String]) {
        val n=readInt
        val A=readLine().trim.split(" ").map(_.toInt).toList
        val m=readInt
        val B=readLine().trim.split(" ").map(_.toInt).toList
        val Ma=A.groupBy(x=>x).map {case(x,y) => (x,y.length)}
        val Mb=B.groupBy(x=>x).map {case(x,y) => (x,y.length)}
        val diff=FindDiff(Ma,Mb,List[Int]())
        println(diff.sorted.map(_.toString) mkString " ")

    }
}