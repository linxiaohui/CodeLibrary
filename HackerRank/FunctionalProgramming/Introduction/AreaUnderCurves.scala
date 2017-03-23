
package FunctionalProgramming.Introduction;

object AreaUnderCurves {

    // This function will be used while invoking "Summation" to compute
    // The area under the curve.
    def f(coefficients:List[Int],powers:List[Int],x:Double):Double =
    {
        var d=0.0
        for((m,n)<-coefficients.zip(powers)) {
            //d+= m* ((X:Double)=>(1 to n).foldLeft(1.0)((a,b)=>a*X))(x)
            d+=m*Math.pow(x,n)
        };
        d
    }

    // This function will be used while invoking "Summation" to compute 
    // The Volume of revolution of the curve around the X-Axis
    // The 'Area' referred to here is the area of the circle obtained
    // By rotating the point on the curve (x,f(x)) around the X-Axis

    def area(coefficients:List[Int],powers:List[Int],x:Double):Double = 
    {
        val r=f(coefficients,powers,x)
        3.14159*r*r
    }

    // This is the part where the series is summed up
    // This function is invoked once with func = f to compute the area under the curve
    // Then it is invoked again with func = area to compute the volume 
    // of revolution of the curve

    def summation(func:(List[Int],List[Int],Double)=>Double,upperLimit:Int,lowerLimit:Int,coefficients:List[Int],powers:List[Int]):Double =
    {
        println(lowerLimit)
        println(upperLimit)
        var x:Double=lowerLimit
        var v=0.0
        while(x<upperLimit)  {
            v+=func(coefficients,powers,x)*0.001
            x+=0.001
        }
        v
    }

    def main(args:Array[String]) {
        val c=readLine().split(" ").map(x=>x.toInt).toList
        val p=readLine().split(" ").map(x=>x.toInt).toList
        val l=readLine().split(" ").map(x=>x.toInt)
        println(summation(f,l(1),l(0),c,p))
        println(summation(area,l(1),l(0),c,p))
    }
}