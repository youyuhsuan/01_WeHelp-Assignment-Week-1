function getNumber(index) {
  let number = 0;
  for (let i = 1; i <= index; i++) {
    if (i % 3 == 0) {
      number--;
    }
    else {
      number += 4;
    }
  }
  return number;
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70