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
  let Xiaobitan_Line = ["Qizhang", "Xiaobitan"];
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
