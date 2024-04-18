let main = document.querySelector("main");
let container = document.createElement("section");
container.className = "card-section";
let loadMore = document.querySelector(".loadmore");

function dynamicHTML(data) {
  let results = data.data.results;
  let stitleArray = [];
  let mageURLArray = [];

  for (let i = 0; i < results.length; i++) {
    let { filelist, stitle } = results[i];
    let links = filelist.split("https://");
    let mageURL = "https://" + links[1];

    stitleArray.push(stitle);
    mageURLArray.push(mageURL);
  }

  showItems(0, 13);

  loadMore.onclick = function () {
    let startIndex = container.children.length; // 目前顯示的項目數量
    showItems(startIndex, startIndex + 10); // 顯示 10 個額外的項目
  };

  console.log("🚀 ~ showItems ~ results.length:", results.length);

  function showItems(startIndex, endIndex) {
    for (let i = startIndex; i < endIndex && i < results.length; i++) {
      let card = document.createElement("div");
      card.className = "card";

      let cardImg = document.createElement("div");
      cardImg.className = "card-img";

      let img = document.createElement("img");
      img.src = mageURLArray[i];

      container.appendChild(card);
      card.appendChild(cardImg);
      cardImg.appendChild(img);

      // 只有在索引大於等於 3 時才添加 "share" 圖標
      if (i >= 3) {
        let share = document.createElement("i");
        share.className = "fa-solid fa-share";
        card.appendChild(share);
      }

      let cardTitle = document.createElement("div");
      cardTitle.className = "card-title";
      card.appendChild(cardTitle);
      let h1 = document.createElement("h1");
      h1.innerText = stitleArray[i];
      cardTitle.appendChild(h1);
    }

    if (endIndex >= results.length) {
      loadMore.style.display = "none";
    }
  }
}

let loadmoreSection = document.querySelector(".loadmore-section");
let parentElement = loadmoreSection.parentNode;
parentElement.insertBefore(container, loadmoreSection);
dynamicHTML(data);
