/*
given the cartesian coordinates of a set of points in a 2D plane. 
When traversed sequentially[clockwise], these points form a Polygon, P, which is not self-intersecting in nature.
compute the perimeter of polygon P? 
*/

package FunctionalProgramming.Introduction;
object ComputeThePerimeterOfPolygon {
    def main(args:Array[String]) {
        val N=readInt()
        var p=0.0
        val coordinates=(1 to N).map(x=>readLine().split(" ").map(_.toInt))
        for(i<-(1 to N-1)) {
            p+=Math.sqrt((coordinates(i)(0)-coordinates(i-1)(0))*(coordinates(i)(0)-coordinates(i-1)(0))+(coordinates(i)(1)-coordinates(i-1)(1))*(coordinates(i)(1)-coordinates(i-1)(1)))
        }
        p+=Math.sqrt((coordinates(N-1)(0)-coordinates(0)(0))*(coordinates(N-1)(0)-coordinates(0)(0))+(coordinates(N-1)(1)-coordinates(0)(1))*(coordinates(N-1)(1)-coordinates(0)(1)))
        println(Math.round(10*p)/10.0)
    }
}