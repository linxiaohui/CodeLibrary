
object Day4BDI {
    def main(args:Array[String]) {
        import scala.math.pow
        val P=readLine.split(" ").map(_.toDouble)
        val pb = P(0)
        val pg = P(1)
        val p=(20*pow(pb, 3)*pow(pg,3)+
               15*pow(pb, 4)*pow(pg,2)+
               6*pow(pb, 5)*pow(pg,1)+
               pow(pb, 6))/pow(pb+pg,6)
        println("%.3f".format(p))
    }
}