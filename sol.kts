import java.util.Scanner;
val reader = Scanner(System.`in`);

var prev = HashMap<Char, Char>();
var next = HashMap<Char, Char>();

for (i in 'a'..'z') {
  prev[i] = 'a'
  next[i] = 'z'
}
prev['a'] = 'b'
next['z'] = 'y'

fun solve() {
  val s = readLine()!!
  for (i in 0..s.length - 1) {
    if (i % 2 == 0)
      print(prev[s[i]])
    else
      print(next[s[i]])
  }
  println()
}

fun main() {
  var tests = readLine()!!.toInt()
  while (tests > 0) {
    solve()
    tests--
  }
}
