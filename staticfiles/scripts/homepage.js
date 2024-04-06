const inputField = document.querySelector(".send--input");
const messageForm = document.forms.sendform;
const messageBox = document.querySelector(".body");
let typing_container = document.querySelector(".typing-container");


inputField.addEventListener("keyup", (e) => {
  let timeout = null;
  userHasTyped = inputField.value.length;
  let span = document.querySelectorAll(".dot");
  //   typing_container.innerHTML = `typing${userHasTyped}`;
  span.forEach((e) => {
    e.classList.add("flow");
  });

  if (timeout) {
    clearTimeout(timeout);
  }

  timeout = setTimeout(() => {
    span.forEach((e) => {
      e.classList.remove("flow");
    });
    // typing_container.innerHTML = "";
  }, 3000);
});

let searchForm = document.forms.searchform;
searchForm.addEventListener("mousedown", () => {
  searchForm.classList.add("view-input");
  searchForm.classList.add("collapse-icons");
  searchForm.classList.add("view-results");
});

//
let settings_icon = document.querySelector(".settings-icon");
let languages_icon = document.querySelector(".languages-icon");

settings_icon.addEventListener("mousedown", () => {
  settings_icon.classList.toggle("view-settings");
});

languages_icon.addEventListener("mousedown", () => {
  languages_icon.classList.toggle("view-languages");
});
