package code.rosetta

import java.nio.file.{ Files, FileSystems }
import java.io.File
import scala.language.implicitConversions
import java.io.FileOutputStream

object OpFile extends App {
  val defaultFS = FileSystems.getDefault()
  val separator = defaultFS.getSeparator()
  def test(filename: String) {
    val path = defaultFS.getPath(filename)
    // Scala 2.10.0 supports direct string interpolation
    // by putting "s" at the beginning of the string.
    println(s"The following ${if (Files.isDirectory(path)) "directory" else "file"} called $filename" +
      (if (Files.exists(path)) " exists." else " not exists."))
  }

  List("output.txt", separator + "output.txt", "docs", separator + "docs" + separator).foreach(test)

  //按行读取文件
  scala.io.Source.fromFile("input.txt").getLines().foreach {
    line =>
      println(line)
  }

  // 文件的创建、删除

  try { new File("output.txt").createNewFile() }
  catch { case e: Exception => println(s"Exception caught: $e with creating output.txt") }
  try { new File(s"${File.separator}output.txt").createNewFile() }
  catch { case e: Exception => println(s"Exception caught: $e with creating ${File.separator}output.txt") }
  try { new File("docs").mkdir() }
  catch { case e: Exception => println(s"Exception caught: $e with creating directory docs") }
  try { new File(s"${File.separator}docs").mkdir() }
  catch { case e: Exception => println(s"Exception caught: $e with creating directory ${File.separator}docs") }
  try { new File("output.txt").delete() }
  catch { case e: Exception => println(s"Exception caught: $e with deleting file output.txt") }
  try { new File(s"${File.separator}docs").delete() }
  catch { case e: Exception => println(s"Exception caught: $e with deleting directory ${File.separator}docs") }

  new java.io.File("/path/to/dir").mkdirs
  def mkdirs(path: List[String]) = // return true if path was created
    path.tail.foldLeft(new File(path.head)) { (a, b) => a.mkdir; new File(a, b) }.mkdir
  mkdirs(List("/path", "to", "dir"))

  //文件重命名
  implicit def file(s: String) = new File(s) // will be converted to new File(String)
  "myfile.txt" renameTo "anotherfile.txt"
  "/tmp/myfile.txt" renameTo "/tmp/anotherfile.txt"
  "mydir" renameTo "anotherdir"
  "/tmp/mydir" renameTo "/tmp/anotherdir"

  List(("myfile.txt", "anotherfile.txt"), ("/tmp/myfile.txt", "/tmp/anotherfile.txt"),
    ("mydir", "anotherdir"), ("/tmp/mydir", "/tmp/anotherdir")).foreach {
      case (oldf, newf) =>
        new java.io.File(oldf) renameTo new java.io.File(newf)
    }

  //遍历目录
  val dir = new File("/foo/bar").list()
  dir.filter(file => file.endsWith(".mp3")).foreach(println)

  def walkTree(file: File): Iterable[File] = {
    val children = new Iterable[File] {
      def iterator = if (file.isDirectory) file.listFiles.iterator else Iterator.empty
    }
    Seq(file) ++: children.flatMap(walkTree(_))
  }

  val dir2 = new File("/home/user")
  for (f <- walkTree(dir2)) println(f)
  for (f <- walkTree(dir2) if f.getName.endsWith(".mp3")) println(f)

  //文件截断

  val outChan = new FileOutputStream(args(0), true).getChannel()
  val newSize = args(1).toLong
  outChan.truncate(newSize)

}