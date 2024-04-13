// task1
function findAndPrint(messages, currentStation) {
  let SongshanXindian_Line = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjing Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xiaobitan",
    "Xindian City Hall",
    "Xindian",
  ];
  let currentPosition = SongshanXindian_Line.indexOf(currentStation);
  let comparisonValue = Infinity;
  let SongshanXindian_Line_tempVaule;

  let nearFriend = "";
  for (let [name, value] of Object.entries(messages)) {
    for (let i = 0; i < SongshanXindian_Line.length; i++) {
      if (value.includes(SongshanXindian_Line[i])) {
        SongshanXindian_Line_tempVaule = Math.abs(i - currentPosition);
        if (currentStation === "Xindian City Hall" && SongshanXindian_Line[i]) {
          SongshanXindian_Line_tempVaule = Math.abs(currentPosition - i);
          nearFriend = name;
          break;
        } else if (SongshanXindian_Line_tempVaule < comparisonValue) {
          comparisonValue = SongshanXindian_Line_tempVaule;
          nearFriend = name;
        }
      }
    }
  }
  console.log(nearFriend);
  return nearFriend;
}

const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bobc
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// task2
function createSchedule(consultants) {
  let schedule = {};
  for (const consultant of consultants) {
    schedule[consultant.name] = Array(24).fill(true);
  }
  return schedule;
}

function book(schedule, consultants, hour, duration, criteria) {
  let sortCriteria;
  if (criteria === "price") {
    sortCriteria = consultants.sort((a, b) => a[criteria] - b[criteria]);
  } else {
    sortCriteria = consultants.sort((a, b) => b[criteria] - a[criteria]);
  }

  for (let consultant of sortCriteria) {
    let consultantSchedule = schedule[consultant.name];
    let availabilityCheck = true;

    for (
      let i = hour;
      i < Math.min(hour + duration, consultantSchedule.length);
      i++
    ) {
      if (!consultantSchedule[i]) {
        availabilityCheck = false;
        break;
      }
    }

    if (availabilityCheck) {
      for (
        let i = hour;
        i < Math.min(hour + duration, consultantSchedule.length);
        i++
      ) {
        consultantSchedule[i] = false;
      }
      console.log(consultant.name);
      return consultant.name;
    }
  }
  console.log("No Service");
  return "No Service";
}

let consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

let schedule = createSchedule(consultants);

book(schedule, consultants, 15, 1, "price"); // Jenny
book(schedule, consultants, 11, 2, "price"); // Jenny
book(schedule, consultants, 10, 2, "price"); // John
book(schedule, consultants, 20, 2, "rate"); // John
book(schedule, consultants, 11, 1, "rate"); // Bob
book(schedule, consultants, 11, 2, "rate"); // No Service
book(schedule, consultants, 14, 3, "price"); // John

// task3
function func(...data) {
  let middleValue;
  let check = true;
  let newData = [];

  for (let name of data) {
    middleValue = Math.floor(name.length / 2);
    let middleText = name[middleValue];
    newData.push(middleText);
  }

  for (let midName in newData) {
    if (
      newData.indexOf(newData[midName]) ===
      newData.lastIndexOf(newData[midName])
    ) {
      let midNameKey = newData.indexOf(newData[midName]);
      check = false;
      console.log(data[midNameKey]);
      return data[midNameKey];
    }
  }
  if (check) {
    console.log("沒有");
    return "沒有";
  }
}
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

// task4
function getNumber(index) {
  let number = 0;
  for (let i = 1; i <= index; i++) {
    if (i % 3 == 0) {
      number--;
    } else {
      number += 4;
    }
  }
  console.log(number);
  return number;
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

// task5
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
        console.log(j);
        return j;
      }
    }
  }
  console.log(-1);
  return -1;
}

let a = find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
let b = find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
let c = find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
