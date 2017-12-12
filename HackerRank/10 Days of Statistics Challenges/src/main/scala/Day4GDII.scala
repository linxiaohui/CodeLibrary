
object Day4GDII {
    def main(args:Array[String]) {
        import scala.math.pow
        val L=readLine.split(" ").map(_.toDouble)
        val p = 1.0*L(0)/L(1)
        val num = readLine.trim().toInt
        val P = (1 to num).map { i=>
            pow(1-p, i-1)*p
        }
        println("%.3f".format(P.sum))
    }    
}