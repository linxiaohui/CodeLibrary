package com.hackerrank.tutorials.statistics

import org.apache.commons.math3.stat.regression.OLSMultipleLinearRegression
import scala.Predef._

object Day8LSRL {
    def main(args:Array[String]) {
        
        val input=(1 to 5).map {i=>
            val xi=readLine.trim().split(" ").map(_.toDouble)
            (xi(0), xi(1))
        }
        val (x,y) = input.unzip
        val xx=x.map( i => Array(i))
        val ols = new OLSMultipleLinearRegression
        ols.newSampleData(y.toArray, xx.toArray)
        val beta = ols.estimateRegressionParameters()
        println("%.3f".format(80*beta(1)+beta(0)))
    }
}