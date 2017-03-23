/*
The series expansion of eexx is given by:

1+x+x1+x+x22/2!+x/2!+x33/3!+x/3!+x44/4!/4! +.......+.......

Evaluate ex for given values of xx by using the above expansion for the first 10 terms. 
*/

def f(x: Float):Float= {   
    // Compute and Return the value of e^x 
    (0 to 9).map(n=>{scala.math.pow(x,n)/(1 to n).product}).map(_.toFloat).reduce(_+_)
}
