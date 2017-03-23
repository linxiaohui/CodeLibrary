/*
given the cartesian coordinates of a set of points in a 2D plane. 
When traversed sequentially[clockwise], these points form a Polygon, P, which is not self-intersecting in nature.
compute the area of polygon PP?

Referer: 
1. http://www.mathopenref.com/coordpolygonarea2.html
2. https://www.mathsisfun.com/geometry/area-irregular-polygons.html
3. http://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
4. http://geomalgorithms.com/a01-_area.html
*/
package FunctionalProgramming.Introduction;
object ComputeTheAreaOfPolygon {
    def main(args:Array[String]) {
        val N=readInt()
        var a=0.0
        val coordinates=(1 to N).map(x=>readLine().split(" ").map(_.toInt))
        for(i<-(1 to N-1)) {
            a+=(coordinates(i)(0)+coordinates(i-1)(0))*(coordinates(i-1)(1)-coordinates(i)(1))/2.0
        }
        a+=(coordinates(N-1)(0)+coordinates(0)(0))*(coordinates(N-1)(1)-coordinates(0)(1))/2.0
        println(a.abs)
    }
}