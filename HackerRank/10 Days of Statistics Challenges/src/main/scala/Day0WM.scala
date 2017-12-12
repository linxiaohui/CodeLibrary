
object Day0WM {
    def main(args:Array[String]) {
        val N=readInt
        val X=readLine.split(" ").map(_.toInt)
        val W=readLine.split(" ").map(_.toInt)
        val S=X.zip(W).foldLeft(0)((b, x)=>b+x._1*x._2)
        println("%.1f".format(1.0*S/W.sum))
    }
}