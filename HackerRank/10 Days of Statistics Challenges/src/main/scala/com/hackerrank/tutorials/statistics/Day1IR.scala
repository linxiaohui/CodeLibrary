
package com.hackerrank.tutorials.statistics

object Day1IR {
    def median(L:Array[Int]) = {
        val s=L.length
        if(s%2==1) L(s/2) else (L(s/2-1)+L(s/2))/2.0
    }

    def main(args:Array[String]) {
        val N=readInt
        val X=readLine.split(" ").map(_.toInt)
        val F=readLine.split(" ").map(_.toInt)
        val L = X.zip(F).foldLeft(List[Int]()) {
            (l,x)=>l:::List.fill(x._2)(x._1)
        }.sorted.toArray
        val q1 = median(L.slice(0, L.length/2))
        val q3 = median(L.slice((L.length+1)/2, L.length))
        println("%.1f".format(q3-q1))
    }
}