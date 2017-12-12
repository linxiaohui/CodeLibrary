
object Day5PDII {
    def main(args:Array[String]) {
        val means=readLine.trim().split(" ").map(_.toDouble)
        val m1 = means(0)
        val m2 = means(1)
        println("%.3f".format(160+40*(m1+m1*m1)))
        println("%.3f".format(128+40*(m2+m2*m2)))
    }
}