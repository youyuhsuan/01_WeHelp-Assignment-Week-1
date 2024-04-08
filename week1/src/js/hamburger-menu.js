let navbarNav = document.querySelector(".navbar-nav");
let hamburger = navbarNav.querySelector(".menu");
let bars = navbarNav.querySelector(".fa-bars");
let xmark = navbarNav.querySelector(".fa-xmark");
let navbarItems = navbarNav.querySelector(".navbar-items");
bars.style.display = "block";
xmark.style.display = "none";

hamburger.onclick = function () {
  menuBtn();
};

function menuBtn() {
  let isVisible = navbarItems.classList.contains("show");

  if (isVisible) {
    navbarItems.classList.remove("show");
    navbarItems.style.width = "0%";
    bars.style.display = "block";
    xmark.style.display = "none";
  } else {
    navbarItems.classList.add("show");
    navbarItems.style.width = "50%";
    bars.style.display = "none";
    xmark.style.display = "block";
  }
}
