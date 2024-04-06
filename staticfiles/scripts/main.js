let nav = document.querySelector(".nav");
let hamburger = document.querySelector(".nav--hamburger-menu");
let hamburger_top = document.querySelector(".nav--hamburger-menu-top");
let hamburger_center = document.querySelector(".nav--hamburger-menu-center");
let hamburger_down = document.querySelector(".nav--hamburger-menu-down");
let content = document.querySelector(".nav--content");
let arrow = document.querySelector(".header--arrow-down");

nav.addEventListener("click", () => {
  content.classList.toggle("visible");
  content.classList.toggle("top-down");
  hamburger_top.classList.toggle("tilt-hamburger-down");
  hamburger_center.classList.toggle("invinsible");
  hamburger_down.classList.toggle("tilt-hamburger-up");
  arrow.classList.toggle("top-down");
});
