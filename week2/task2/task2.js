let JohnSchedule = Array(24).fill(true);
let BobSchedule = Array(24).fill(true);
let JennySchedule = Array(24).fill(true);
let schedule;

function consultantName(consultants) {
  for (const consultant of consultants) {
    schedule[consultant.name] = Array(24).fill(true);
  }
}

function book(consultants, hour, duration, criteria) {
  let sortCriteria;
  if (criteria === "price") {
    sortCriteria = consultants.sort((a, b) => a[criteria] - b[criteria]);
  } else {
    sortCriteria = consultants.sort((a, b) => b[criteria] - a[criteria]);
  }

  for (let consultant of sortCriteria) {
    let schedule;
    if (consultant.name === "John") {
      schedule = JohnSchedule;
    } else if (consultant.name === "Bob") {
      schedule = BobSchedule;
    } else if (consultant.name === "Jenny") {
      schedule = JennySchedule;
    }

    let availabilityCheck = true;

    for (let i = hour; i <= hour + duration; i++) {
      if (schedule[i] !== true) {
        availabilityCheck = false;
        break;
      }
    }

    if (availabilityCheck) {
      for (let i = hour; i <= hour + duration; i++) {
        schedule[i] = false;
      }
      console.log(consultant.name);
      return;
    }
  }
  console.log("No Service");
}

let consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John
