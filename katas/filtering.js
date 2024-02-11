let intArr = [1, -2, 3, -4, 5, 6, -7, 8, -9];

let postiveArr = intArr
    .filter((num) => num > 0)
    .join("-");

console.log(postiveArr);