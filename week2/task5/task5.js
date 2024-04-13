function find(spaces, stat, n) {
  let availSeat = spaces.slice();
  for (let i = 0; i < stat.length; i++) {
    if (stat[i] == 0) {
      availSeat[i] = 0;
    }
  }

  for (let i = n; i <= Math.max(...availSeat); i++) {
    for (let j = 0; j < availSeat.length; j++) {
      if (availSeat[j] == i) {
        return j;
      }
    }
  }
  return -1;
}

let a = find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
let b = find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
let c = find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
