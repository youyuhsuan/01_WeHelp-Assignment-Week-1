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
  const isMenuVisible = navbarItems.classList.contains("show");

  navbarItems.classList.toggle("show");
  bars.style.display = isMenuVisible ? "block" : "none";
  xmark.style.display = isMenuVisible ? "none" : "block";
  navbarItems.style.width = isMenuVisible ? "0%" : "50%";
}
