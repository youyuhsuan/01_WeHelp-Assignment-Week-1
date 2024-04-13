function func(...data) {
  let middleValue;
  let check = true;
  let newData = [];

  for (let name of data) {
    middleValue = Math.floor(name.length / 2);
    let middleText = name[middleValue];
    newData.push(middleText);
    // newData.push(name.length > 3 ? name[2] : name[1]);
  }

  for (let midName in newData) {
    if (
      newData.indexOf(newData[midName]) ===
      newData.lastIndexOf(newData[midName])
    ) {
      let midNameKey = newData.indexOf(newData[midName]);
      console.log(data[midNameKey]);
      check = false;
      break;
    }
  }
  if (check) {
    console.log("沒有");
  }
}
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安
