
object Day4GDI {
    def main(args:Array[String]) {
        import scala.math.pow
        val L=readLine.split(" ").map(_.toDouble)
        val p = 1.0*L(0)/L(1)
        val num = readLine.trim().toInt
        val P = pow(1-p, num-1)*p
        println(f"$P%.3f")
    } 
}