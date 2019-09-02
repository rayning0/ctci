/*
 * Problem: Write a function to reverse a string
*/
boolean reverse(String str) {
  char[] chars = str.toCharArray()
  int s = 0, e = chars.length - 1;
  while (s < e) {
    temp = chars[e]
    chars[e] = chars[s]
    chars[s] = temp
    s++;
    e--;
  }
  return String(chars);
}
