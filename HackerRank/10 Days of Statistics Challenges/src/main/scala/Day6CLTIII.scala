import breeze.stats.distributions.Gaussian

object Day6CLTIII {
    def main(args:Array[String]) {
        val sample=readLine.trim().toDouble
        val u=readLine.trim().toDouble
        val dev=readLine.trim().toDouble
        val range=readLine.trim().toDouble
        val z=readLine.trim().toDouble
        val g = Gaussian(u,dev/scala.math.sqrt(sample))
        println("%.2f".format(g.icdf(0.025)))
        println("%.2f".format(g.icdf(0.975)))
    }    
}