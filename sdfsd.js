instString = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];

result = instString
  .filter((n) => n > 5)
  .map((n) => n * 100)
  .join(":");

console.log(result);
console.log(typeof result[0]);

instString.forEach((n, i, a) => console.log(i, n, a[i+1]))