package com.hackerrank.tutorials.statistics

/*
 * 提交到Hackerrank的代码是Python版的 

from sklearn import linear_model
m,n = [int(x) for x in input().strip().split(" ")]
x=[]
y=[]
for i in range(n):
    l=[float(x) for x in input().strip().split(" ")]
    x.append(l[:-1])
    y.append(l[-1])
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
q = int(input().strip())
for i in range(q):
    l=[float(x) for x in input().strip().split(" ")]
    r=sum([x*y for (x,y) in zip(lm.coef_,l)])+lm.intercept_
    print("{:.3f}".format(r))
*/
import org.apache.commons.math3.stat.regression.OLSMultipleLinearRegression

object ay9MLR {
    def main(args:Array[String]) {
        val m::n::Nil = readLine.trim.split(" ").toList.map(_.toInt)
        val (_x,_y) = (1 to n).map { i =>
            val in = readLine.trim.split(" ").map(_.toDouble)
            (in.slice(0, m), in(m))
        }.toArray.unzip
        val ols = new OLSMultipleLinearRegression
        ols.newSampleData(_y.toArray, _x.toArray)
        val beta = ols.estimateRegressionParameters()
        val q=readLine.trim().toInt
        (1 to q).foreach { i=>
            val in =1.0+:readLine.trim.split(" ").map(_.toDouble)
            val p = beta.zip(in)
            val r = p.foldLeft(0.0)((r,x) => r+x._1*x._2)
            println(f"$r%.2f")
        }
    }
}