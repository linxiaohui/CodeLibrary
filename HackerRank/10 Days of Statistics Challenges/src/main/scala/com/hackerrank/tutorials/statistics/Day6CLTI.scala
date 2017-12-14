
package com.hackerrank.tutorials.statistics

import breeze.stats.distributions.Gaussian

object Day6CLTI {
    def main(args:Array[String]) {
        val limit=readLine.trim().toInt
        val boxes=readLine.trim().toInt
        val u=readLine.trim().toInt
        val dev=readLine.trim().toInt
        val g = Gaussian(u,dev/scala.math.sqrt(boxes))
        println("%.4f".format(g.cdf(1.0*limit/boxes)))
    }
}