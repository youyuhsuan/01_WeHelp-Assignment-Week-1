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
